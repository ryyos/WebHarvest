
from ApiRetrys import ApiRetry
from typing import List, Dict, Tuple
from pyquery import PyQuery
from icecream import ic

from .component import ArthagrahaComponent

class ArthagrahaLibs(ArthagrahaComponent):
    def __init__(self) -> None:
        super().__init__()

        self.api = ApiRetry(show_logs=True)
        ...

    def divide_profil(self, html: PyQuery) -> List[PyQuery]:

        profiles: List[List[PyQuery]] = []

        component_p: List[PyQuery] = []
        ps: List[PyQuery] = html.find('div[class="col-lg-9 col-md-9 col-sm-12 col-xs-12 float-right blog-content"] > p')
        if not ps: 
            ps: List[PyQuery] = html.find('article > p')

        for index, p in enumerate(ps):
            if PyQuery(p).find('img'):
                if component_p:
                    profiles.append(component_p)
                component_p = []

            if PyQuery(p).is_('p'):
                component_p.append(PyQuery(p))
                
            if index+1 == len(ps):
                profiles.append(component_p)
            ...

        return profiles
        ...

    def extract(self, html: PyQuery) -> List[Dict[str, any]]:
        profiles: List[List[PyQuery]] = self.divide_profil(html)
        results: List[dict] = []

        for profile in profiles:
            
            trash: PyQuery = PyQuery(profile.pop(0))
            foto: str = trash.find('img').attr('src')

            jabatan: str | None = None
            name: str | None = None

            if trash.find('strong') and '\n' in trash.find('strong').text():
                name: str = trash.find('strong').text().split('\n')[0]
                jabatan: str = trash.find('strong').text().split('\n')[-1]
            
            elif trash.find('strong'):
                name: str = trash.find('strong').text()

            if not name:
                name: str = PyQuery(profile.pop(0)).text()
                if not name:
                    name: str = PyQuery(profile.pop(0)).text()

            if not jabatan:
                jabatan: str = PyQuery(profile.pop(0)).text()

            bio: str = '\n'.join([PyQuery(p).text() for p in profile if PyQuery(p).text()])
            
            results.append({
            "nama_lengkap": name,
            "nama_jabatan": jabatan,
            "link_foto": foto,
            "biografi": bio,
            "riwayat_pekerjaan": None,
            "riwayat_pencapaian": None,
            "dll": None,
            "organisasi": None,
            "riwayat_pendidikan": None,
            "tempat_tanggal_lahir": None,
            })
            ...

        return results
        ...