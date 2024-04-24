import asyncio

from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple, AsyncGenerator
from pyquery import PyQuery
from icecream import ic


from .component import CommbankComponent
from src.utils import *

class CommbankLibs(CommbankComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    async def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:

        name: str = html.find('hgroup').text().split(',')[-1]
        jabatan: str = html.find('hgroup').text().split(',')[0]
        foto: str = html.find('div.section.clearfix.content-wrap.m-t-55 img').attr('src')
        pekerjaan: str = html.find('div.section.clearfix.content-wrap.m-t-55 p').eq(-1).text()
        bio: str = PyQuery(html.find('div.section.clearfix.content-wrap.m-t-55 p')[:-1]).text()

        return (foto, name, jabatan, bio, pekerjaan)
        ...

    async def extract(self, url: str) -> List[Dict[str, any]]:
        response: Response = self.api.get(url)
        html: PyQuery = PyQuery(response.text)

        (foto, name, jabatan, bio, pekerjaan) = await self.extract_bio(PyQuery(html))

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