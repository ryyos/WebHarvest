import asyncio

from typing import Dict, List
from asyncio import Queue, Semaphore
from playwright.async_api import BrowserContext, Browser, Page
from icecream import ic
from src.drivers import Playwright
from src.utils import Annotations
from .dependency import GoogleReviewsLibs

class GoogleReviews(GoogleReviewsLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__(options)
        self.__playwright = Playwright()

        self.__save: str = options["save"]
        self.__kafka: str = options["kafka"]
        self.__url: str = options["url"]
        self.__worker: str = options["worker"]
        ...

    async def main(self) -> None:
        browser: BrowserContext = await self.__playwright.browser()
        browser.set_default_timeout(120000)

        tasks: List[any] = []

        index = 0
        await self.execute('https://www.google.co.id/travel/search?ts=CAESCgoCCAMKAggDEAAaVAo2EjIyJDB4MmRhMzkzZjc5ZmVlYjVjNToweDEwMzBiZmJjYTdjYjg1MDoKSmF3YSBUaW11choAEhoSFAoHCOgPEAMYHRIHCOgPEAQYBRgHMgIIASoJCgU6A0lEUhoA&qs=CAESBENJUUgyKENob1FfNHlsMTlIS3RKU3RBUm9OTDJjdk1URjBlSEZzZVhab2RoQUM4AkgA&utm_campaign=sharing&utm_medium=link_btn&utm_source=htls&ap=KigKEgnfQ8UnHJkmwBFrcCL6T2tbQBISCXpQ5KkyphDAEWtwIvob6VxAMAC6AQhvdmVydmlldw&destination=East%20Java', browser)
        # async for hotel in self.collect_hotel(browser, self.__url):
            # ic(hotel)
            # tasks.append(self.execute(hotel, browser))
            # index+=1
            # if index % int(self.__worker) == 0:
            #     await asyncio.gather(*tasks)
            #     tasks.clear()

        await self.__playwright.close()
        ...