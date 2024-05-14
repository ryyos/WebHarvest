
from loguru import logger
from requests import Response
from pyquery import PyQuery
from typing import List, Dict, Tuple
from dekimashita import Dekimashita

from src.utils import File, Time, Dir, Endecode
from src.server import S3
from .dependency import BpsPublikasiLibs

class BpsPublikasi(BpsPublikasiLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__()
        
        self.__s3: bool = options.get('s3')
        self.__save: bool = options.get('save')
        
    def metadata(self, **kwargs) -> Dict[str, any]:
        result = {
            "id": Endecode.md5_hash(kwargs["url"]),
            "provinsi": kwargs["prov"],
            "link": kwargs["url"],
            "domain": kwargs["domain"],
            "tags": [kwargs["domain"]],
            "crawling_time": Time.now(),
            "crawling_time_epoch": Time.epoch(),
            "path_data_raw": self.base_path_s3+kwargs["path_json"],
            "path_data_clean": self.base_path_s3+Dir.convert_path(kwargs["path_json"]),
            "path_document": self.base_path_s3+kwargs["path_doc"]
        }
        
        return result
        ...
        
    def main(self) -> None:
        
        for prov, target in zip(self.targets_prov, self.targets):
            try:
                response: Response = self.api.get(target)
                html: PyQuery = PyQuery(response.text)
                
                text_metadata: dict = self.extract_text(html)
                
                path_json: str = f'data/data_raw/BPS/publikasi/{prov}/json/{Dekimashita.vdir(text_metadata["title"])}.json'
                path_document: str = f'data/data_raw/BPS/publikasi/{prov}/pdf/{Dekimashita.vdir(text_metadata["title"])}.pdf'
                
                metadata: dict = self.metadata(
                    url=target,
                    path_json=path_json,
                    path_doc=path_document,
                    domain=self.get_domain(target),
                    prov=prov
                )
                
                result: dict = {
                    **text_metadata,
                    **metadata
                }
                
                response_doc: Response = self.api.get(result["url_document"])
                
                logger.info(f'{prov} :: DOCUMENT [ {result["title"]} ] DONE')
                
                if self.__save:
                    File.write_json(path_json, result)
                    File.write_byte(path_document, response_doc.content)
                    
                S3.upload_json(destination=path_json, body=result, send=self.__s3)
                S3.upload(destination=path_document, body=response_doc.content, send=self.__s3)
                
            except Exception as e:
                self.error.append({
                    "message": str(e),
                    "target": target,
                    "prov": prov
                })
                File.write_json(self.path_err, self.error)
                
            finally:
                self.dones.append(target)
                File.write_json(self.path_done, self.dones)
            ...
        ...