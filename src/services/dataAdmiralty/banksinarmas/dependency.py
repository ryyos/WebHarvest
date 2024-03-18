import asyncio

from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple, AsyncGenerator
from pyquery import PyQuery
from icecream import ic


from .component import BanksinarmasComponent
from src.utils import *

class BanksinarmasLibs(BanksinarmasComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def build_url(self, text: str) -> str:
        return '/'.join(text.split('/')[2:])
        ...

    async def sorter(self, html: PyQuery) -> AsyncGenerator[Dict[str, str], any]:
        switch: bool = False
        for tr in html.find('tbody tr'):
            if PyQuery(tr).find('h2'):
                switch: bool = not switch
                continue
            if not PyQuery(tr).text(): continue

            if switch:
                yield {
                    "type": "komisaris",
                    "url": self.base_url+self.build_url(PyQuery(tr).find('a').attr('href'))
                }
            else:
                yield {
                    "type": "direksi",
                    "url": self.base_url+self.build_url(PyQuery(tr).find('a').attr('href'))
                }
            ...
        ...


    async def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:
        ps: List[PyQuery] = html.find('div[class="container"]').eq(1).find('p')
        name: str = html.find('div[class="caption-content"] h1').eq(-1).text()
        jabatan: str = html.find('div[class="caption-content"] h2').text()
        foto: PyQuery = self.base_url+self.build_url(html.find('div[class="container"]').eq(1).find('img').attr('src'))
        bio: str = PyQuery(ps.pop(0)).text()
        pekerjaan: str = PyQuery(ps.pop(0)).text()
        organisasi: str = PyQuery(ps.pop(-1)).text()

        dll: str | None = None
        if ps:
            dll: str = '\n'.join([PyQuery(p).text() for p in ps])

        return (foto, name, jabatan, bio, pekerjaan, dll, organisasi)
        ...


    async def extract(self, url: str) -> Dict[str, any]:
        response: Response = self.api.get(url)
        html = PyQuery(response.text)

        (foto, name, jabatan, bio, pekerjaan, dll, organisasi) = await self.extract_bio(html)

        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "link_foto": foto,
            "biografi": bio,
            "riwayat_pekerjaan": pekerjaan,
            "dll": dll,
            "organisasi": organisasi,
            "riwayat_pendidikan": None,
            "riwayat_pencapaian": None,
            "tempat_tanggal_lahir": None,
            }