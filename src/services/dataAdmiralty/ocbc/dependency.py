
from ApiRetrys import ApiRetry
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import OcbcComponent

class OcbcLibs(OcbcComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract_bio(self, html: PyQuery) -> Tuple[str, any, None]:
        pieces: List[PyQuery] = html.find('div[class="ocbc-popup-bod__body__item"]')
        bio: str = PyQuery(pieces[0]).find('p').eq(0).text()

        pekerjaan: str | None = None
        organisasi: str | None = None
        pendidikan: str | None = None
        penghargaan: str | None = None
        dll: str | None = None

        for piece in pieces:

            if 'Riwayat Pekerjaan:' in PyQuery(piece).find('h4').text():
                pekerjaan = '\n'.join([PyQuery(li).text() for li in PyQuery(piece).find('li')])
                if not pekerjaan:
                    pekerjaan = PyQuery(piece).find('p').text()

            if 'Organisasi Nirlaba:' in PyQuery(piece).find('h4').text():
                organisasi = '\n'.join([PyQuery(li).text() for li in PyQuery(piece).find('li')])
                if not organisasi:
                    organisasi = PyQuery(piece).find('p').text()

            if 'Riwayat Pendidikan:' in PyQuery(piece).find('h4').text():
                pendidikan = '\n'.join([PyQuery(li).text() for li in PyQuery(piece).find('li')])
                if not pendidikan:
                    pendidikan = PyQuery(piece).find('p').text()

            if 'Penghargaan:' in PyQuery(piece).find('h4').text():
                penghargaan = '\n'.join([PyQuery(li).text() for li in PyQuery(piece).find('li')])
                if not penghargaan:
                    penghargaan = PyQuery(piece).find('p').text()

            if 'Riwayat Penunjukan' in PyQuery(piece).find('h4').text():
                dll = '\n'.join([PyQuery(li).text() for li in PyQuery(piece).find('li')])
                if not dll:
                    dll = PyQuery(piece).find('p').text()

            ...

        return (bio, pekerjaan, organisasi, pendidikan, penghargaan, dll)
        ...

    def extract(self, html: PyQuery, **kwargs) -> None:
        (bio, pekerjaan, organisasi, pendidikan, penghargaan, dll) = self.extract_bio(html)
        return {
            "nama_lengkap": kwargs.get('name'),
            "nama_jabatan": kwargs.get('jabatan'),
            "riwayat_pendidikan": pendidikan,
            "riwayat_pekerjaan": pekerjaan,
            "link_foto": kwargs.get('img'),
            "biografi": bio,
            "riwayat_pencapaian": penghargaan,
            "dll": dll,
            "organisasi": organisasi,
            "tempat_tanggal_lahir": None,
            }
        ...