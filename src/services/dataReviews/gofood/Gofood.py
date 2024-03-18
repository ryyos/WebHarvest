import os
import datetime as date

from requests import JSONDecodeError
from zlib import crc32
from time import time
from icecream import ic
from typing import List, Dict, Tuple
from dekimashita import Dekimashita
from dotenv import *

from .dependency import GofoodLibs
from src.utils import *
from src.server import S3

class Gofood(GofoodLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__(options.get('save'))

        self.SAVE_TO_S3 = options.get('s3')
        self.SAVE_TO_LOKAL = options.get('save')
        self.USING_THREADS = options.get('threads')


    def __get_review(self, raw_json: dict):
        details: dict = self.write_detail(raw_json)

        response: int = S3.upload_json(
            destination=details["path_detail"],
            body=raw_json,
            send=self.SAVE_TO_S3
        )

        if self.SAVE_TO_LOKAL:
            File.write_json(path=details["path_detail"], content=details["data_detail"])

        reviews: dict = self.collect_reviews(raw_json)
        raw_json["total_reviews"] = len(reviews["all_reviews"])
        
        for index, comment in enumerate(reviews["all_reviews"]):
            detail_reviews = {
                "id_review": comment["id"],
                "username_reviews": comment["author"]["fullName"],
                "initialName": comment["author"]["initialName"],
                "image_reviews": comment["author"]["avatarUrl"],
                "created_time": comment["createdAt"].split('.')[0].replace('T', ' '),
                "created_time_epoch": Time.convert_time(comment["createdAt"]),
                "email_reviews": None,
                "company_name": None,
                "location_reviews": None,
                "title_detail_reviews": None,
                "reviews_rating": comment["rating"],
                "detail_reviews_rating": [{
                    "score_rating": None,
                    "category_rating": None
                }],
                "total_likes_reviews": None,
                "total_dislikes_reviews": None,
                "total_reply_reviews": None,
                "orders": comment["order"],
                "tags_review": comment["tags"] + [self.DOMAIN],
                "content_reviews": comment["text"],
                "reply_content_reviews": {
                    "username_reply_reviews": None,
                    "content_reviews": None
                },
                "date_of_experience": comment["createdAt"].split('.')[0].replace('T', ' '),
                "date_of_experience_epoch": Time.convert_time(comment["createdAt"]),
            }

            path_data = self.create_dir(raw_data=raw_json, create=self.SAVE_TO_LOKAL)

            raw_json.update({
                "detail_reviews": detail_reviews,
                "path_data_raw": f'S3://ai-pipeline-statistics/{path_data}/{detail_reviews["id_review"]}.json',
                "path_data_clean": f'S3://ai-pipeline-statistics/{Dir.convert_path(path_data)}/{detail_reviews["id_review"]}.json'
            })

            response: int = S3.upload_json(
                destination=path_data,
                body=raw_json,
                send=self.SAVE_TO_S3
            )

            response = 200

            if self.SAVE_TO_LOKAL: 
                File.write_json(path=f'{path_data}/{detail_reviews["id_review"]}.json', content=raw_json)


            self.logs.logging(
                total=len(reviews["all_reviews"]),
                failed=1 if response != 200 else 0,
                success=1 if response == 200 else 0,
                id_product=raw_json["id"],
                id_review=detail_reviews["id_review"],
                status_runtime="success" if response == 200 else "error",
                message="Failed to send to S3" if response != 200 else None,
                sub_source=raw_json["reviews_name"],
                type_error=response if response != 200 else None
            )


        if not reviews["all_reviews"]:
            self.logs.logging(
                total=0,
                failed=0,
                success=0,
                id_product=raw_json["id"],
                id_review=detail_reviews["id_review"],
                status_runtime=None,
                message=None,
                sub_source=raw_json["reviews_name"],
                type_error=None
            )
        ...

    def __extract_restaurant(self, component: Tuple[Dict[str, any]]):
            (restaurant, city) = component

            while True:
                try:
                    cards: List[str] = self.collect_card_restaurant(restaurant=restaurant["path"]) # Mengambil card restaurant dari area

                    for card in cards:

                        """ api_review

                        Param:
                            card | /ketapang/restaurant/pempek-bang-awie-wenang-a906c98d-2d31-48bc-8408-82dc1350cdca
                        
                        """
                        api_review = f'https://gofood.co.id/_next/data/{self.VERSION}/id{card}/reviews.json?id={card.split("/")[-1]}'
                        
                        if self.check_dones(api_review): continue
                        try:
                            food_review = self.api.get(url=api_review, max_retries=30)

                            # Jika di redirect maka ambil destination dan request ke path yang di berikan
                            if food_review.json()["pageProps"].get("__N_REDIRECT", None):
                                food_review = self.api.get(url=f'https://gofood.co.id/_next/data/{self.VERSION}/id{food_review.json()["pageProps"]["__N_REDIRECT"]}/reviews.json?id={card.split("/")[-1]}', max_retries=30)

                            header_required = {
                                "id": crc32(Dekimashita.vdir(food_review.json()["pageProps"]["outlet"]["core"]["displayName"]).encode('utf-8')),
                                "link": self.MAIN_URL+food_review.json()["pageProps"].get("outletUrl"),
                                "domain": self.DOMAIN,
                                "tags": [tag["displayName"] for tag in food_review.json()["pageProps"]["outlet"]["core"]["tags"]] + [self.DOMAIN],
                                "crawling_time": Time.now(),
                                "crawling_time_epoch": int(time()),
                                "path_data_raw": "",
                                "path_data_clean": "",
                                "reviews_name": food_review.json()["pageProps"]["outlet"]["core"]["displayName"],
                                "location_review": city["name"].lower(),
                                "category_reviews": "food & baverage",
                                "total_reviews": 0,

                                "location_restaurant": {
                                    "city": city["name"].lower(),
                                    "area": restaurant["path"].split("/")[-1],
                                    "distance_km": food_review.json()["pageProps"]["outlet"]["delivery"]["distanceKm"],
                                },

                                "range_prices": self.PRICE[str(food_review.json()["pageProps"]["outlet"]["priceLevel"])],
                                "restaurant_id": food_review.json()["pageProps"]["outlet"]["uid"],

                                "reviews_rating": {
                                    "total_ratings": food_review.json()["pageProps"]["outlet"]["ratings"],
                                    "detail_total_rating": [
                                        {
                                            "category_rating": self.RATING[rating["id"]],
                                            "score_rating": rating["count"]
                                        } for rating in food_review.json()["pageProps"]["cannedOutlet"]
                                    ],
                                },
                                "range_prices": self.PRICE[str(food_review.json()["pageProps"]["outlet"]["priceLevel"])],
                                "detail_reviews": ""
                            }

                            self.__get_review(raw_json=header_required)
                            

                        except JSONDecodeError as err:
                            ic({
                                "error": err,
                                "api_review": api_review,
                                "card": card
                            })

                        finally:
                            self.add_dones(api_review)
                            ...
                    
                    break
                except JSONDecodeError as err:
                    ic(err)
                    self.VERSION = input('INSERT NEW VERSION: ')
                    ...
                    

    def __extract_city(self, city: str) -> None:
        response = self.api.get(url=f'https://gofood.co.id/_next/data/{self.VERSION}/id{city["path"]}.json', max_retries=10)        
        for restaurant in response.json()["pageProps"]["contents"][0]["data"]: # Mengambil restaurant dari kota
            self.__extract_restaurant((restaurant, city))


    @Annotations.stopwatch
    def main(self) -> None:

        cities = self.collect_cities(self.API_CITY)
        for city in cities: # Mengambil Kota
            self.__extract_city(city)
        
        ...