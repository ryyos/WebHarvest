import asyncio

from typing import Dict, List
from asyncio import Queue, Semaphore
from playwright.async_api import BrowserContext, Browser, Page
from icecream import ic
from src.drivers import AsyncPlaywright
from src.utils import Annotations, File, Time
from .dependency import GoogleReviewsLibs
from time import perf_counter

class GoogleReviews(GoogleReviewsLibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__(options)
        self.__playwright = AsyncPlaywright(options["headless"])

        # self.__url: str = options["url"]
        self.__url = 'https://www.google.co.id/travel/search?q=hotel%20di%20jawa%20timur&ved=0CAAQ5JsGahgKEwiw_J2snYeFAxUAAAAAHQAAAAAQtwE&ap=MAA&qs=SAA'
        self.__worker: str = options["worker"]
        ...

    @Annotations.stopwatch
    async def main(self) -> None:
        start: float = perf_counter()
        File.write(self.path_log, f' START [ {Time.now()} ]')
        browser: BrowserContext = await self.__playwright.browser()
        browser.set_default_timeout(120000)

        tasks: List[any] = []

        index = 0
        # await self.execute('https://www.google.co.id/travel/search?q=hotel%20di%20jawa%20timur&ap=MAC6AQhvdmVydmlldw&qs=MihDaG9JazRQaTk3bjRtdm5yQVJvTkwyY3ZNVEYyWTNac1kxOW5NaEFCOA1IAA&ts=CAESCgoCCAMKAggDEAAaVAo0EjIyJDB4MmRhMzkzZjc5ZmVlYjVjNToweDEwMzBiZmJjYTdjYjg1MDoKSmF3YSBUaW11chIcEhQKBwjoDxAEGBwSBwjoDxAEGB0YATIECAAQACoHCgU6A0lEUg', browser)
        async for hotel in self.collect_hotel(browser, self.__url):
            tasks.append(self.execute(hotel, browser))
            index+=1
            if index % int(self.__worker) == 0:
                await asyncio.gather(*tasks)
                tasks.clear()

        await self.__playwright.close()
        File.write(self.path_log, f'DONE :: TIME NEED [ {perf_counter() - start} ]')
        ...