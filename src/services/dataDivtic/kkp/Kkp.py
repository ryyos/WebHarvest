
from requests import Response
from pyquery import PyQuery
from html2excel import ExcelParser

from typing import Dict, List, Tuple, Generator
from src.utils import File, Dir, Time, Endecode
from src.server import S3
from .dependency import KkpLibs

class Kkp(KkpLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__()
        
        self.__s3: bool = options.get('s3')
        self.__save: bool = options.get('save')
        
    def metadata(self, **kwargs) -> Dict[str, any]:
        result = {
            "id": kwargs["id"],
            "link": kwargs["link"],
            "domain": kwargs["domain"],
            "tags": [kwargs["domain"]],
            "crawling_time": Time.now(),
            "crawling_time_epoch": Time.epoch(),
            "path_data_raw": self.base_path_s3+kwargs["path_json"],
            "path_data_clean": self.base_path_s3+Dir.convert_path(kwargs["path_json"]),
        }
        
        return result
        ...
    def statistik(self) -> Generator[Dict[str, any], any, None]:
        response: Response = self.api.get(self.statistic_url)
        html: PyQuery = PyQuery(response.text)
        
        for category, url in self.collect_categories(html):
            response: Response = self.api.get(url)
            html: PyQuery = PyQuery(response.text)
            
            sub_categories: List[tuple] = self.collect_sub_categories(html)
            if sub_categories:
                _api: str = self.get_endpoint(html)
                for sub, id in sub_categories:
                    if not id: continue
                    response: Response = self.api.post(_api, data={"no_kpda": id}, headers=self.header)
                    data_table: str = '<table>'+response.json()[0]+'</table>'
                    yield (url, category.replace('/', '_'), sub.replace('/', '_'), data_table)

            if 'JTB/Potensi/SDI WPP' in category:
                for sub, data_table in self.get_jtb_potensi(html):
                    yield (url, category.replace('/', '_'), sub.replace('/', '_'), '<table>'+data_table+'</table>')
                """
                * TODO hapus / dan ganti _
                """
                    
            elif 'Angka Konsumsi Ikan' in category:
                for sub, data_table in self.get_angka_konsumsi_ikan():
                    yield (url, category, sub, '<table>'+data_table+'</table>')
                
            elif 'IKU KKP' in category:
                for sub, data_table in self.get_iku_kkp(html):
                    yield (url, category, sub, '<table>'+data_table+'</table>')
                    
            elif 'Unit Pengolahan Ikan' in category:
                for sub, data_table in self.get_unit_pengolahan_ikan(html):
                    yield (url, category, sub, '<table>'+data_table+'</table>')
            
            elif 'Jadwal Rilis' in category:
                for sub, data_table in self.get_jadwal_rilis(html):
                    yield (url, category, sub, '<table>'+data_table+'</table>')
            
            elif 'Publikasi' in category:
                for sub, data in self.get_publikasi(html):
                    yield (url, category, sub, data)
            
            elif 'Deskripsi' in category:
                for sub, data in self.get_deskripsi(html):
                    yield (url, category, sub, data)
        ...
        
    def main(self) -> None:
        response: Response = self.api.get(self.home_url)
        html: PyQuery = PyQuery(response.text)
        
        nilai_tukar: dict = self.get_nilai_tukar(html)
        pdb: dict = self.get_pdb(html)
        aki: dict = self.get_aki(html)
        ekspor: dict = self.get_ekspor(html)
        
        for data in [nilai_tukar, pdb, aki, ekspor]:
            path_json: str = f'data/data_raw/data statistic/satu data Kementrian Kelautan dan Perikanan/{data["category"]}/{data["label"]}/json/{data["label"]}.json'
            metadata = self.metadata(
                id=Endecode.md5_hash(data["label"]),
                path_json=path_json,
                link=self.home_url,
                domain='satudata.kkp.go.id'
            )
            metadata.update({
                **data,
            })
            
            S3.upload_json(
                body=metadata,
                destination=path_json,
                send=self.__s3
            )
            
            File.write_json(
                path_json,
                metadata
            )
        
        for url, category, sub, data in self.statistik():
            
            path_json: str = f'data/data_raw/data statistic/satu data Kementrian Kelautan dan Perikanan/{category}/{sub}/json/{sub}.json'
            path_xlsx: str = Dir.create_dir(f'data/data_raw/data statistic/satu data Kementrian Kelautan dan Perikanan/{category}/{sub}/xlsx/')+f'{sub}.xlsx'
            
            metadata = self.metadata(
                id=Endecode.md5_hash(sub),
                path_json=path_json,
                link=url,
                domain='statistik.kkp.go.id'
            )
            
            if isinstance(data, list): 
                metadata.update({
                    "data": data,
                    "sub_category": sub
                })
                
                if data[0].get("link"):
                    for d in data:
                        path_pdf: str = f'data/data_raw/data statistic/satu data Kementrian Kelautan dan Perikanan/{category}/{sub}/pdf/{d["judul"]}.pdf'
                        response = self.api.get(d["link"])
                        File.write_byte(path_pdf, response.content)
                        d["path_document"] = self.base_path_s3+path_pdf
                        S3.upload(
                            body=response.content,
                            destination=path_pdf,
                            send=self.__s3
                        )
                    
            
            else:
                metadata.update({
                    "path_document": self.base_path_s3+path_xlsx,
                    "sub_category": sub
                })
                
                temp_path: str = 'src/services/dataDivtic/kkp/process.html'
                File.write_str(temp_path, data)
                convert = ExcelParser(temp_path)
                convert.to_excel(path_xlsx)
                
                S3.upload(
                    body=File.read_byte(path_xlsx),
                    destination=path_xlsx,
                    send=self.__s3
                )
            
            S3.upload_json(
                body=metadata,
                destination=path_json,
                send=self.__s3
            )
            
            File.write_json(
                path_json,
                metadata
            )
            ...
        ...