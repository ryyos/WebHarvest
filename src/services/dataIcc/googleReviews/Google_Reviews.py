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
        self.__playwright = Playwright(options["headless"])

        self.__url: str = options["url"]
        self.__worker: str = options["worker"]
        ...

    async def main(self) -> None:
        browser: BrowserContext = await self.__playwright.browser()
        browser.set_default_timeout(120000)

        tasks: List[any] = []

        index = 0
        async for hotel in self.collect_hotel(browser, self.__url):
            tasks.append(self.execute(hotel, browser))
            index+=1
            if index % int(self.__worker) == 0:
                await asyncio.gather(*tasks)
                tasks.clear()

        await self.__playwright.close()
        ...