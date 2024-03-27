import asyncio

from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple, AsyncGenerator
from pyquery import PyQuery
from icecream import ic


from .component import PerdaniaComponent
from src.utils import *

class PerdaniaLibs(PerdaniaComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    async def extract(self, html: PyQuery) -> List[Dict[str, any]]:

        result = {
                "nama_lengkap": html.find('td').eq(-1).text(),
                "nama_jabatan": html.find('td').eq(0).text(),
                "link_foto": None,
                "biografi": None,
                "riwayat_pekerjaan": None,
                "dll": None,
                "organisasi": None,
                "riwayat_pendidikan": None,
                "riwayat_pencapaian": None,
                "tempat_tanggal_lahir": None,
            }

        return result
        ...