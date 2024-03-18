
from icecream import ic
from requests import Response
from typing import Dict, Tuple, List
from pyquery import PyQuery
from ApiRetrys import ApiRetry

from .component import MayBankComponent

class MayBankLibs(MayBankComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:
        childrens: List[PyQuery] = html.find('div[class="col-lg-8 col-md-6 col-sd-6 col-xd-12"]').children()

        pendidikan_found = False
        pencapaian_found = False
        pengalaman_kerja_found = False
        dll_found = False

        pendidikan: str | None = None
        pencapaian: str | None = None
        pengalaman_kerja: str | None = None
        dll: str | None = None

        name: str = html.find('div.container h2').text()
        jabatan: str = PyQuery(html.find('div.container strong')[0]).text()
        foto: str = html.find('div[style="text-align: center;"] img').attr('src')
        bio: str = PyQuery(html.find('div[class="col-lg-8 col-md-6 col-sd-6 col-xd-12"] p')[1]).text()

        if name == jabatan:
            jabatan: str = PyQuery(html.find('div.container strong')[1]).text()

        for child in childrens:

            if 'Riwayat Pendidikan'.lower() in PyQuery(child).text().lower():
                pendidikan_found = True
            elif PyQuery(child).is_('p') and pendidikan_found:
                pendidikan: str = PyQuery(child).text()
                pendidikan_found = False
            elif PyQuery(child).is_('ul') and pendidikan_found:
                pendidikan: str = '\n'.join([PyQuery(li).text() for li in PyQuery(child).find('li')])
                pendidikan_found = False
                ...

            if 'Dasar Hukum Penunjukan'.lower() in PyQuery(child).text().lower():
                pencapaian_found = True
            elif pencapaian_found:
                pencapaian: str = PyQuery(child).text()
                pencapaian_found = False
                ...

            if 'Pengalaman Kerja'.lower() in PyQuery(child).text().lower():
                pengalaman_kerja_found = True
            elif pengalaman_kerja_found:
                pengalaman_kerja: str = '\n'.join([PyQuery(li).text() for li in PyQuery(child).find('li')])
                pengalaman_kerja_found = False
                ...

            if 'Jabatan Rangkap'.lower() in PyQuery(child).text().lower():
                dll_found = True
            elif dll_found:
                dll: str = PyQuery(child).text()
                dll_found = False
                ...

        return (name, bio, jabatan, foto, pendidikan, pencapaian, pengalaman_kerja, dll)
        ...

    def extract(self, url: str, target: str) -> Dict[str, any]:
        response: Response = self.api.get(url)
        html = PyQuery(response.text)

        (name, bio, jabatan, foto, pendidikan, pencapaian, pengalaman_kerja, dll) = self.extract_bio(html)

        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "riwayat_pendidikan": pendidikan,
            "riwayat_pekerjaan": pengalaman_kerja,
            "link_foto": target+foto,
            "biografi": bio,
            "riwayat_pencapaian": pencapaian,
            "dll": dll,
            "organisasi": None,
            "tempat_tanggal_lahir": None,
            }
        ...