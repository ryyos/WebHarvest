
from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import AmarbankComponent

class AmarbankLibs(AmarbankComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:


        foto: str = html.find('img').attr('src')
        name: str = html.find('h2').text()
        jabatan: str = html.find('h5').text()
        bio: List[str] = html.find('p').text()
        ...

        return (name, jabatan, bio, foto)

    def extract(self, html: PyQuery) -> Dict[str, any]:
        (name, jabatan, bio, foto) = self.extract_bio(html)
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