
from icecream import ic
from requests import Response
from pyquery import PyQuery
from typing import Dict, Tuple, List

from .dependency import MayBankLibs

from src.utils import *
from src.server import S3


class MayBank(MayBankLibs):
    def __init__(self, options: Dict[str, any]) -> None:
        super().__init__()
        
        self.__s3: bool = options.get('s3')
        self.__save: bool = options.get('save')
        ...

    def chef(self, datas: Tuple[List[Dict[str, any]]]) -> None:

        for type, data, url in zippy(self.type, datas, self.target_url):
            path: str = self.base_path+type+'_mayBank.json'
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

            S3.upload_json(
                destination=path,
                body=result,
                send=self.__s3
            )

    def main(self) -> None:

        results_direksi: List[dict] = []
        results_komisaris: List[dict] = []

        for index, target in enumerate(self.target_url):
            response: Response = self.api.get(target)
            html = PyQuery(response.text)

            for url in html.find('div[class="section"] div.container a'):
                result = self.extract(self.base_url+PyQuery(url).attr('href'), target)

                if index == 0: results_direksi.append(result)
                else: results_komisaris.append(result)

        self.chef((results_direksi, results_komisaris))
        ...