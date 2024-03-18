import asyncio

from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple, AsyncGenerator
from pyquery import PyQuery
from icecream import ic


from .component import BankmestikaComponent
from src.utils import *

class BankmestikaLibs(BankmestikaComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    async def extract_table(self, html: PyQuery) -> str:
        trs: List[PyQuery] = html.find('tr')
        words: List[str] = []
        for tr in trs[1:]:
            words.append(PyQuery(tr).find('td:first-child').text() + ': '+PyQuery(tr).find('td:last-child').text())
            ...
        return '\n'.join(words)
        ...

    async def extract(self, main_html: PyQuery, selector_html: PyQuery) -> List[Dict[str, any]]:

        results: List[dict] = []
        for a in selector_html.find('a'):
            html: PyQuery = main_html.find(PyQuery(a).attr('href'))

            results.append({
                "nama_lengkap": html.find('font[class="name"]').text(),
                "nama_jabatan": html.find('font[class="position"]').text(),
                "link_foto": html.find('img').attr('src'),
                "biografi": html.find('p').eq(0).text(),
                "riwayat_pekerjaan": await self.extract_table(html.find('table').eq(0)) if html.find('font[class="name"]').text() != 'Katio' else await self.extract_table(html.find('table').eq(1)),
                "riwayat_pendidikan": await self.extract_table(html.find('table').eq(-1)),
                "dll": None,
                "organisasi": None,
                "riwayat_pencapaian": None,
                "tempat_tanggal_lahir": None,
            })
            ...

        return results
        ...