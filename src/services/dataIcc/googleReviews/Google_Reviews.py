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
        ...

    async def main(self) -> None:
        browser: BrowserContext = await self.__playwright.browser()
        browser.set_default_timeout(120000)

        tasks: List[any] = []

        index = 0
        # await self.extract_hotel('https://www.google.co.id/travel/search?q=hotel%20di%20jawa%20timur&ved=0CBsQyvcEahgKEwiw_J2snYeFAxUAAAAAHQAAAAAQzwE&ap=MAE&qs=MihDaG9JbU9MNGhhcnRsYnE2QVJvTkwyY3ZNVEZyYWpKamJEYzBkaEFCOA0&ts=CAESCgoCCAMKAggDEAAaUgo0EjIyJDB4MmRhMzkzZjc5ZmVlYjVjNToweDEwMzBiZmJjYTdjYjg1MDoKSmF3YSBUaW11chIaEhQKBwjoDxADGBwSBwjoDxADGB0YATICEAAqBwoFOgNJRFI', browser)
        # await self.extract_hotel('https://www.google.co.id/travel/search?ts=CAESCgoCCAMKAggDEAAaVAo0EjIyJDB4MmRhMzkzZjc5ZmVlYjVjNToweDEwMzBiZmJjYTdjYjg1MDoKSmF3YSBUaW11chIcEhQKBwjoDxADGB0SBwjoDxADGB4YATIECAAQACoJCgU6A0lEUhoA&qs=MihDaG9RZy1yemo2YXQyOVdZQVJvTkwyY3ZNVEYyYzNRNGQzZDJNaEFDOAJIAA&utm_campaign=sharing&utm_medium=link_btn&utm_source=htls&ap=KigKEgkaex57ekUfwBEAAACuLCBcQBISCZyJehvGHx_AEQAAABIDIlxAMAC6AQhvdmVydmlldw&destination=East%20Java', browser)
        await self.extract_hotel('https://www.google.co.id/travel/search?ts=CAESCgoCCAMKAggDEAAaVAo0EjIyJDB4MmRhMzkzZjc5ZmVlYjVjNToweDEwMzBiZmJjYTdjYjg1MDoKSmF3YSBUaW11chIcEhQKBwjoDxADGB0SBwjoDxADGB4YATIECAAQACoJCgU6A0lEUhoA&qs=MihDaG9JeWVXbl85cjI3THlMQVJvTkwyY3ZNVEZ5Y3pGeWNtSTRaeEFCOAJIAA&utm_campaign=sharing&utm_medium=link_btn&utm_source=htls&ap=KigKEgm5yLEbpvYiwBGWqx-bEMBbQBISCf16kZZZVRbAEZarH5u4rVxAMAC6AQhvdmVydmlldw&destination=East%20Java', browser)
        # async for hotel in self.collect_hotel(browser):
        #     tasks.append(self.extract_hotel(hotel, browser))
        #     index+=1
        #     if index % 5 == 0:
        #         await asyncio.gather(*tasks)
        #         tasks.clear()

        await self.__playwright.close()
        ...