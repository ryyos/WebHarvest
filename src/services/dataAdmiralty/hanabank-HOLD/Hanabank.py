
from typing import List, Dict, Tuple
from requests import Response
from pyquery import PyQuery
from icecream import ic

from .dependency import HanabankLibs
from src.utils import *
from src.server import S3

class Hanabank(HanabankLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__()

        self.__s3: bool = options.get('s3')
        self.__save: bool = options.get('save')
        ...

    def chef(self, datas: Tuple[List[Dict[str, any]]]) -> None:

        for type, data, url in zip(self.type, datas, self.target_url):
            path: str = self.base_path+type+'_kbbukopinsyariah.json'
            result = {
                "link": url,
                "type": type,
                "domain": self.domain,
                "tags": [self.domain],
                "crawling_time": Time.now(),
                "crawling_time_epoch": Time.epoch(),
                "path_data_raw": self.base_path_s3+path,
                "path_data_clean": self.base_path_s3+Dir.convert_path(path),
                "datas": data
            }

            if self.__save:
                File.write_json(path, result)

            if self.__s3:
                S3.upload_json(
                destination=path,
                body=result,
                send=self.__s3
            )

    def main(self) -> None:
        response: Response = self.api.get(self.target_url)
        html = PyQuery(response.text)

        results_direksi: List[dict] = []
        results_komisaris: List[dict] = []

        divs: PyQuery = html.find('div[class="max-w-screen-xl mx-auto px-16 md:px-40 xl:px-32 2xl:px-0 mb-40 md:mb-96 overflow-hidden"] > div > div')
        
        self.extract(divs.eq(1))

        # self.chef((results_direksi, results_komisaris))
        ...