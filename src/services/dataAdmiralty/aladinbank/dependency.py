from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import AladinbankComponent

class AladinbankLibs(AladinbankComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True)     
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:

        name: str = html.find('h3').text()
        foto: str = html.find('img').attr('data-src')
        jabatan: str = html.find('div[class="md:ml-3"] > p').text()
        bio: str = '\n'.join(list(map(lambda p: PyQuery(p).text(), html.find('div[class="text-sm mt-8"] > p'))))

        return (name, bio, foto, jabatan)
        ...

    def extract(self, html: PyQuery) -> Dict[str, any]:
        (name, bio, foto, jabatan) = self.extract_bio(html)

        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "link_foto": foto,
            "biografi": bio,
            "riwayat_pekerjaan": None,
            "riwayat_pencapaian": None,
            "dll": None,
            "organisasi": None,
            "riwayat_pendidikan": None,
            "tempat_tanggal_lahir": None,
            }
        ...