import asyncio
from requests import Response
from icecream import ic
from typing import Dict
from pyquery import PyQuery
from .dependency import GeospasialLibs
from src.utils import File

class Geospasial(GeospasialLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__(options)
        ...

    async def main(self) -> None:
        response: Response = self.api.get(self.target_url)
        html: PyQuery = PyQuery(response.text)

        async for row in self.collect_url(html):
            if not row["url"] or row["url"] in self.dones: continue
            try:
                asyncio.gather(self.process_data(row))
                self.dones.append(row["url"])
                File.write_json('src/database/json/geospasial.json', self.dones)
            except Exception as err:
                ic(err)
            ...
        ...