from loguru import logger
from .dependency import SipsnLibs
from typing import Dict, List
from requests import Response
from icecream import ic
from dekimashita import Dekimashita

from src.utils import File, Time, Dir
from src.server import S3

class Sipsn(SipsnLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__()
        
        self.__s3: bool = options.get('s3')
        self.__save: bool = options.get('save')
        
    def metadata(self, **kwargs) -> Dict[str, any]:
        result = {
            "id": kwargs["id"],
            "link": self.home_url,
            "provinsi": kwargs["prov"],
            "domain": self.domain,
            "tags": [self.domain],
            "crawling_time": Time.now(),
            "crawling_time_epoch": Time.epoch(),
            "path_data_raw": self.base_path_s3+kwargs["path_json"],
            "path_data_clean": self.base_path_s3+Dir.convert_path(kwargs["path_json"]),
            "path_document": self.base_path_s3+kwargs["path_doc"]
        }
        
        return result
        ...
        
    def main(self) -> None:
        
        for id, prov in self.generate_prov(self.home_url):
            payloads: dict = self.update_payload(id)
            response: Response = self.api.post(self.main_api, headers=self.headers, data=payloads)
            
            raw_data: List[dict] = self.mappings(response.json())
            xlsx_byte: bytes = self.convert_xlsx(raw_data)
            
            logger.info(f'EXTRACT PROVINSI [ {prov} ]')
            
            path_json: str = f'data/data_raw/Divtik/menlhk/Fasilitas_Tempat_Pembuangan_Akhir/json/{Dekimashita.vdir(prov)}.json'
            path_doc: str = f'data/data_raw/Divtik/menlhk/Fasilitas_Tempat_Pembuangan_Akhir/xlsx/{Dekimashita.vdir(prov)}.xlsx'
            
            result: dict = self.metadata(
                id=id,
                prov=prov,
                path_json=path_json,
                path_doc=path_doc,
            )
            
            if self.__save:
                File.write_json(path_json, result)
                File.write_byte(path_doc, xlsx_byte)
                
            S3.upload_json(destination=path_json, body=result, send=self.__s3)
            S3.upload(destination=path_doc, body=xlsx_byte, send=self.__s3)
        ...