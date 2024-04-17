import requests

from requests import Response
from pyquery import PyQuery
from icecream import ic
from typing import List, Dict, Tuple

from .dependency import ArthagrahaLibs
from src.utils import *
from src.server import S3

class Arthagraha(ArthagrahaLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__()
        self.__s3: bool = options.get('s3')
        self.__save: bool = options.get('save')
        ...

    def chef(self, datas: Tuple[List[Dict[str, any]]]) -> None:

        for type, data, url in zip(self.type, datas, self.target_url):
            path: str = self.base_path+type+'_arthagraha.json'
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
            response: Response = self.api.get(target, verify=False)
            html = PyQuery(response.text)

            if index == 0: results_direksi.extend(self.extract(html))
            else: results_komisaris.extend(self.extract(html))

            ...
        self.chef((results_direksi, results_komisaris))
        ...