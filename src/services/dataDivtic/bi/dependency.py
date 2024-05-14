import re
import requests
import urllib.request
import httpx

from time import sleep
from loguru import logger
from io import BytesIO
from requests import Response
from dekimashita import Dekimashita
from icecream import ic
from ApiRetrys import ApiRetry
from pyquery import PyQuery
from typing import Dict, List, Tuple, Generator

from src.utils import File, Dir, Endecode, Down, Zip
from src.server import S3
from src.drivers import SyncPlaywright, Page, ElementHandle
from .component import BIComponent

class BILibs(BIComponent):
    def __init__(self, options: Dict[str, any]) -> None:
        super().__init__()
        
        self.__s3: bool = options.get('s3')
        self.__save: bool = options.get('save')
        self._category: str = options.get('category')
        
        self.playwright = SyncPlaywright(headless=False)
        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        
        self.dones: List[str] = File.read_list_json(self.path_dones)
        self.error: List[str] = File.read_list_json(self.path_err)
        
        ...
        
    def fetch(self, url: str) -> PyQuery:
        req = urllib.request.Request(url, headers=self.headers)
        with urllib.request.urlopen(req) as response:
            response = response.read().decode('utf-8')
            return PyQuery(response)
        
        
    def collect_money(self, html: PyQuery) -> Generator[Tuple[str], any, None]:
        
        def _img_url(text: str) -> str:
            return text.split("url('")[-1].split("');")[0]
        
        ic(len(html.find('div.content-text + div[class="row"] > div > div')))
        for index, card in enumerate(html.find('div.content-text + div[class="row"] > div > div')):
            logger.info(f'INDEX TO [ {index} ]')
            # if 'Detail-Uang-Khusus.aspx?Bahan=Kertas&ID=19' not in PyQuery(card).find('a').attr('href'): continue
            yield _img_url(PyQuery(card).attr('style')), 'https://www.bi.go.id/id/rupiah/gambar-uang/'+PyQuery(card).find('a').attr('href')\
                , PyQuery(card).find('h2').text(), PyQuery(card).find('p').text()
        ...
    def extract_money(self, html: PyQuery, image: str = None) -> Dict[str, any]:
        result: dict = {}
        
        def _history(html: PyQuery) -> Dict[str, any]:
                
            childrens: List[PyQuery] = html.find('div#content-editor > div').children()
            
            if len(childrens) <= 1:  childrens: List[PyQuery] = html.find('div#content-editor > div > div').children()
            if len(childrens) <= 1:  childrens: List[PyQuery] = html.find('div#content-editor > div > div > div').children()
            
            history: dict = {
                "nominal": html.find('div#content-editor > div h2').text() \
                    if html.find('div#content-editor > div h2').text() else html.find('h2.heading-title').text().replace('Histori ', ''),
            }
            
            if not childrens:
                history["description"] = ''
                for text in html.find('#sejarah > div').eq(-1).find('p, div'):
                    if not PyQuery(text).text(): continue
                    history["description"] += PyQuery(text).text()
                    
            _key: str | None = None
            for child in childrens:
                child: PyQuery = PyQuery(child)
                if child.is_('h3'):
                    _key: str = Dekimashita.vdir(child.text())
                    history[_key] = ''
                elif child.text() and _key:
                    history[_key] += child.text()
                    

            return Dekimashita.vdict(history, chars=['\n'])
            ...
            
        def _table(html: PyQuery) -> Dict[str, any]:
            tables = html.find('div#table-sejarah tr')
            table: dict = dict()
            for tr in tables:
                tr: PyQuery = PyQuery(tr)
                table[Dekimashita.vdir(tr.find('td').eq(0).text())] = tr.find('td').eq(1).text()
                
            return table
            ...
            
        def _image(html: PyQuery) -> List[str]:
            images: List[str] = list()
            def process_01(html: PyQuery) -> List[str]:
                urls: List[str] | None = None
                try:
                    _script: str = PyQuery(html.find('div#content > script')[-1]).text()
                    urls = re.findall(r'https?://\S+', _script)
                    urls = [url.rstrip("',") for url in urls]
                except Exception as err:
                    ...
                return urls
                ...
                
            def process_02(html: PyQuery) -> List[str]:
                return list(map(lambda x: PyQuery(x).attr('src'), html.find('#ctl00_ctl54_g_353753b6_6bfa_45c7_a00b_18e9c5c239cd img')))
                ...
                
            if not images: images = process_01(html)
            if not images: images = process_02(html)
            if not images: images = [image]
            
            return images
            ...
            
        result["history"] = _history(html)
        result["table"] = _table(html)
        result["images"] = _image(html)
        
        return result
        ...
        
    def download(self, data: dict, sub_category: str, page: Page) -> str:
        
        urls: List[str] = data["images"]
        def extract_filename(url):
            filename = url.split('/')[-1]
            extention = filename.split('.')[-1]

            return filename, extention
        
        def download_file(url, filename, extention):
            path_image = f'data/data_raw/bank_indonesia/gambar_uang/{sub_category}/{extention}/{filename}'
            
            logger.info(f'DOWNLOAD IMAGE [ {url} ]')
            screenshot_stream = BytesIO()
            response = page.goto(url)
            if response.status != 200 or len(url) <= len('https://www.bi.go.id/Gambar%20Uang/TE2022/360'): raise Exception('err')
            screenshot_stream.write(page.screenshot())
            screenshot_stream.seek(0)
                
            if self.__save:
                File.write_byte(path_image, screenshot_stream.getvalue())
                
            S3.upload(
                body=screenshot_stream.getvalue(),
                destination=path_image,
                send=self.__s3
            )
                
            return path_image
            ...
        paths: List[str] = list()
        for url in urls:
            try:
                filename, extention = extract_filename(url)
                path: str = download_file(url, filename, extention)
                
                paths.append(self.base_path_s3+path)
            except Exception as err:
                logger.error(f'ERROR [ {err} ]')
                data["images"].remove(url)
            
        return paths
    
    def collect_url_items(self, html: PyQuery) -> Generator[Tuple[str], any, None]:
        for div in html.find('div.media-list div.media'):
            div: PyQuery = PyQuery(div)
            yield div.find('a').attr('href')
        ...
        
    def extract_items(self, html: PyQuery) -> Dict[str, any]:
        result: dict = {
            "documents": [self.base_url+PyQuery(a).attr('href') for a in html.find('div#layout-lampiran a')]\
                if html.find('div#layout-lampiran a') else [self.base_url+PyQuery(a).attr('href') for a in html.find('div#layout-sumber-data a')],
            "kontak": html.find('div#layout-kontak .right').text(),
            "title": html.find('h4#layout-title').text(),
            "date": html.find('div#layout-date').text(),
            "last_update": html.find('span#layout-last-update').text(),
            "hits": html.find('div#layout-hits').text().split(':')[-1] if html.find('div#layout-hits').text() else None
        }
        return result
        ...
        
    def curl(self, base_path: str, page_02: Page) -> any:
        paths: List[str] = []
        for button in page_02.query_selector_all('div#layout-lampiran a'):
            path: str = Down.playwright(
                page=page_02,
                loc=button,
                base_desctination=base_path,
                s3=self.__s3,
                save=self.__save
            )
            if path.endswith('zip'):
                paths_docs: List[str] = Zip.unzip_items_zip(
                    source=path,
                    destination=base_path,
                    s3=self.__s3
                )
                paths.extend(list(map(lambda x: self.base_path_s3+x, paths_docs)))
                
            paths.append(self.base_path_s3+path)
        
        return paths
        ...
        
    def data_top(self, page: Page, html: PyQuery, func: any, page_02: Page) -> None:
        _url: str = page.url
        result: dict = {
            "description": html.find('h2#floating-1 + div + div').text()
        }
        
        def _inner_table(_page: Page) -> List[str]:
            values: List[str] = list(map(lambda x: x.get_attribute('value'), _page.query_selector_all('select.custom-select option')))
            paths: List[str] = list()
            for value in values:
                _page.select_option('select.custom-select', value=value)
                sleep(10)
                _page.wait_for_selector('input[value="Unduh"]')
                unduh = _page.query_selector('input[value="Unduh"]')
                path: str = Down.playwright(
                    page=_page,
                    loc=unduh,
                    base_desctination=base_path,
                    s3=self.__s3,
                    save=self.__save
                )
                paths.append(self.base_path_s3+path)
                sleep(5)
                ...
            return paths
            ...
        
        for row in page.query_selector_all('div#accordion div.card'):
            row.query_selector('i.fa-angle-up').click()
            sleep(5)
            sub_category: str = row.query_selector('div.color-blue p').text_content()
            sub_description: str = row.query_selector('div.ms-rtestate-field').text_content() if row.query_selector('div.ms-rtestate-field') else None
            
            title: str = None
            for sub_row in row.query_selector_all('tbody > tr'):
                if sub_row.query_selector('th'):
                    title = sub_row.query_selector('th').text_content()
                    logger.info(f'EXTRACT INFO [ {title} ]')
                else:
                    text: str = sub_row.query_selector('td:nth-child(2)').text_content().replace('\n', '').strip()
                    
                    urls: List[str] = list()
                    paths: List[str] = list()
                    
                    path_json: str = f'data/data_raw/bank_indonesia/{self._category}/{Dekimashita.vdir(sub_category)}/json/{Dekimashita.vdir(text)}.json'
                    base_path: str = f'data/data_raw/bank_indonesia/{self._category}/{Dekimashita.vdir(sub_category)}/'
                    
                    for index, doc in enumerate(sub_row.query_selector_all('a')):
                        urls.append(doc.get_attribute('href') if self.base_url in doc.get_attribute('href') else self.base_url+doc.get_attribute('href'))
                        if '/id/statistik/ekonomi-keuangan/ssp/RTGS-Region.aspx' in doc.get_attribute('href'):
                            page_02.goto(self.base_url+doc.get_attribute('href'))
                            paths.extend(_inner_table(page_02))
                            
                        if not doc.get_attribute('href').endswith('.aspx') or index == 0: 
                            if not doc.get_attribute('href').endswith('.aspx'):
                                path: str = Down.playwright(
                                    page=page,
                                    loc=doc,
                                    base_desctination=base_path,
                                    s3=self.__s3,
                                    save=self.__save
                                )
                                paths.append(self.base_path_s3+path)
                            
                        metadata: dict = func(
                            id=Endecode.md5_hash(text),
                            link=_url,
                            domain='www.bi.go.id',
                            path_json=path_json,
                        )
                        
                        result.update({
                            **metadata,
                            "sub_description": sub_description,
                            "sub_category": sub_category,
                            "text": text,
                            "title": title,
                            "documents": urls,
                            "path_documents": paths
                        })
                        
                        if self.__save:
                            File.write_json(path_json, result)
                        S3.upload_json(
                            body=result,
                            destination=path_json,
                            send=self.__s3
                        )
                ...
            ...
        ...