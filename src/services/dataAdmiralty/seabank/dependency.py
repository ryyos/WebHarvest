
from ApiRetrys import ApiRetry
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import SeabankComponent
from src.utils import search_key
class SeabankLibs(SeabankComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract_bio(self, data: Dict[str, any]) -> Tuple[str, any, None]:

        foto: str = data["avatar"]
        name: str = data["name"]["textEn"]
        jabatan: str = search_key(data["title"], 'textEn')
        bio: str = search_key(data["desc"], 'textEn')
        ...

        return (foto, name, jabatan, bio)

    def extract(self, data: Dict[str, any]) -> None:
        (foto, name, jabatan, bio) = self.extract_bio(data)
        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "riwayat_pendidikan": None,
            "riwayat_pekerjaan": None,
            "link_foto": foto,
            "biografi": bio,
            "riwayat_pencapaian": None,
            "dll": None,
            "organisasi": None,
            "tempat_tanggal_lahir": None,
            }
        ...