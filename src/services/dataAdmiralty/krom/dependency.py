from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic
from time import sleep

from .component import KromComponent

class KromLibs(KromComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:
        
        name: str = html.find('.name-board').text()
        jabatan: str = html.find('.title-boar').eq(0).text()
        foto: str = self.base_url+html.find('img').attr('src')
        bio: str = html.find('.content-board-popup').text()

        return (name, jabatan, foto, bio)
        ...

    def extract(self, html: PyQuery) -> Dict[str, any]:
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