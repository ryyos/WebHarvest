
from ApiRetrys import ApiRetry
from requests import Response
from pyquery import PyQuery
from typing import List, Dict
from dekimashita import Dekimashita

from .component import DephubComponent

class  DephubLibs(DephubComponent):
    def __init__(self) -> None:
        super().__init__()
        
        self.api = ApiRetry(show_logs=True)
        ...
        
    def get_list_table(self, url: str) -> List[Dict[str, any]]:
        response: Response = self.api.get(url, headers=self.headers, cookies=self.cookies)
        return response.json()["data"]
        ...
    def get_profile(self, html: PyQuery) -> Dict[str, any]:
        childrens: List[PyQuery] = html.find('ul.products-list li').children()
        temp: dict = {
            "name": html.find('ul.products-list li').find('a').text(),
            "provinsi": html.find('ul.products-list li').text().split('\n')[1]
        }
        for child in childrens:
            child: PyQuery = PyQuery(child)
            if child.is_('strong'):
                if child.next().is_('p') or child.next().is_('span'):
                    temp.update({
                        Dekimashita.vdir(child.text()): child.next().text()
                    })
            ...
        return temp
        ...
        
    def get_working_area(self, html: PyQuery) -> List[Dict[str, any]]:
        _temp: List[dict] = []
        for card in html.find('div.card_body > div.row > div'):
            card: PyQuery = PyQuery(card)
            _temp.append({
                "desa_kecamatan": card.find('h4').text(),
                "nc": card.text().split('NC:')[-1].split(' ')[0],
                "address": card.find('address').text().split('\n')[0],
                "long": card.find('address').text().split('\n')[-2].split(',')[0],
                "lat": card.find('address').text().split('\n')[-2].split(',')[-1],
            })
            ...
        ...
        
    def get_hirarki_pelabuhan(self, html: PyQuery) -> List[Dict[str, any]]:
        _temp: List[dict] = []
        for card in html.find('div#timeline > div.row > div'):
            card: PyQuery = PyQuery(card)
            _temp.append({
                "tahun": int(Dekimashita.vnum(card.find('h4').text())),
                "code": card.text().replace(card.find('h4').text(), '').strip(),
            })
            ...
        ...
        return _temp
        ...