
from ApiRetrys import ApiRetry
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import HibankComponent

class HibankLibs(HibankComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract(self, data: dict) -> None:

        return {
            "nama_lengkap": data["Name"],
            "nama_jabatan": data["JobTitle"],
            "riwayat_pendidikan": None,
            "riwayat_pekerjaan": None,
            "link_foto": data["Image"],
            "biografi": PyQuery(data["Description"]).text(),
            "riwayat_pencapaian": None,
            "dll": None,
            "organisasi": None,
            "tempat_tanggal_lahir": None,
            }
        ...