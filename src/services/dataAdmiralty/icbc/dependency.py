from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import IcbcComponent

class IcbcLibs(IcbcComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True)
        ...

    def sorter_div(self, html: PyQuery) -> List[PyQuery]:
        
        divs: List[PyQuery] = []
        for div in html.find('tr:last-child td:first-child div[align="center"]'):
            if PyQuery(div).find('strong'):
                divs.append(PyQuery(div))
        
        return divs
        ...
    def special(self, html: PyQuery) -> Tuple[str, any, None]:
        text: str = html.find('tr:last-child td:last-child > p').text()

        pieces: List[str] = text.split('\n')

        bio: str = pieces[1].split('\n')[-1]
        pendidikan: str = pieces[4].split('\n')[-1]
        pekerjaan: str = pieces[-1].split('\n')[-1]

        return (bio, pendidikan, pekerjaan)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:
        contents: PyQuery = html.find('tr:last-child td:last-child > p')
        if len(contents) <= 1:
            return self.special(html)

        bio: str = PyQuery(contents.pop(0)).text().split('\n')[-1]
        pendidikan: str = PyQuery(contents.pop(0)).text().split('\n')[-1]
        pekerjaan: str = '\n'.join([PyQuery(p).text() for p in contents])

        return (bio, pendidikan, pekerjaan)
        ...

    def extract(self, html: PyQuery) -> Dict[str, any]:

        divs: List[PyQuery] = self.sorter_div(html)
        (bio, pendidikan, pekerjaan) = self.extract_bio(html)

        return {
            "nama_lengkap": divs[-1].text().split('\n')[0],
            "nama_jabatan": divs[-1].text().split('\n')[-1],
            "link_foto": 'https:'+html.find('img').attr('src'),
            "biografi": bio,
            "riwayat_pekerjaan": pekerjaan,
            "riwayat_pencapaian": pendidikan,
            "dll": None,
            "organisasi": None,
            "riwayat_pendidikan": None,
            "tempat_tanggal_lahir": None,
            }
        ...