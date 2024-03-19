import asyncio
import gdown
import tempfile

from ApiRetrys import ApiRetry
from pyquery import PyQuery
from dekimashita import Dekimashita
from icecream import ic
from typing import AsyncGenerator, Dict, List
from src.server import S3

from .component import GeospasialComponent
from src.utils import (Zip, 
                       Time, 
                       Dir, 
                       Funct, 
                       File)

class GeospasialLibs(GeospasialComponent):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__()

        self.__s3: bool = options["s3"]
        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        self.dones = File.read_list_json('src/database/json/geospasial.json')
        ...

    def build_path(self, provinsi: str, extentsion: str=None) -> str:
        if extentsion:
            return f'data/data_raw/Divtik/indonesia-geospasial/{provinsi}/{extentsion}/'
        else:
            return f'data/data_raw/Divtik/indonesia-geospasial/{provinsi}/'
        ...

    async def collect_url(self, html: PyQuery) -> AsyncGenerator[Dict[str, any], any]:
        for tr in html.find('table tbody > tr'):
            yield {
                "provinsi": PyQuery(tr).find('td').eq(1).text(),
                "url": PyQuery(tr).find('td a').attr('href')
            }
            ...
        ...

    async def download(self, url: str, destination: str, password: str = None, rar_path: str = None) -> List[str]:
        temp_dir: str = tempfile.mkdtemp().replace('\\', '/')
        temp_dir = gdown.download(url, temp_dir+'/'+rar_path.split('/')[-1], quiet=False, fuzzy=True, use_cookies=True)

        if rar_path:
            Funct.copy(temp_dir, rar_path)
        
        path_all_media: List[str] = Zip.unzip_items_rar(
            source=temp_dir.replace('\\', '/'),
            destination=destination,
            password=password,
            s3=self.__s3
        )
        
        return path_all_media
        ...

    async def create_metadata(self, path: str, provinsi: str, path_medias: List[str]) -> Dict[str, any]:
        result = {
            "link": self.target_url,
            "provinsi": provinsi,
            "domain": self.domain,
            "tags": [self.domain],
            "crawling_time": Time.now(),
            "crawling_time_epoch": Time.epoch(),
            "path_data_raw": self.base_path_s3+path,
            "path_data_clean": self.base_path_s3+Dir.convert_path(path),
            "path_all_media": [self.base_path_s3+path for path in path_medias]
        }

        return result
        ...

    async def process_data(self, row: Dict[str, str]) -> None:
        path_rar: str = self.build_path(row["provinsi"], 'rar')+Dekimashita.vdir(row["provinsi"])+'.rar'
        path_main: str = self.build_path(row["provinsi"], 'json')+Dekimashita.vdir(row["provinsi"])+'.json'

        all_path_media: List[str] = await self.download(
            url=row["url"], 
            destination=self.build_path(row["provinsi"]),
            password=self.password_rar,
            rar_path=path_rar)
        
        result: dict = await self.create_metadata(path=path_main, provinsi=row["provinsi"], path_medias=all_path_media)
        File.write_json(path_main, result)
        S3.upload_json(
            destination=path_main,
            body=result,
            send=self.__s3
        )
        
        ...