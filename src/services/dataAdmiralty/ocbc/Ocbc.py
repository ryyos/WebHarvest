
from typing import List, Dict, Tuple
from requests import Response
from pyquery import PyQuery
from icecream import ic

from .dependency import OcbcLibs
from src.utils import *
from src.server import S3

class Ocbc(OcbcLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__()

        self.__s3: bool = options.get('s3')
        self.__save: bool = options.get('save')
        ...

    def chef(self, datas: Tuple[List[Dict[str, any]]]) -> None:

        for type, data in zip(self.type, datas):
            path: str = self.base_path+type+'_ocbc.json'
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
        response: Response = self.api.get(self.target_url)
        html = PyQuery(response.text)
        done: bool

        all_direksi: PyQuery = html.find('div[data-pane="290FA664DCFB43859D5E2E41CA60C7EF"]')
        all_komisaris: PyQuery = html.find('div[data-pane="564E38D2C575449D9CB08154E26355A4"]')

        results_direksi: List[dict] = []
        results_komisaris: List[dict] = []

        for direksi in all_direksi.find('div[class="ocbc-row"] > div > div'):
            results_direksi.append(self.extract(PyQuery(PyQuery(direksi).attr('data-popup-body')), name=PyQuery(direksi).find('h4').text(), jabatan=PyQuery(direksi).find('p').text(), img=PyQuery(direksi).find('img').attr('src')))
            ...

        for komisaris in all_komisaris.find('div[class="ocbc-row"] > div > div'):
            results_komisaris.append(self.extract(PyQuery(PyQuery(komisaris).attr('data-popup-body')), name=PyQuery(komisaris).find('h4').text(), jabatan=PyQuery(komisaris).find('p').text(), img=PyQuery(komisaris).find('img').attr('src')))
            ...

        self.chef((results_direksi, results_komisaris))
        ...