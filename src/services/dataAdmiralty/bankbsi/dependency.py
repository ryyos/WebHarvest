
from ApiRetrys import ApiRetry
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import BankbsiComponent

class BankbsiLibs(BankbsiComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:

        foto: str = html.find('img').attr('src')
        name: str = html.find('h3').text()
        jabatan: str = html.find('h3 + p').text()
        bio: str = html.find('div.description > p').eq(0).text()
        pendidikan: str = '\n'.join([PyQuery(li).text().replace('\n', '') for li in html.find('div.description > ul li')])
        pekerjaan: str = '\n'.join([PyQuery(li).text().replace('\n', '') for li in html.find('div[class="content-more"] > ul > li')])
        dll: str = html.find('div[class="content-more"] > ul + p').text()
        ...

        return (foto, name, jabatan, bio, pendidikan, pekerjaan, dll)

    def extract(self, html: PyQuery) -> None:
        (foto, name, jabatan, bio, pendidikan, pekerjaan, dll) = self.extract_bio(html)
        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "riwayat_pendidikan": pendidikan,
            "riwayat_pekerjaan": pekerjaan,
            "link_foto": foto,
            "biografi": bio,
            "riwayat_pencapaian": None,
            "dll": None if not dll or 'Hubungan Afiliasi' in dll else dll,
            "organisasi": None,
            "tempat_tanggal_lahir": None,
            }
        ...