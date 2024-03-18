import os

from dotenv import load_dotenv

class GofoodComponent:
    def __init__(self) -> None:
        load_dotenv()

        self.VERSION = '11.2.0'

        # Service

        self.DOMAIN = 'gofood.co.id'
        self.MAIN_URL = 'https://gofood.co.id'

        self.API_CITY = f'https://gofood.co.id/_next/data/{self.VERSION}/id/cities.json' # 89
        self.RESTAURANT = f'https://gofood.co.id/_next/data/{self.VERSION}/id/jakarta/restaurants.json' # 94
        self.NEAR_ME_API = f'https://gofood.co.id/_next/data/{self.VERSION}/id/jakarta/bekasi-restaurants/near_me.json' 
        self.FOODS_API = f'https://gofood.co.id/api/outlets'
        self.API_REVIEW = f'https://gofood.co.id/_next/data/{self.VERSION}/id/jakarta/restaurant/mcdonald-s-pekayon-50150204-8f6d-4372-8458-668f1be126e8/reviews.json?id=mcdonald-s-pekayon-50150204-8f6d-4372-8458-668f1be126e8'
        self.API_REVIEW_PAGE = 'https://gofood.co.id/api/outlets/'

        self.PRICE = {
            '0': 'Not Set',
            '1': '<16k',
            '2': '16k-40k',
            '3': '40k-100k',
            '4': '>100k',
        }

        self.RATING = {
            "CANNED_RESPONSE_TASTE": "taste",
            "CANNED_RESPONSE_PORTION": "portion",
            "CANNED_RESPONSE_PACKAGING": "packaging",
            "CANNED_RESPONSE_FRESHNESS": "freshness",
            "CANNED_RESPONSE_VALUE": "prices",
            "CANNED_RESPONSE_HYGIENE": "hygiene",
        }



        # Library
        self.bucket = os.getenv('BUCKET')
        self.FOODS_API = f'https://gofood.co.id/api/outlets'
        self.API_REVIEW_PAGE = 'https://gofood.co.id/api/outlets/'
        ...