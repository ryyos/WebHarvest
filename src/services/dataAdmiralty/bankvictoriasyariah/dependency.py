
from ApiRetrys import ApiRetry
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic
from dekimashita import Dekimashita

from .component import BankvictoriasyariahComponent

class BankvictoriasyariahLibs(BankvictoriasyariahComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract(self, html: PyQuery) -> List[Dict[str, any]]:
        results: List[dict] = []
        ps: List[dict] = []
        childrens: List[PyQuery] = html.find('div.fl').children()
        
        data: dict = {
            "nama_lengkap": None,
            "nama_jabatan": None,
            "riwayat_pendidikan": None,
            "link_foto": None,
            "biografi": [],
            "riwayat_pekerjaan": None,
            "riwayat_pencapaian": None,
            "dll": None,
            "organisasi": None,
            "tempat_tanggal_lahir": None,
        }
        
        for index, child in enumerate(childrens):
            child: PyQuery = PyQuery(child)
            
            if child.is_('h2') or index == len(childrens)-1:
                if data["nama_jabatan"] is not None: 
                    data["biografi"] = ' '.join(ps.copy()).strip()
                    ps.clear()
                    results.append(data.copy())
                data["nama_jabatan"] = child.text().split('-')[-1] if '-' in child.text() else child.text().split('–')[-1]
                data["nama_lengkap"] = child.text().split('-')[0] if '-' in child.text() else child.text().split('–')[0]
                
            if child.find('img'):
                data["link_foto"] = child.find('img').attr('src')
                
            if child.is_('p') and child.text() is not None:
                ps.append(child.text())
                
        
        return results
        ...