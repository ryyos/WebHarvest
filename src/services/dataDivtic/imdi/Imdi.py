import asyncio

from requests import Response
from icecream import ic
from typing import Dict
from .dependency import ImdiLibs

class Imdi(ImdiLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__(options)
        ...

    def build_param(self, code: int = None) -> str:
        if code: return {
            "pilar": "infrastruktur_ekosistem_1",
            "type_kategori": "klasifikasi_pilar_1",
            "provinsi": code
        }
        else: return {
            "pilar": "infrastruktur_ekosistem_1",
            "type_kategori": "klasifikasi_pilar_1",
        }
        ...

    async def main(self) -> None:

        async for provinsi in self.collect_provinsi(self.base_api_all, self.build_param()):
            asyncio.gather(self.extract(self.base_api, self.build_param(provinsi["code"]), provinsi["provinsi"]))
            ...

        ...