from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic
from time import sleep

from .component import CtbcbankComponent

class CtbcbankLibs(CtbcbankComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract_bio(self, html: PyQuery) -> List[str]:
        
        name: str = html.find('h2.name').text()
        jabatan: str = html.find('p.role').text()
        foto: str = html.find('img').attr('src')
        bio: str = '\n'.join(list(map(lambda p: PyQuery(p).text(), html.find('p:not(.role):not(.bio)'))))
        pekerjaan: str = None
        return (name, jabatan, foto, bio, pekerjaan)
        ...

    def extract(self, html: PyQuery) -> List[Dict[str, any]]:
        (name, jabatan, foto, bio, pekerjaan) = self.extract_bio(html)

        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "link_foto": foto,
            "biografi": bio,
            "riwayat_pencapaian": None,
            "riwayat_pekerjaan": pekerjaan,
            "organisasi": None,
            "dll": None,
            "riwayat_pendidikan": None,
            "tempat_tanggal_lahir": None,
        }
        ...