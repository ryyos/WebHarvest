
from ApiRetrys import ApiRetry
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import BankmegaComponent

class BankmegaLibs(BankmegaComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def sorter(self, html: PyQuery) -> Tuple[List[PyQuery], any, None]:
        persons: List[PyQuery] = html.find('div[class="container-fluid"] > div')

        all_direksi: List[PyQuery] = []
        all_komisaris: List[PyQuery] = []
        for person in persons:
            if 'direktur' in PyQuery(person).find('h4').text().lower(): all_direksi.append(person)
            if 'komisaris' in PyQuery(person).find('h4').text().lower(): all_komisaris.append(person)

        return (all_direksi, all_komisaris)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:

        foto: str = html.find('img').attr('src')
        name: str = html.find('h3').text()
        jabatan: str = html.find('h4').text()
        bio: str = html.find('h4 + p').text()
        pendidikan: str = html.find('h4 + p + p').text()
        pekerjaan: str = \
        '\n'.join([PyQuery(ul).text().replace('\n', '') for ul in html.find('ul').eq(0).find('li')]) if name != 'Chairul Tanjung' else \
        '\n'.join([PyQuery(ul).text().replace('\n', '') for ul in html.find('ul').eq(-1).find('li')])
        dll: str = html.find('p').eq(-1).text()

        if not pekerjaan:
            pekerjaan: str = '\n'.join([PyQuery(tr).find('td').eq(0).text().replace('\n', '')+': '+PyQuery(tr).find('td').eq(-1).text().replace('\n', '') for tr in html.find('table tr')])

        return (foto, name, jabatan, bio, pendidikan, pekerjaan, dll)
        ...

    def extract(self, html: PyQuery) -> None:
        (foto, name, jabatan, bio, pendidikan, pekerjaan, dll) = self.extract_bio(html)
        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "riwayat_pendidikan": pendidikan,
            "riwayat_pekerjaan": pekerjaan,
            "link_foto": self.base_url+foto,
            "biografi": bio,
            "riwayat_pencapaian": None,
            "dll": dll,
            "organisasi": None,
            "tempat_tanggal_lahir": None,
            }
        ...