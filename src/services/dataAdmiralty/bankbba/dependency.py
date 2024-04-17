
from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import BankbbaComponent

class BankbbaLibs(BankbbaComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True)
        ...

    def extract_table(self, html: PyQuery) -> str:

        table: PyQuery = html.find('table')
        pekerjaan: List[str] = []

        for tr in table.find('tr')[1:]:
            pekerjaan.append(
                Dekimashita.vdict(PyQuery(tr).find('td').eq(0).text()+': '+
                PyQuery(tr).find('td').eq(-1).text(), '\n')
            )
            ...

        return '\n'.join(pekerjaan)
        ...

    def extract(self, url: str) -> Dict[str, any]:
        response: Response = self.api.get(url)
        html = PyQuery(response.text)

        content: PyQuery = html.find('div[class="content-manajemen"]')

        return {
            "nama_lengkap": content.find('h3').text(),
            "nama_jabatan": content.find('p').eq(0).text(),
            "link_foto": content.find('img').eq(0).attr('src'),
            "biografi": content.find('p').eq(1).text(),
            "riwayat_pekerjaan": self.extract_table(content),
            "riwayat_pencapaian": None,
            "dll": None,
            "organisasi": None,
            "riwayat_pendidikan": None,
            "tempat_tanggal_lahir": None,
            }
        ...