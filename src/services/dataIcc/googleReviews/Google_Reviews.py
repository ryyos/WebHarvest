import asyncio

from typing import Dict, List
from asyncio import Queue, Semaphore
from playwright.async_api import BrowserContext, Browser, Page
from icecream import ic
from src.drivers import AsyncPlaywrightfrom src.utils import Annotations
from .dependency import GoogleReviewsLibs

class GoogleReviews(GoogleReviewsLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__(options)
        self.__playwright = Playwright(options["headless"])

        self.__url: str = options["url"]
        self.__worker: str = options["worker"]
        ...

    @Annotations.stopwatch
    async def main(self) -> None:
        browser: BrowserContext = await self.__playwright.browser()
        browser.set_default_timeout(120000)

        tasks: List[any] = []

        index = 0
        # await self.execute('https://www.google.co.id/travel/search?ts=CAESCgoCCAMKAggDEAAaVgo2EjIyJDB4MmRhMzkzZjc5ZmVlYjVjNToweDEwMzBiZmJjYTdjYjg1MDoKSmF3YSBUaW11choAEhwSFAoHCOgPEAQYAxIHCOgPEAQYBBgBMgQIABAAKgcKBToDSURS&qs=CAEyKENob0l5ZVduXzlyMjdMeUxBUm9OTDJjdk1URnljekZ5Y21JNFp4QUI4AkgA&utm_campaign=sharing&utm_medium=link_btn&utm_source=htls&ap=KigKEgkt4Ax__j0jwBEAAACA6vJbQBISCWJF5PvZvhPAEQAAAID2bVxAMAC6AQhvdmVydmlldw&destination=East%20Java', browser)
        async for hotel in self.collect_hotel(browser, self.__url):
            tasks.append(self.execute(hotel, browser))
            index+=1
            if index % int(self.__worker) == 0:
                await asyncio.gather(*tasks)
                tasks.clear()

        await self.__playwright.close()
        ...