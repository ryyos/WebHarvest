import asyncio
import json
from time import sleep
from requests import Response
from icecream import ic
from typing import Dict
from .dependency import UnodcLibs
from src.utils import Stream, Annotations

class Unodc(UnodcLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__(options)
        ...

    def build_param(self, start: int) -> dict:
        return f'?lng=en&criteria=%7B%22filters%22:%5B%7B%22fieldName%22:%22en%23__el.caseLaw.crimeTypes_s%22,%22value%22:%22Money+laundering%22%7D%5D,%22startAt%22:{start},%22sortings%22:%22%22%7D'
        ...

    @Annotations.stopwatch
    async def main(self) -> None:

        page = 0
        while True:
            response: Response = self.api.get(self.base_api+self.build_param(page))
            response: dict = response.json()

            Stream.found('ENODC', 'START PAGE', page)

            await asyncio.gather(*[self.extract(self.base_url+url["uri"]) for url in response["results"]])

            if not response["results"]: break
            page+= len(response["results"])
            ...

        ...