import asyncio

from icecream import ic
from playwright.sync_api import sync_playwright, BrowserContext, Browser, Page
from time import sleep

class SyncPlaywright:

    def __init__(self, headless: bool) -> None:
        self.headless = headless
        self.playwright = None
        self.browsers = None
        self.chrome = None
        ...

    def start(self) -> BrowserContext:
        self.playwright = sync_playwright().start()
        self.chrome: Browser = self.playwright.chromium.launch(headless=self.headless, args=['--window-position=-8,-2'])
        self.browsers: BrowserContext = self.chrome.new_context()
        return self.browsers
    
    def close(self) -> None:
        self.browsers.close()
        self.chrome.close()
        self.playwright.stop()
        ...
    
