from requests import Response
from icecream import ic
from typing import Dict, List, Generator
from pyquery import PyQuery
from dekimashita import Dekimashita

from .dependency import AhugoidLibs
from src.utils import File, Dir, Time, Stream
from src.server import S3


class Ahugoid(AhugoidLibs):
    def __init__(self, options: Dict[str, any]) -> None:
        super().__init__()
        
        self.__recaptcha: str = options.get('recaptcha')
        self.__keyword: str = options.get('keyword')
        
        self.__save: bool = options.get('save')
        self.__s3: bool = options.get('s3')
        ...
        
    def head(self, **kwargs) -> Dict[str, any]:
        return {
            "link": kwargs.get('url'),
            "keyword": self.__keyword,
            "domain": self.domain,
            "tags": [self.domain],
            "crawling_time": Time.now(),
            "crawling_time_epoch": Time.epoch(),
            "path_data_raw": self.base_path_s3+kwargs.get('path'),
            "path_data_clean": self.base_path_s3+Dir.convert_path(kwargs.get('path')),
        }
        ...
        
    def mapping(self, response: Response) -> Generator[Dict[str, any], any, None]:
        html: PyQuery = PyQuery(response.text)
        cards: List[PyQuery] = html.find('#hasil_cari div.cl0, #hasil_cari div.cl1')
        if not cards: raise Exception('clear')
        
        for card in cards:
            card: PyQuery = PyQuery(card)
            
            extract_card: dict = self.extract(card)
            path = f'data/data_raw/ahugoid/{Dekimashita.vdir(self.__keyword)}/json/{Dekimashita.vdir(extract_card["name"])}.json'
            
            head: dict = self.head(path=path, url=response.url)
            result: dict = {
                **head,
                **extract_card
            }
            
            Stream.one("PT", "FOUND", extract_card["name"])
            
            yield result
        ...
        
    def main(self) -> None:
        
        page: int = 1
        while True:
            try:
                response: Response = self.api.get(self.base_url, params=self.build_param(
                    page=page,
                    keyword=self.__keyword,
                    recaptcha=self.__recaptcha
                ))
                for result in self.mapping(response):    
                    if self.__save:
                        File.write_json(result["path_data_raw"].replace(self.base_path_s3, ''), result)

                    S3.upload_json(
                        destination=result["path_data_raw"].replace(self.base_path_s3, ''),
                        body=result,
                        send=self.__s3
                    )
                page+=1
            except Exception:
                Stream.one("STOP", "STOP IN PAGE", page)
                break
        ...