import asyncio

from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple, AsyncGenerator
from pyquery import PyQuery
from icecream import ic


from .component import BankmayapadaComponent

class BankmayapadaLibs(BankmayapadaComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    async def sorter(self, html: PyQuery) -> AsyncGenerator[Dict[str, str], any]:
        switch: bool = False
        for tr in html.find('tbody tr'):
            if PyQuery(tr).find('h2'):
                switch: bool = not switch
                continue
            
            if not PyQuery(tr).text(): continue
            if 'meninggal' in PyQuery(tr).find('a').attr('href'): break

            if switch:
                yield {
                    "type": "komisaris",
                    "url": self.base_url+PyQuery(tr).find('a').attr('href')
                }
            else:
                yield {
                    "type": "direksi",
                    "url": self.base_url+PyQuery(tr).find('a').attr('href')
                }
            ...
        ...

    async def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:

        childrens: List[PyQuery] = html.find('div[class="item-page"]').children()
        
        raw_foto: PyQuery = PyQuery(childrens.pop(0))
        foto: str = self.base_url + (raw_foto.find('a').attr('href') or raw_foto.find('img').attr('src'))
        name: str = PyQuery(childrens[0]).text().split('\n')[0]
        jabatan: str = PyQuery(childrens.pop(0)).text().split('\n')[-1]
        bio: str = PyQuery(childrens.pop(0)).text()

        if not bio:
            bio: str = PyQuery(childrens.pop(0)).text()

        pekerjaan: str = '\n'.join([PyQuery(child).text() for child in childrens])

        return (foto, name, jabatan, bio, pekerjaan)
        ...

    async def extract(self, url: str) -> Dict[str, any]:
        response: Response = self.api.get(url)
        html = PyQuery(response.text)

        (foto, name, jabatan, bio, pekerjaan) = await self.extract_bio(html)

        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "link_foto": foto,
            "biografi": bio,
            "riwayat_pekerjaan": pekerjaan,
            "dll": None,
            "organisasi": None,
            "riwayat_pendidikan": None,
            "riwayat_pencapaian": None,
            "tempat_tanggal_lahir": None,
            }
        ...