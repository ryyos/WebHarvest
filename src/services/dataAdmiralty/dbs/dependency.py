from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic
from time import sleep

from .component import DbsComponent

class DbsLibs(DbsComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:
        
        name: str = html.find('div[class="bod-title"] > h2').text()
        jabatan: str = html.find('div[class="bod-title"] > p').eq(0).text()
        foto: str = self.base_url+html.find('div.bodImageWithText img').attr('src')
        bio: str = html.find('div[class="rich-text-box"] > div > p').text()

        return (name, jabatan, foto, bio)
        ...

    def extract(self, url: str) -> Dict[str, any]:
        response: Response = self.api.get(url)
        html: PyQuery = PyQuery(response.text)

        (name, jabatan, foto, bio) = self.extract_bio(html)
        
        result = {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "link_foto": foto,
            "biografi": bio,
            "riwayat_pencapaian": None,
            "riwayat_pekerjaan":None,
            "organisasi":None,
            "dll":None,
            "riwayat_pendidikan": None,
            "tempat_tanggal_lahir": None,
        }

        return result
        ...