from ApiRetrys import ApiRetry
from dekimashita import Dekimashita
from requests import Response
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic
from time import sleep

from .component import QnbComponent

class QnbLibs(QnbComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True, defaulth_headers=True)
        ...

    def extract_bio(self, html: PyQuery) -> List[str]:
        elements: List[PyQuery] = html.find('section[data-portal-component-type="text"] figure, section[data-portal-component-type="text"] figure ~ p, section[data-portal-component-type="text"] figure ~ h4')
        
        results: List[str] = []
        temp: List[str] = []

        ic(len(elements))

        for index, element in enumerate(elements):
            if PyQuery(element).is_('figure'):
                if temp: 
                    temp_copy = temp.copy()
                    results.append(temp_copy)
                temp.clear()
                temp.append(PyQuery(element).find('img').attr('src'))
            elif PyQuery(element).is_('h4') or PyQuery(element).is_('p'):
                temp.append(PyQuery(element).text())

            if index+1 == len(elements):
                temp_copy = temp.copy()
                results.append(temp)

        return results
        ...

    def extract(self, html: PyQuery) -> List[Dict[str, any]]:
        list_elements: List[List[str]] = self.extract_bio(html)
        results: List[dict] = []
        for elements in list_elements:
            results.append({
                "nama_lengkap": elements[1].split('\n')[0],
                "nama_jabatan": elements[1].split('\n')[-1],
                "link_foto": self.base_url+elements[0],
                "biografi": elements[2],
                "riwayat_pencapaian": elements[3],
                "riwayat_pekerjaan": elements[4],
                "organisasi": elements[-1] if elements[-1] else elements[-2],
                "dll": '\n'.join(elements[5:-2]) if '\n'.join(elements[5:-2]) else None,
                "riwayat_pendidikan": None,
                "tempat_tanggal_lahir": None,
            })

        return results
        ...