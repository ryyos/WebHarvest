import asyncio

from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple, AsyncGenerator
from pyquery import PyQuery
from icecream import ic


from .component import BoiindonesiaComponent
from src.utils import *

class BoiindonesiaLibs(BoiindonesiaComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    async def sorter(self, html: PyQuery) -> AsyncGenerator[Dict[str, str], any]:
        komisaris_check: bool = False
        direksi_check: bool = False

        childrens: List[PyQuery] = html.find('table[class="teks"] table').children()

        for index, tr in enumerate(childrens):
            if not PyQuery(tr).text(): continue

            if 'CORPORATE SECRETARY PROFILE' in PyQuery(tr).text(): break

            if 'DIRECTORS PROFILE' in PyQuery(tr).text():
                direksi_check = True
            elif direksi_check:
                yield {
                    "type": "direksi",
                    "html": PyQuery(tr)
                }
                ...

            if 'COMMISSIONERS PROFILE' in PyQuery(tr).text():
                komisaris_check = True
            elif komisaris_check and not direksi_check:
                yield {
                    "type": "komisaris",
                    "html": PyQuery(tr)
                }
                ...
            ...
        ...

    async def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:

        name: str = html.find('span[class="submenu"]').text().split('\n')[0]
        jabatan: str = html.find('span[class="submenu"]').text().split('\n')[-1]
        foto: str = self.base_url+html.find('img').attr('src')
        bio: str = html.find('td').text().split('\n')[-1]

        return (foto, name, jabatan, bio)
        ...

    async def extract(self, html: PyQuery) -> Dict[str, any]:
        (foto, name, jabatan, bio) = await self.extract_bio(html)

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