import asyncio

from icecream import ic
from playwright.async_api import async_playwright, BrowserContext, Browser, Page
from time import sleep

class Playwright:

    def __init__(self, headless: bool) -> None:
        self.headless = headless
        self.playwright = None
        self.browsers = None
        self.chrome = None
        ...

    async def browser(self) -> BrowserContext:
        self.playwright = await async_playwright().start()
        self.chrome: Browser = await self.playwright.chromium.launch(headless=self.headless, args=['--window-position=-8,-2'])
        self.browsers: BrowserContext = await self.chrome.new_context()
        return self.browsers
    
    async def close(self) -> None:
        await self.browsers.close()
        await self.chrome.close()
        await self.playwright.stop()
        ...
    
