
from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import BankmasComponent

class BankmasLibs(BankmasComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:

        foto: str = self.base_url+html.find('img').attr('src')
        name: str = html.find('div.text-primary-black-dark > span').eq(0).text()
        jabatan: str = html.find('div.text-primary-black-dark > span').eq(-1).text()
        bio: str = html.find('p').text()
        ...

        return (foto, name, jabatan, bio)

    def extract(self, html: PyQuery) -> Dict[str, any]:
        (foto, name, jabatan, bio) = self.extract_bio(html)
        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "link_foto": foto,
            "biografi": bio,
            "riwayat_pekerjaan": None,
            "dll": None,
            "organisasi": None,
            "riwayat_pendidikan": None,
            "riwayat_pencapaian": None,
            "tempat_tanggal_lahir": None,
            }
        ...