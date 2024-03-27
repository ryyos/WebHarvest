import asyncio

from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple, AsyncGenerator
from pyquery import PyQuery
from icecream import ic


from .component import CcbComponent
from src.utils import *

class CcbLibs(CcbComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    async def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:

        ps: List[PyQuery] = list(map(lambda p: PyQuery(p).text(), html.find('p')))

        name: str = html.find('h3').text()
        jabatan: str = html.find('h4').text()
        bio: str = ps.pop(0)
        dll: str = ps.pop(-1)
        pekerjaan: str = '\n'.join(ps)
        foto: str = self.base_url+html.find('img').attr('src')

        return (foto, name, jabatan, bio, dll, pekerjaan)
        ...

    async def extract(self, html: PyQuery) -> List[Dict[str, any]]:
        profiles: List[PyQuery] = html.find('div[class="container"]')

        results: List[dict] = []
        for profile in profiles:
            try:
                (foto, name, jabatan, bio, dll, pekerjaan) = await self.extract_bio(PyQuery(profile))
            except Exception:
                continue
            if not name: continue

            results.append({
                "nama_lengkap": name,
                "nama_jabatan": jabatan,
                "link_foto": foto,
                "biografi": bio,
                "riwayat_pekerjaan": pekerjaan,
                "dll": dll,
                "organisasi": None,
                "riwayat_pendidikan": None,
                "riwayat_pencapaian": None,
                "tempat_tanggal_lahir": None,
            })

            ...

        return results
        ...