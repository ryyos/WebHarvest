
from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import BankganeshaComponent

class BankganeshaLibs(BankganeshaComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True)
        ...

    def extract(self, html: PyQuery) -> Dict[str, any]:

        return {
            "nama_lengkap": html.find('h2[class="title-news"]').text(),
            "nama_jabatan": html.find('div[class="content-text"] p > strong').text(),
            "link_foto": html.find('img').attr('src'),
            "biografi": html.find('div[class="content-text"] p').eq(-1).text(),
            "riwayat_pekerjaan": None,
            "riwayat_pencapaian": None,
            "dll": None,
            "organisasi": None,
            "riwayat_pendidikan": None,
            "tempat_tanggal_lahir": None,
            }
        ...