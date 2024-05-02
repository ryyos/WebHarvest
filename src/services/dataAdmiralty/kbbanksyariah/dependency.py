
from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import KbbanksyariahComponent

class KbbanksyariahLibs(KbbanksyariahComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:

        foto: str = html.find('img').attr('src')
        name: str = html.find('h3').text()
        jabatan: str = html.find('h4').text()
        pendidikan: List[str] = '\n'.join(list(map(lambda x: PyQuery(x).text(), html.find('ul > li'))))
        pekerjaan: str = html.find('ul + p + p').text()
        bio: str = html.find('p').eq(0).text()
        ...

        return (name, jabatan, foto, pendidikan, pekerjaan, bio)

    def extract(self, html: PyQuery) -> Dict[str, any]:
        (name, jabatan, foto, pendidikan, pekerjaan, bio) = self.extract_bio(html)
        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "link_foto": foto,
            "biografi": bio,
            "riwayat_pekerjaan": pekerjaan,
            "dll": None,
            "organisasi": None,
            "riwayat_pendidikan": pendidikan,
            "riwayat_pencapaian": None,
            "tempat_tanggal_lahir": None,
            }
        ...