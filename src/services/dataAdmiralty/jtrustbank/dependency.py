
from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import JtrustbankComponent

class JtrustbankLibs(JtrustbankComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:
        right_side = html.find('td').eq(1)
        left_side = html.find('td').eq(0)

        pendidikan: str | None = None
        pekerjaan: str | None = None
        dll: str | None = None
        organisasi: str | None = None
        bio: str | List[str] = []

        name: str = left_side.find('h2').text()
        jabatan: str = left_side.find('h3').text()
        foto: str = self.base_url+left_side.find('div[class="box-photo"] img').attr('src')

        temp: str | None = None
        childrens: List[PyQuery] =  right_side.children()
        for index, child in enumerate(childrens):
            if 'Riwayat Pendidikan' in PyQuery(child).text() and not pendidikan:
                if PyQuery(childrens[index+1]).is_('p'):
                    pendidikan: str = PyQuery(childrens[index+1]).text()
                elif PyQuery(childrens[index+1]).is_('ul'):
                    pendidikan: str = '\n'.join([PyQuery(li).text() for li in PyQuery(childrens[index+1]).find('li')])
            elif 'Riwayat Jabatan:' in PyQuery(child).text() and not pekerjaan:
                if PyQuery(childrens[index+1]).is_('p'):
                    pekerjaan: str = PyQuery(childrens[index+1]).text()
                elif PyQuery(childrens[index+1]).is_('ul'):
                    pekerjaan: str = '\n'.join([PyQuery(li).text() for li in PyQuery(childrens[index+1]).find('li')])
            elif 'Rangkap Jabatan' in PyQuery(child).text() and not dll:
                dll: str = PyQuery(childrens[index+1]).text()
            elif 'Hubungan Afiliasi' in PyQuery(child).text() and not organisasi:
                organisasi: str = PyQuery(childrens[index+1]).text()
            else:
                if PyQuery(child).is_('b'):
                    temp: None = None
                    temp: str = PyQuery(child).text()
                else:
                    if not temp: continue
                    bio.append(f'{temp} {PyQuery(child).text()}')
                    temp: None = None
            ...
        ...

        return (name, jabatan, foto, pendidikan, pekerjaan, dll, organisasi, '\n'.join(bio))

    def extract(self, html: PyQuery) -> Dict[str, any]:
        (name, jabatan, foto, pendidikan, pekerjaan, dll, organisasi, bio) = self.extract_bio(html)
        return {
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "link_foto": foto,
            "biografi": bio,
            "riwayat_pekerjaan": pekerjaan,
            "dll": dll,
            "organisasi": organisasi,
            "riwayat_pendidikan": pendidikan,
            "riwayat_pencapaian": None,
            "tempat_tanggal_lahir": None,
            }
        ...