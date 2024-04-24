
from pyquery import PyQuery
from ApiRetrys import ApiRetry
from typing import Dict
from .component import AhugoidComponent

class AhugoidLibs(AhugoidComponent):
    def __init__(self) -> None:
        super().__init__()
        
        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...
        
    def build_param(self, page: str, keyword: str, recaptcha: str) -> Dict[str, str]:
        return {
            "nama": keyword,
            "tipe": "perseroan",
            "page": page,
            "g-recaptcha-response": recaptcha
        }
        ...
        
    def extract(self, html: PyQuery) -> Dict[str, any]:
        return {
            "name": html.find('strong.judul').text(),
            "alamat": html.find('div.alamat').text(),
            "kabuten_provinsi": html.find('div.kabpro').text(),
            "telphone": html.find('div.telp').text()
        }
        ...
        