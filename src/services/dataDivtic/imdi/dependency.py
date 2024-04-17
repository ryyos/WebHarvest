from ApiRetrys import ApiRetry
from requests import Response
from typing import Tuple, List, AsyncGenerator, Dict
from icecream import ic
from dekimashita import Dekimashita
from .component import ImdiComponent
from src.utils import Time, Dir, File
from src.server import S3

class ImdiLibs(ImdiComponent):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__()

        self.__save: bool = options.get('save')
        self.__s3: bool = options.get('s3')
        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        
        ...

    async def collect_provinsi(self, url: str, param: dict) -> AsyncGenerator[Dict[str, str], any]:
        response: Response = self.api.get(url, params=param)

        for index, data in enumerate(response.json()):
            yield {
                "provinsi": data["provinsi"],
                "code": index+1
            }
        ...

    async def meta_data(self, url: str, path: str, datas: List[dict], provinsi: str) -> str:
        result = {
            "link": url,
            "provinsi": provinsi,
            "domain": self.domain,
            "tags": [self.domain],
            "crawling_time": Time.now(),
            "crawling_time_epoch": Time.epoch(),
            "path_data_raw": self.base_path_s3+path,
            "path_data_clean": self.base_path_s3+Dir.convert_path(path),
            "datas": datas
        }

        return result
        ...

    def build_path(self, provinsi: str) -> str:
        return f'data/data_raw/Divtik/imdi/{provinsi}/json/{Dekimashita.vdir(provinsi)}.json'
        ...

    async def extract(self, url: str, param: dict, provinsi: str) -> List[Dict[str, any]]:
        response: Response = self.api.get(url, params=param)
        datas: List[dict] = []
        for data in response.json():
            datas.append({
                "kota": data["kota"],
                "infrastruktur_ekosistem_1": float(data["infrastruktur_ekosistem_1"])
            })
            ...
        
        path_data: str = self.build_path(provinsi)
        result: dict = await self.meta_data(
            url=response.url,
            datas=datas,
            path=path_data,
            provinsi=provinsi
        )

        if self.__save:
            File.write_json(path_data, result)
        
        S3.upload_json(
            destination=path_data,
            body=result,
            send=self.__s3
        )
        ...