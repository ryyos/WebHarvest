
from typing import List, Dict, Tuple
from requests import Response
from pyquery import PyQuery
from icecream import ic

from .dependency import BankindexLibs
from src.utils import *
from src.server import S3

class Bankindex(BankindexLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__()

        self.__s3: bool = options.get('s3')
        self.__save: bool = options.get('save')
        ...

    def chef(self, datas: Tuple[List[Dict[str, any]]]) -> None:

        for type, data in zip(self.type, datas):
            path: str = self.base_path+type+'_bankindex.json'
            result = {
                "link": self.target_url,
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
        response: Response = self.api.get(self.target_url, verify=False)
        html = PyQuery(response.text)

        results_direksi: List[dict] = []
        results_komisaris: List[dict] = []

        (all_direksi, all_komisaris) = self.sorter(html)

        for direksi in all_direksi[1:]:
            results_direksi.append(self.extract(PyQuery(direksi)))
            ...

        for komisaris in all_komisaris[1:]:
            results_komisaris.append(self.extract(PyQuery(komisaris)))
            ...

        self.chef((results_direksi, results_komisaris))
        ...