from urllib.parse import urlparse
from ApiRetrys import ApiRetry
from pyquery import PyQuery
from icecream import ic
from typing import Generator, List, Dict, Tuple
from src.utils import File

from .component import BpsPublikasiComponent

class BpsPublikasiLibs(BpsPublikasiComponent):
    def __init__(self) -> None:
        super().__init__()
        
        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...
        
    def get_domain(self, url: str) -> str:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        return domain

    def extract_text(self, html: PyQuery) -> Dict[str, any]:
        
        _base_url = html.find('#nav > li:nth-child(1) > a').attr('href') +'/'
        result: dict = {
            "title": html.find('h4.judulberita').text(),
            "thumbnail": _base_url + html.find('h4.judulberita + div img').attr('src'),
            "url_document": _base_url + html.find('div#PopTriger').attr('data-url')
        }
        pieces: List[str] = html.find('div.nomor-identitas').text().split('\n')
        
        for piece in pieces:
            key, value = piece.split(':')
            result[key.strip()] = value.strip()
            
        return result
        ...