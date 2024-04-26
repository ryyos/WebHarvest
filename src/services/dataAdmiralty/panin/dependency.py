from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic
from time import sleep

from .component import PaninComponent

class PaninLibs(PaninComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract_bio(self, card: PyQuery, popup: PyQuery) -> Tuple[str, any, None]:
        result: dict = {}
        childrens: List[PyQuery] = popup.find('.panin-points-popup__teks').children()
        for child in childrens:
            child: PyQuery = PyQuery(child)
            if child.find('strong'):
                if child.next().is_('p'):
                    result[child.find('strong').text()] = child.next().text()
                elif child.next().is_('ul'):
                    result[child.find('strong').text()] = '\n'.join(list(map(lambda x: PyQuery(x).text(), child.next().find('li'))))
        name: str = card.find('h4').text()
        jabatan: str = card.find('h6').text()
        foto: str = self.base_url+popup.find('img').attr('src')
        bio: str = result.get("Warga Negara")
        pendidikan: str = result.get("Riwayat Pendidikan")
        kerja: str = result.get("Pengalaman Kerja")
        return (name, jabatan, foto, bio, pendidikan, kerja)
        ...

    def extract(self, card: PyQuery, popup: PyQuery) -> Dict[str, any]:
        (name, jabatan, foto, bio, pendidikan, kerja) = self.extract_bio(card, popup)
        
        result = {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "link_foto": foto,
            "biografi": bio,
            "riwayat_pendidikan": pendidikan,
            "riwayat_pekerjaan":kerja,
            "riwayat_pencapaian": None,
            "organisasi":None,
            "dll":None,
            "tempat_tanggal_lahir": None,
        }

        return result
        ...