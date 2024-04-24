
from ApiRetrys import ApiRetry
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import BtpnComponent

class BtpnLibs(BtpnComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:

        top: PyQuery = html.find('div.row')
        foto: str = top.find('img').attr('src')
        name: str = top.find('p').eq(0).text()
        jabatan: str = top.find('p').eq(-1).text()
        bio: str = html.find('div.modal-body > p').eq(0).text()
        pekerjaan: str = html.find('div.modal-body > p').text().replace(bio, '')

        return (foto, name, jabatan, bio, pekerjaan)
        ...

    def extract(self, html: PyQuery) -> None:
        (foto, name, jabatan, bio, pekerjaan) = self.extract_bio(html)
        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "riwayat_pendidikan": None,
            "link_foto": self.base_url+foto,
            "biografi": bio,
            "riwayat_pekerjaan": pekerjaan,
            "riwayat_pencapaian": None,
            "dll": None,
            "organisasi": None,
            "tempat_tanggal_lahir": None,
            }
        ...