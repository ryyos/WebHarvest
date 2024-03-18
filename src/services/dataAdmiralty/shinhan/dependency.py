import asyncio

from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple, AsyncGenerator
from pyquery import PyQuery
from icecream import ic


from .component import ShinhanComponent
from src.utils import *

class ShinhanLibs(ShinhanComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    async def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:

        name: str = html.find('div[class="desc-bod"] h3').text()
        jabatan: str = html.find('div[class="desc-bod"] span').text()
        bio: str = html.find('div[class="inbod"] p').text()
        foto: str = html.find('div[class="img-bod"] img').attr('src')

        return (foto, name, jabatan, bio)
        ...

    async def extract(self, html: PyQuery) -> List[Dict[str, any]]:
        profiles: List[PyQuery] = html.find('div[class="box-list-bod"] > div')

        results: List[dict] = []
        for profile in profiles:
            (foto, name, jabatan, bio) = await self.extract_bio(PyQuery(profile))

            results.append({
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
            })

            ...

        return results
        ...