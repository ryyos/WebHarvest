from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic
from time import sleep

from .component import BankcapitalComponent

class BankcapitalLibs(BankcapitalComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract(self, html: PyQuery) -> Dict[str, any]:
        childrens: List[PyQuery] = html.find('div[class="content"]').children()

        results: List[dict] = []

        for index, child in enumerate(childrens):

            if PyQuery(child).is_('h3'):
                result = {
                    "nama_lengkap": PyQuery(childrens[index-1]).text().split('-')[0].strip(),
                    "nama_jabatan": PyQuery(childrens[index-1]).text().split('-')[-1].strip(),
                    "link_foto": PyQuery(childrens[index-1]).find('img').attr('src'),
                    "biografi": PyQuery(child).text(),
                    "riwayat_pencapaian": None,
                    "riwayat_pekerjaan":None,
                    "organisasi":None,
                    "dll":None,
                    "riwayat_pendidikan": None,
                    "tempat_tanggal_lahir": None,
                }
                results.append(result)

        return results
        ...