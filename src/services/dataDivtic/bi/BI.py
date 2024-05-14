import requests
import asyncio
import httpx

from time import sleep
from loguru import logger
from icecream import ic
from requests import Response
from pyquery import PyQuery
from typing import Dict, List
from dekimashita import Dekimashita
from .dependency import BILibs

from src.server import S3
from src.drivers import Browser, Page
from src.utils import File, Time, Dir, Endecode

class BI(BILibs):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__(options)
        
        self.__s3: bool = options.get('s3')
        self.__save: bool = options.get('save')
        self.__mode: str = options.get('mode')
        self._url: str = options.get('url')
        self._category: str = options.get('category')
        
    def metadata(self, **kwargs) -> Dict[str, any]:
        result = {
            "id": kwargs["id"],
            "link": kwargs["link"],
            "domain": kwargs["domain"],
            "tags": [kwargs["domain"], self._category],
            "crawling_time": Time.now(),
            "crawling_time_epoch": Time.epoch(),
            "path_data_raw": self.base_path_s3+kwargs["path_json"],
            "path_data_clean": self.base_path_s3+Dir.convert_path(kwargs["path_json"]),
        }
        
        return result
        ...
    
    def gambar_uang(self, page: Page) -> None:
        # html: PyQuery = self.fetch(self.gambar_uang_url)
        page.goto(self.gambar_uang_url)
        html: PyQuery = PyQuery(page.content())
        
        
        for img, url, title, code in self.collect_money(html):
            try:
                page.goto(url)
                html: PyQuery = PyQuery(page.content())
                bahan: str = url.split('Bahan=')[-1].split('&')[0]
                id: str = url.split('=')[-1]
                name_file: str = Dekimashita.vdir(f"{bahan}_{title}_{id}")
                path_json: str = f'data/data_raw/bank_indonesia/gambar_uang/{bahan}/json/{name_file}.json'
                
                money_data: dict = self.extract_money(html, img)
                metadata: dict = self.metadata(
                    id=Endecode.md5_hash(name_file),
                    link=url,
                    domain='www.bi.go.id',
                    path_json=path_json,
                )
                
                logger.info(f'EXTRACT DATA [ {id} ]')
                
                metadata["path_images"] = self.download(money_data, bahan, page)
                metadata["title"] = title
                metadata["code"] = code
                
                result: dict = {
                    **metadata,
                    **money_data
                    }
                
                if self.__save:
                    File.write_json(path_json, result)
                    
                S3.upload_json(
                    body=result,
                    destination=path_json,
                    send=self.__s3
                )
                
            except Exception as err:
                File.write('src/services/dataDivtic/bi/error.log', f'ERROR URL [ {url} ] MESSAGES [ {str(err)} ]')
            ...
        ...
        
    def paged(self, page: Page, page_02: Page) -> None:
        page.goto(self._url)
        html: PyQuery = PyQuery(page.content())
        
        if html.find('div#accordion'):
            self.data_top(page, html, self.metadata, page_02)
        
        while True:
        
            html: PyQuery = PyQuery(page.content())
            
            for url in self.collect_url_items(html):
                if url in self.dones: 
                    logger.info(f'DONE [ {url} ]')
                    continue
                try:
                    page_02.goto(url)
                    html: PyQuery = PyQuery(page_02.content())
                    
                    data_items: dict = self.extract_items(html)
                    
                    path_document: str = f'data/data_raw/bank_indonesia/{self._category}/{Dekimashita.vdir(data_items["title"])}/'
                    path_document: List[str] | str = self.curl(path_document, page_02)
                    path_json: str = f'data/data_raw/bank_indonesia/{self._category}/{Dekimashita.vdir(data_items["title"])}/json/{Dekimashita.vdir(data_items["title"])}.json'
                    
                    logger.info(f'EXTRACT FILE [ {data_items["title"]} ]')
                    metadata: dict = self.metadata(
                        id=Endecode.md5_hash(data_items["title"]),
                        link=url,
                        domain='www.bi.go.id',
                        path_json=path_json,
                    )
                    
                    result = {
                        **metadata,
                        **data_items,
                        "path_documents": path_document,
                    }
                    
                    if self.__save:
                        File.write_json(path_json, result)
                    S3.upload_json(
                        body=result,
                        destination=path_json,
                        send=self.__s3
                    )
                except Exception as err:
                    logger.error(f'ERROR [ {url} ] MESSAGE [ {str(err)} ]')
                    File.write('src/services/dataDivtic/bi/items_error.log', f'{url} [ {str(err)} ]')
                    
                finally:
                    self.dones.append(url)
                    File.write_json(self.path_dones, self.dones)
            
            if html.find('input.aspNetDisabled.next'): break
            # if not html.find('input[class="next"]'): break
            
            page.locator('input[class="next"]').click()
            sleep(10)
            
            html: PyQuery = PyQuery(page.content())
            ...
        ...
    
    def main(self) -> None:
        _browser: Browser = self.playwright.start()
        _browser.set_default_timeout(120000)
        _page: Page = _browser.new_page()
        # try:
        match self.__mode:
            case 'gambar_uang':
                self.gambar_uang(_page)
                
            case 'items':
                _page_02: Page = _browser.new_page()
                self.items(_page, _page_02)
                _page_02.close()
                
            case 'paged':
                _page_02: Page = _browser.new_page()
                self.paged(_page, _page_02)
                _page_02.close()
                
            case _:
                raise ValueError(f'Invalid mode: {self.__mode}')
        # except Exception as err:
        #     print('ERROR: ' + str(err))
        # finally:
        _page.close()
        self.playwright.close()
        ...