from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic
from time import sleep

from .component import BankmandiritaspenComponent

class BankmandiritaspenLibs(BankmandiritaspenComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:
        
        name: str = html.find('h3').text()
        jabatan: str = html.find('p.ttle').text()
        foto: str = html.find('img').attr('src')
        pendidikan: str | None = None
        pekerjaan: str | None = None
        organisasi: str | None = None
        dll: str | None = None
        
        divs: List[PyQuery] = html.find('div.bio-cnt > div')
        
        for div in divs:
            div: PyQuery = PyQuery(div)
            if 'Pendidikan' in div.find('div.on p').text():
                pendidikan = div.find('div.tu').text()
                
            if 'Pengalaman Kerja' in div.find('div.on p').text():
                pekerjaan = div.find('div.tu').text()
                
            if 'Hubungan Afiliasi' in div.find('div.on p').text():
                organisasi = div.find('div.tu').text()
                
            if 'Dasar Hukum Penunjukan' in div.find('div.on p').text():
                dll = div.find('div.tu').text()
                

        return (name, jabatan, foto, pendidikan, pekerjaan, organisasi, dll)
        ...

    def extract(self, html: PyQuery) -> Dict[str, any]:
        (name, jabatan, foto, pendidikan, pekerjaan, organisasi, dll) = self.extract_bio(html)
        
        result = {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "link_foto": foto,
            "biografi": None,
            "riwayat_pencapaian": None,
            "riwayat_pekerjaan":pekerjaan,
            "organisasi":organisasi,
            "dll":dll,
            "riwayat_pendidikan": pendidikan,
            "tempat_tanggal_lahir": None,
        }

        return result
        ...