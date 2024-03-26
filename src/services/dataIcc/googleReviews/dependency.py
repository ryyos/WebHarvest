import asyncio

from asyncio import sleep, Queue, Semaphore
from icecream import ic
from playwright.async_api import BrowserContext, Page, Locator
from typing import AsyncGenerator, List, Dict, Any
from pyquery import PyQuery
from dekimashita import Dekimashita

from .component import GoogleReviewsComponent
from src.utils import *

class GoogleReviewsLibs(GoogleReviewsComponent):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__()

        self.query: str = options["query"]
        self.topic: str = options.get('topic', None)
        ...

    def vfree(self, text: str) -> str:
        if 'gratis' in text: return text.replace('gratis', '') + ' gratis'
        else: return text
        ...

    def check_url(self, text: str) -> str:
        try:
            if 'https:' not in text: return 'https'+text
            else: return text
        except Exception:
            return text

    async def completed_not_yet(self, id: str) -> bool:
        
        ...

    async def collect_hotel(self, browser: BrowserContext) -> AsyncGenerator[str, any]:
        base_page: Page = await browser.new_page()
        await base_page.goto(url=self.base_query)

        while True:
            hotels: List[any] = await base_page.query_selector_all('a[class="PVOOXe"]')

            for hotel in hotels:
                yield self.google_url+await hotel.get_attribute('href')

            try:
                await base_page.wait_for_selector('#id > c-wiz > c-wiz:nth-child(26) > div.eGUU7b > button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-INsAgc.VfPpkd-LgbsSe-OWXEXe-Bz112c-UbuQg.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.Rj2Mlf.OLiIxf.PDpWxe.LQeN7.my6Xrf.wJjnG.dA7Fcf.tEQgl > span')
                next: Locator = await base_page.query_selector('#id > c-wiz > c-wiz:nth-child(26) > div.eGUU7b > button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-INsAgc.VfPpkd-LgbsSe-OWXEXe-Bz112c-UbuQg.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.Rj2Mlf.OLiIxf.PDpWxe.LQeN7.my6Xrf.wJjnG.dA7Fcf.tEQgl > span')
                if not next: break
                await next.click()
            except Exception:
                break
        await base_page.close()
        ...

    async def metadata(self, url: str, page: Page) -> Dict[str, any]:
        html: PyQuery = PyQuery(await page.content())
        head = {
            "link": url,
            "id": Endecode.md5_hash(Dekimashita.valpha(html.find('title').eq(0).text())),
            "name": html.find('title').eq(0).text().split(' - ')[0],
            "topic_kafka": self.topic,
            "domain": self.domain,
            "tags": [self.domain],
            "crawling_time": Time.now(),
            "crawling_time_epoch": Time.epoch(),
        }

        return head
        ...

    async def topsights(self, html: PyQuery) -> List[Dict[str, any]]:

        topsights: List[dict] = []
        for top in html.find('div[class="unrdjc"]'):
            topsights.append({
                "thumbnail": val(PyQuery(top).find('img[class="x7VXS I2nXKd"]').attr('data-src')),
                "place": val(PyQuery(top).find('div.AFZtd').text()),
                "rating": to_float(val(PyQuery(top).find('span.KFi5wf').text())),
                "total_ratings": val(PyQuery(top).find('span.jdzyld').text()),
                "location": val(PyQuery(top).find('div.bJlStd').text()),
                "distance": val(PyQuery(top).find('span[class="kJW6fe"]').text()) or val(PyQuery(top).find('div[class="kC4Ofd NUiScc"]').text())
            })
            ...

        return topsights
        ...

    async def nearby_places(self, page: Page) -> Dict[str, any]:
        html: PyQuery = PyQuery(await page.content())
        html: PyQuery = html.find('section[class="OEscc"]')

        nearby = {
            "point": html.find('div[data-tab="location"] text').text(),
            "topsights": val(await self.topsights(html.find('#topsights'))),
            "restaurants": val(await self.topsights(html.find('#restaurants'))),
            "airports": val(await self.topsights(html.find('#airports'))),
            "transit": val(await self.topsights(html.find('#transit'))),
        }

        return nearby
        ...

    async def get_detail_v1(self, html: PyQuery) -> str:
        html: PyQuery = html.find('div[class="FbLHzc kh7loe"] div[jsname="z5Cjge"] > div[class="BczChc eoY5cb"]')
        detail = {
            "deskripsi": html.find('section[class="O3oTUb"]').eq(0).text(),
            "penting":
                    {str(index): PyQuery(div).text() for index, div in enumerate(html.find('section[class="O3oTUb pR0Q9b"]').eq(0).find('div[class="xGm0S B8PKdc XSe9p"]'))} ,
            "waktu_check_in": html.find('section[class="O3oTUb"]').eq(-1).find('div').eq(0).text().split(': ')[-1],
            "waktu_check_out": html.find('section[class="O3oTUb"]').eq(-1).find('div').eq(-1).text().split(': ')[-1],
        }

        return detail
        ...

    async def get_detail_v2(self, html: PyQuery) -> str:
        html: PyQuery = html.find('div[jsname="z5Cjge"] > div[class="BczChc eoY5cb"]')
        detail = {
            "deskripsi": '\n'.join([PyQuery(p).text() for p in html.find('section[class="mEKuwe G8T82"]  p.GtAk2e')]),
            "waktu_check_in": html.find('section[class="mEKuwe G8T82"]').eq(0).find('span[class="IIl29e"]').eq(0).text(),
            "waktu_check_out": html.find('section[class="mEKuwe G8T82"]').eq(0).find('span[class="IIl29e"]').eq(-1).text(),
            "alamat": html.find('div[class="GtAk2e"] span[class="XGa8fd"]').eq(0).text(),
            "phone": html.find('div[class="GtAk2e"] span[class="XGa8fd"]').eq(1).text(),
        }

        return detail
        ...

    async def get_fasilitas_v1(self, html: PyQuery) -> Dict[str, any]:
        raw_fac: List[PyQuery] = [PyQuery(span).text() for span in html.find('section[class="O3oTUb pR0Q9b"] > div[class="hwR8Dd DmBmM fmFs0c"]').eq(-1).find('div[class="xGm0S B8PKdc XSe9p"]')]\
            + [PyQuery(span).text() for span in html.find('section[class="O3oTUb pR0Q9b"] > div[class="hwR8Dd DmBmM fmFs0c"]').eq(-1).find('div[class="xGm0S AOZSGb XSe9p"]')]
        
        fasilitas: List[dict] = {str(index): value for index, value in enumerate(raw_fac)}
        return fasilitas
        ...

    async def get_fasilitas_v2(self, html: PyQuery) -> Dict[str, any]:

        fasilitas: List[dict] = []

        for fac in html.find('div[class="eFfcqe G8T82"] div[class="IYmE3e"]'):
            fasilitas.append({
                PyQuery(fac).find('h4').text():
                    {str(index): self.vfree(PyQuery(li).text()) for index, li in enumerate(PyQuery(fac).find('ul > li'))}
            })

        return fasilitas
        ...

    async def get_kesehatan(self, html: PyQuery) -> Dict[str, any]:
        kesehatans: List[dict] = []
        for div in html.find('section[class="mEKuwe G8T82"] > div[jscontroller="N4VHee"]'):
            kesehatans.append({
                PyQuery(div).find('h4').text():
                    {str(index): PyQuery(li).text() for index, li in enumerate(PyQuery(div).find('ul > li'))}
            })
            ...

        return kesehatans
        ...

    async def get_photo_v1(self, page: Page) -> List[str]:
        html: PyQuery = PyQuery(await page.content())
        photos: List[str] = ['https:'+PyQuery(img).attr('src') for img in html.find('div[jsname="TeyQfe"] img')]
        return photos
        ...

    async def get_photo_v2(self, page: Page) -> List[str]:
        all_button = await page.query_selector_all('div[jsname="t1pjHf"] div[jsname="oZzHLe"]')
        for button in all_button:
            classe: str = await button.evaluate('(element) => element.getAttribute("class")')
            while True:
                await button.click()
                await sleep(5)
                classe: str = await button.evaluate('(element) => element.getAttribute("class")')
                break
                if 'eLNT1d' in classe: break
            
        html: PyQuery = PyQuery(await page.content())
        return [self.check_url(PyQuery(img).attr('src')) for img in html.find('div[class="M3UVH"] img')]
        ...

    async def price(self, page: Page) -> Dict[str, any]:
        await page.locator('//*[@id="prices"]/span').click()
        html: PyQuery = PyQuery(await page.content())

        choices: List[PyQuery] = html.find('div[jsname="Nf35pd"]').eq(-1).find('a[jsname="xf4CU"]')

        prices: List[dict] = []
        for choice in choices:
            prices.append({
                    "url": self.google_url+PyQuery(choice).attr('href'),
                    "website": PyQuery(choice).find('span[class="NiGhzc"]').text(),
                    "harga": PyQuery(choice).find('span[class="nDkDDb"]').text(),
                })

        return vlist_dict(prices, 'website')
        ...

    async def photo(self, page: Page) -> List[str]:
        await page.locator('//*[@id="photos"]/span').click()
        html: PyQuery = PyQuery(await page.content())

        photo: None = None
        photo_v1: bool = bool(html.find('div[jsname="TeyQfe"]'))
        photo_v2: bool = bool(html.find('div[jsname="t1pjHf"]'))
        if photo_v1: photo: List[str] = await self.get_photo_v1(page)
        if photo_v2: photo: List[str] = await self.get_photo_v2(page)

        return photo
        ...

    async def about(self, page: Page) -> Dict[str, any]:
        await page.locator('//*[@id="details"]/span').click()
        html: PyQuery = PyQuery(await page.content())

        detail: None = None
        detail_v1: bool = bool(html.find('div[jsname="z5Cjge"] > div[class="BczChc eoY5cb"] div.fmFs0c'))
        detail_v2: bool = bool(html.find('div[jsname="z5Cjge"] > div[class="BczChc eoY5cb"]'))
        if detail_v1: detail: dict = await self.get_detail_v1(html)
        elif detail_v2: detail: dict = await self.get_detail_v2(html)

        fasilitas: None = None
        fasilitas_v1: bool = bool(html.find('div[class="FbLHzc kh7loe"] div[jsname="z5Cjge"] > div[class="BczChc eoY5cb"] section[class="O3oTUb pR0Q9b"] > div[class="hwR8Dd DmBmM fmFs0c"]'))
        fasilitas_v2: bool = bool(html.find('div[class="eFfcqe G8T82"]'))
        if fasilitas_v1: fasilitas: dict = await self.get_fasilitas_v1(html)
        elif fasilitas_v2: fasilitas: dict = await self.get_fasilitas_v2(html)

        kesehatan: None = None
        kesehatan_v1: bool = bool(html.find('section[class="mEKuwe G8T82"] > div[jscontroller="N4VHee"]'))
        if kesehatan_v1: kesehatan: dict = await self.get_kesehatan(html)

        about = {
            "detail": detail,
            "fasilitas": fasilitas,
            "Kesehatan_dan_keselamatan": kesehatan
        }

        return about
        ...

    async def reviews_header(self, page: Page) -> Dict[str, any]:
        await page.locator('//*[@id="reviews"]/span').click()
        html: PyQuery = PyQuery(await page.content())

        google_rating: PyQuery = html.find('div[class="pDLIp"] div.SRQlQ')
        review_header = {
            "review_google": {
                    "total_rating": val(html.find('div[class="FBsWCd"]').eq(0).text()),
                    "total_ulasan": val(to_int(Dekimashita.vnum(html.find('span[class="P2NYOe GFm7je sSHqwe"]').eq(0).text()))),
                    "detail_rating": val({
                        Dekimashita.vdir(PyQuery(div).find('div[class="CQYfx N7orM"]').text()):  PyQuery(div).find('div[class="RrMXgd uT0pob"]').attr('style').split(' ')[-1]\
                            for div in html.find('div[class="dcdcEf UsMcpf"]')   
                    })
                },
            "reviews_website": [
                {
                    "url": PyQuery(div).attr('href'),
                    "domain": PyQuery(div).find('div[class="lvpOub"]').text(),
                    "total_rating": PyQuery(div).find('div[class="s97yQ ogfYpf"] span.QB2Jof').text(),
                    "total_ulasan": to_int(Dekimashita.vnum(PyQuery(div).find('div[class="s97yQ ogfYpf"] span.CQYfx').text())),
                } for div in html.find('div[jsname="a4yjDf"] > div[class="TL1fMd F0n91b"] a')
            ],
            "lainnya": {
                Dekimashita.valpha(PyQuery(span).find('span[jsname="ODzDMd"]').text()): to_int(Dekimashita.vnum(PyQuery(span).find('span[jsname="ODzDMd"]').text()))\
                    for span in html.find('div[jsname="EHpbmb"] span[jsname="zuUKYb"]')
            }
        }

        return review_header
        ...

    async def reviews(self, page: Page) -> AsyncGenerator[Dict[str, any], any]:
        await page.locator('//*[@id="reviews"]/span').click()
        html: PyQuery = PyQuery(await page.content())

        bottom: bool = False
        scroll_height = await page.evaluate("document.body.scrollHeight")
        current_height = await page.evaluate("window.scrollY + window.innerHeight")
        await page.locator('//*[@id="reviews"]/c-wiz/c-wiz/div/div/div/div/div[1]/div[1]').click()
        index_done = 0
        while not bottom:
            html: PyQuery = PyQuery(await page.content())
            scroll_height = await page.evaluate("document.body.scrollHeight")
            current_height = await page.evaluate("window.scrollY + window.innerHeight")

            ic(scroll_height)
            ic(current_height)

            for review in html.find('div[jsname="Pa5DKe"] div[class="Svr5cf bKhjM"]')[index_done:]:
                index_done+=1
                yield {
                    "id_review": Endecode.md5_hash(PyQuery(review).find('div[class="aAs4ib"] span[class="k5TI0"] > a').text()),
                    "username_reviews": PyQuery(review).find('div[class="aAs4ib"] span[class="k5TI0"] > a').text() \
                        or PyQuery(review).find('div[class="aAs4ib"] span[class="k5TI0"] span.faBUBf').text(),
                    "image_reviews": PyQuery(review).find('div[class="jUkSGf WwUTAf"] img').attr('src'),
                    "created_time": PyQuery(review).find('span[class="iUtr1 CQYfx"]').text(),
                    "created_time_epoch": None,
                    "reviews_rating": PyQuery(review).find('div[class="GDWaad"]').text(),
                    "detail_reviews_rating": [
                        {
                            "score_rating": PyQuery(tag).find('span').eq(-1).text(),
                            "category_rating": PyQuery(tag).find('span').eq(0).text(),
                        } for tag in PyQuery(review).find('div[class="dA5Vzb"]')
                    ],
                    "tags_review": list(PyQuery(review).find('div[class="ThUm5b"]').text().split(' ❘ ')),
                    "content_reviews": PyQuery(review).find('div[class="STQFb eoY5cb"] div[class="K7oBsc"]').text(),
                    "reply_content_reviews": {
                        "username_reply_reviews": "null",
                        "content_reviews": "null"
                    },
                    "media_reviews": [
                        PyQuery(img).find('img').attr('data-src') or PyQuery(img).find('img').attr('src') for img in PyQuery(review).find('div[class="fBMzfe"] div[jsname="o8HAFf"]')
                    ]
                }
                ...
            
            if current_height >= scroll_height:
                bottom = True
            else:
                while True:
                    await page.keyboard.press("ArrowDown")
                    new_current_height = await page.evaluate("window.scrollY + window.innerHeight")
                    if new_current_height == current_height: break
                    current_height = new_current_height
            ...
        ...

    async def extract_hotel(self, url: str, page: Page) -> None:
        await page.goto(url)
        await sleep(5)

        html: PyQuery = PyQuery(await page.content())

        result: dict = {
            **await self.metadata(url, page),
            "tempat_terdekat": await self.nearby_places(html.find('section[class="OEscc"]')),
            "harga": await self.price(page),
            "tentang": await self.about(page),
            "foto": await self.photo(page),
            "reviews": await self.reviews_header(page)
        }

        async for review in self.reviews(page):
            result["reviews"].update(review)
            File.write_json(f'data/data_raw/icc/google-reviews/json/{Time.epoch_ms()}.json', result)
        
        ...

    async def execute(self, url: str, browser: BrowserContext) -> None:
        page: Page = await browser.new_page()
        try:
            await self.extract_hotel(url, page)
        except Exception:
            ...
        finally:
            await page.close()
