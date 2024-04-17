
from typing import List, Dict
from ApiRetrys import ApiRetry
from pyquery import PyQuery
from icecream import ic

from .component import UobComponent
from src.utils import split_list

class UobLibs(UobComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract(self, html: PyQuery) -> List[Dict[str, str]]:
        results: List[dict] = []

        all_profiles: List[PyQuery] = html.find('div.free-text tbody > tr')
        profile_pieces: List[List[PyQuery]] = split_list(
            datas=all_profiles,
            length_each=3
        )

        for profile in profile_pieces:
            name: str = PyQuery(profile[0]).find('strong').eq(-1).text()
            ic(name)
            jabatan: str = PyQuery(profile[0]).find('strong').eq(0).text()
            foto: str = PyQuery(profile).find('img').attr('src')

            descriptions: List[PyQuery] = PyQuery(profile[1]).find('td').eq(-1).find('p')
            bio: str = PyQuery(descriptions.pop(0)).text()
            pencapaian: str = PyQuery(descriptions.pop(-1)).text()

            pengalaman_kerja: str = '\n'.join([PyQuery(p).text() for p in descriptions])

            results.append({
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "riwayat_pekerjaan": pengalaman_kerja,
            "link_foto": self.base_url+foto,
            "biografi": bio,
            "riwayat_pencapaian": pencapaian,
            "riwayat_pendidikan": None,
            "dll": None,
            "organisasi": None,
            "tempat_tanggal_lahir": None,
            })
            ...

        return results
        ...