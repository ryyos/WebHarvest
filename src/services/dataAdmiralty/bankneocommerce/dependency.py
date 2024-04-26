from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic
from time import sleep

from .component import BankneocommerceComponent
from src.drivers import SyncPlaywright

class BankneocommerceLibs(BankneocommerceComponent):
    def __init__(self, options: Dict[str, bool]) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        self.driver = SyncPlaywright(options.get('headless'))
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:
        ps: List[PyQuery] = html.find('p')
        
        name: str = PyQuery(ps.pop(0)).text()
        jabatan: str = PyQuery(ps.pop(0)).text()
        foto: str = html.find('img').attr('src')
        bio: str = ps.text()

        return (name, jabatan, foto, bio)
        ...
        
    def fetch(self, url: str) -> PyQuery:
        try:
            browser = self.driver.start()
            page = browser.new_page()
            page.goto(url)
            page.wait_for_selector('div.pt-20:nth-child(1) > div:nth-child(1)')
            return PyQuery(page.content())
        except Exception as err:
            print(err)
        finally:
            self.driver.close()
        ...

    def extract(self, html: PyQuery) -> Dict[str, any]:
        (name, jabatan, foto, bio) = self.extract_bio(html)
        
        result = {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "link_foto": foto,
            "biografi": bio,
            "riwayat_pencapaian": None,
            "riwayat_pekerjaan":None,
            "organisasi":None,
            "dll":None,
            "riwayat_pendidikan": None,
            "tempat_tanggal_lahir": None,
        }

        return result
        ...