
from ApiRetrys import ApiRetry
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import BankindexComponent

class BankindexLibs(BankindexComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def sorter(self, html: PyQuery) -> Tuple[List[PyQuery], any, None]:
        h1 = False

        all_direksi: List[PyQuery] = []
        all_komisaris: List[PyQuery] = []

        childrens: List[PyQuery] = html.find('div[class="col-md-9 page-content"] > div[class="row"] > div').eq(-1).children()
        for child in childrens:
            if PyQuery(child).is_('h1'): h1 = not h1
            if h1: all_komisaris.append(child)
            else: all_direksi.append(child)
            ...

        return (all_direksi, all_komisaris)
        ...
    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:

        foto: str = html.find('img').attr('src')
        name: str = html.find('h2').text()
        jabatan: str = html.find('h3').text()
        bio: str = html.find('div.management-detail').text().replace('\n', '')

        return (foto, name, jabatan, bio)
        ...

    def extract(self, html: PyQuery) -> None:
        (foto, name, jabatan, bio) = self.extract_bio(html)
        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "riwayat_pendidikan": None,
            "link_foto": self.base_url+foto,
            "biografi": bio,
            "riwayat_pekerjaan": None,
            "riwayat_pencapaian": None,
            "dll": None,
            "organisasi": None,
            "tempat_tanggal_lahir": None,
            }
        ...