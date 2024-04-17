
from ApiRetrys import ApiRetry
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import MegasyariahComponent

class MegasyariahLibs(MegasyariahComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:

        foto: str = html.find('img').attr('src')
        name: str = html.find('h5').eq(0).text()
        jabatan: str = html.find('h5').eq(-1).text()
        bio: str = html.find('p').eq(0).text()
        pekerjaan: str = '\n'.join([PyQuery(p).text() for p in html.find('p')[1:]])
        ...

        return (foto, name, jabatan, bio, pekerjaan)

    def extract(self, html: PyQuery) -> None:
        (foto, name, jabatan, bio, pekerjaan) = self.extract_bio(html)
        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "riwayat_pekerjaan": pekerjaan if pekerjaan else None,
            "link_foto": self.base_url+foto,
            "biografi": bio,
            "riwayat_pendidikan": None,
            "riwayat_pencapaian": None,
            "dll": None,
            "organisasi": None,
            "tempat_tanggal_lahir": None,
            }
        ...