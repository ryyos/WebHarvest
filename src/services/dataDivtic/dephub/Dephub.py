
from pyquery import PyQuery
from requests import Response
from typing import List, Dict
from icecream import ic

from .dependency import DephubLibs
from src.utils import Time, Dir, File
from src.server import S3

class Dephub(DephubLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__()
        
        self.__s3: bool = options.get('s3')
        self.__save: bool = options.get('save')
        ...
        
    def header(self, path: str, url: str) -> Dict[str, str]:
        head: dict = {
                "link": url,
                "domain": self.domain,
                "tags": [self.domain],
                "crawling_time": Time.now(),
                "crawling_time_epoch": Time.epoch(),
                "path_data_raw": self.base_path_s3+path,
                "path_data_clean": self.base_path_s3+Dir.convert_path(path),
            }
        
        return head
        ...
    def mapping(self, data: Dict[str, any]) -> Dict[str, any]:
        response: Response = self.api.get(self.row_url+data["IDpel"])
        html: PyQuery = PyQuery(response.text)
        
        path: str = self.build_path(data["IDpel"])
        headers: dict = self.header(path, response.url)
        profile: dict = self.get_profile(html)
        working_area: List[dict] = self.get_working_area(html)
        hirarki_pelabuhan: List[dict] = self.get_hirarki_pelabuhan(html)
        fasilitas_pokok: List[dict] = self.get_fasilitas_pokok(data["IDpel"])
        
        result: dict = {
            **headers,
            **data,
            **profile,
            "working_area": working_area,
            "hirarki_pelabuhan": hirarki_pelabuhan,
            "fasilitas_pokok": fasilitas_pokok
        }
        
        if self.__save:
            File.write_json(path, result)
        
        S3.upload_json(
            destination=path,
            body=result,
            send=self.__s3
        )
        
        ...
        
    def main(self) -> None:
        list_table: List[dict] = self.get_list_table(self.target_url)
        for row in list_table:
            self.mapping(row)
            ...
        ...