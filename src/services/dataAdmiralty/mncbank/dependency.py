
from requests import Response
from ApiRetrys import ApiRetry
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import MncbankComponent

class MncbankLibs(MncbankComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:
        pendidikan: str = html.find('div[class="txt-vision"] + div').eq(0).text()
        pencapaian: str = html.find('div[class="txt-vision"] + div').eq(1).text()
        pekerjaan: str = html.find('div[class="txt-vision"] + div').eq(1).text()
        ...

        return (pendidikan, pekerjaan, pencapaian)

    def extract(self, data: Dict[str, any]) -> None:
        (pendidikan, pekerjaan, pencapaian) = self.extract_bio(PyQuery(data["contents"][0]["content"]))

        return {
            "nama_lengkap": data["meta_title"],
            "nama_jabatan": data["contents"][0]["summary"].split(',')[0],
            "riwayat_pendidikan": pendidikan,
            "riwayat_pekerjaan": pekerjaan,
            "link_foto": self.base_url+data["image_lg"],
            "biografi": data["contents"][0]["summary"].split(',')[-1],
            "riwayat_pencapaian": pencapaian,
            "dll": None,
            "organisasi": None,
            "tempat_tanggal_lahir": None,
            }
        ...