
from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import VictoriabankComponent

class VictoriabankLibs(VictoriabankComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract(self, html: PyQuery) -> Tuple[str, any, None]:
        
        childrens: List[PyQuery] = html.find('div[class="vismis"]').children()
        ic(len(childrens))
        results: List[dict] = []
        _temp: dict = dict()
        
        for index, child in enumerate(childrens):
            child: PyQuery = PyQuery(child)
            if child.is_('h4') and _temp or index+1 >= len(childrens):
                _res: dict = _temp.copy()
                results.append({
                    "nama_lengkap": _res["name"],
                    "nama_jabatan": _res["jabatan"],
                    "link_foto": self.base_url+_res["foto"],
                    "biografi": '\n'.join(_res["biografi"]),
                    "riwayat_pekerjaan": None,
                    "dll": None,
                    "organisasi": None,
                    "riwayat_pendidikan": None,
                    "riwayat_pencapaian": None,
                    "tempat_tanggal_lahir": None,
                })
                _temp = dict()
            
            if child.is_('h4'):
                _temp['name'] = child.find('strong').text()
                _temp['jabatan'] = child.text().replace(child.find('strong').text(), '')
            elif child.is_('p') and not child.find('img') and child.text():
                if not _temp.get('biografi'):
                    _temp['biografi'] = []
                _temp['biografi'].append(child.text())
            elif child.find('img'):
                _temp['foto'] = child.find('img').attr('src')
                
        return results
        ...