
from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import JagoComponent

class JagoLibs(JagoComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True)
        ...

    def extract_bio(self, html: PyQuery, raw: PyQuery) -> Tuple[str, any, None]:
        
        foto: str = html.find('img').attr('src')
        name: str = html.find('h2').text()
        jabatan: str = raw.find('p.text-grey').text()
        bio: str = html.find('p').text()
        ...

        return (name, jabatan, foto, bio)

    def extract(self, html: PyQuery) -> Dict[str, any]:
        
        response: Response = self.api.get(self.profile_url+html.attr('data-name'), cookies=self.cookies, headers=self.headers)
        response_html: PyQuery = PyQuery(response.text)
        
        (name, jabatan, foto, bio) = self.extract_bio(response_html, html)
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