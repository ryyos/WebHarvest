
from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import OkbankComponent

class OkbankLibs(OkbankComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True)
        ...

    def extract_bio(self, data: Dict[str, any]) -> Tuple[str, any, None]:

        name: str = data["name"]
        jabatan: str = data["position"]
        bio: List[str] = '\n'.join(list(map(lambda x: PyQuery(x).text(), PyQuery(data["content"]).find('li'))))
        ...

        return (name, jabatan, bio)

    def extract(self, data: Dict[str, any]) -> Dict[str, any]:
        (name, jabatan, bio) = self.extract_bio(data)
        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "link_foto": None,
            "biografi": bio,
            "riwayat_pekerjaan": None,
            "dll": None,
            "organisasi": None,
            "riwayat_pendidikan": None,
            "riwayat_pencapaian": None,
            "tempat_tanggal_lahir": None,
            }
        ...