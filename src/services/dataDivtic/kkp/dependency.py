import json
import re

from requests import Response
from dekimashita import Dekimashita
from ApiRetrys import ApiRetry
from pyquery import PyQuery
from icecream import ic
from typing import List, Dict, Generator, Tuple

from src.utils import File
from .component import KkpComponent

class KkpLibs(KkpComponent):
    def __init__(self) -> None:
        super().__init__()
        
        self.api = ApiRetry(show_logs=True)
        ...
        
    def get_nilai_tukar(self, html: PyQuery) -> Dict[str, any]:
        script: str = html.find('script[type="text/javascript"]').eq(0).text()
        pieces: str = script.split('config_nilai_tukar = ')[1].split(';')[0]
        
        parent_keys: List[str] = eval(pieces.split('labels: ')[-1].split(']')[0]+']')
        
        kid_key_01: str = Dekimashita.vdir(pieces.split('label: ')[1].split(',')[0].replace("'", ''))
        kid_key_02: str = Dekimashita.vdir(pieces.split('label: ')[2].split(',')[0].replace("'", ''))
        
        values_01: List[str] = eval(pieces.split('data: ')[2].split(']')[0]+']')
        values_02: List[str] = eval(pieces.split('data: ')[3].split(']')[0]+']')
        
        result: dict = {
            "category": 'Nilai Tukar',
            "data": dict(),
            "label": 'nilai tukar nelayan dan penukaran ikan'
        }
        for parent, value_01, value_02 in zip(parent_keys, values_01, values_02):
            result["data"][parent] = {
                kid_key_01: value_01,
                kid_key_02: value_02
            }
            
        return result
        ...
        
    def get_pdb(self, html: PyQuery) -> Dict[str, any]:
        script: str = html.find('script[type="text/javascript"]').eq(0).text()
        pieces: str = script.split('config_pdb = ')[1].split(';')[0]
        
        keys: List[str] = eval(pieces.split('labels: ')[-1].split(']')[0]+']')
        values: List[str] = eval(pieces.split('data: ')[-1].split(']')[0]+']')
        label: str = 'Perkembangan PDB Perikanan (Rp. Miliar)'
        
        result: dict = {
            "category": 'PDB',
            "label": label,
            "data": dict()
        }
        
        for key, value in zip(keys, values):
            result["data"][key] = value
            
        return result
    
    def get_aki(self, html: PyQuery) -> Dict[str, any]:
        script: str = html.find('script[type="text/javascript"]').eq(0).text()
        pieces: str = script.split('config_aki = ')[1].split(';')[0]
        
        keys: List[str] = eval(pieces.split('labels: ')[-1].split(']')[0]+']')
        values: List[str] = eval(pieces.split('data: ')[-1].split(']')[0]+']')
        label: str = pieces.split('label: ')[-1].split(',')[0].replace("'", '')
        
        result: dict = {
            "category": 'Angka Konsumsi Ikan ',
            "label": label,
            "data": dict()
        }
        
        for key, value in zip(keys, values):
            result["data"][key] = value
            
        return result
        ...
        
    def get_ekspor(self, html: PyQuery) -> Dict[str, any]:
        script: str = html.find('script[type="text/javascript"]').eq(0).text()
        pieces: str = script.split('config_export = ')[1].split(';')[0]
        
        keys: List[str] = eval(pieces.split('labels: ')[-1].split(']')[0]+']')
        values: List[str] = eval(pieces.split('data: ')[-1].split(']')[0]+']')
        label: str = pieces.split('label: ')[-1].split(',')[0].replace("'", '')
        
        result: dict = {
            "category": 'Nilai Ekspor',
            "label": label,
            "data": dict()
        }
        
        for key, value in zip(keys, values):
            result["data"][key] = value
            
        return result
        ...
    
    def collect_categories(self, html: PyQuery) -> Generator[str, any, None]:
        for side in html.find('ul.nav-stacked > li a'):
            yield (PyQuery(side).text(), self.base_static_url+PyQuery(side).attr('href'))
        ...
        
    def collect_sub_categories(self, html: PyQuery) -> List[Tuple[str, str]]:
        subs: List[tuple] = list()
        for li in html.find('#dl_data_statis a'):
            subs.append((PyQuery(li).text(), Dekimashita.vnum(PyQuery(li).attr('onclick'))))
            
        return subs
        ...
        
    def get_endpoint(self, html: PyQuery) -> str:
        return self.base_static_url+html.find('script[type="text/javascript"]').text().split("url: '")[1].split("'")[0]
    
    def get_jtb_potensi(self, html: PyQuery) -> List[Tuple[str, str]]:
        potensis: List[tuple] = list()
        kepmens = list(map(lambda x: PyQuery(x).text(), html.find('select#kepmen > option')))
        
        for kepmen in kepmens:
            self.jtb_payload["kepmen"] = kepmen
            response: Response = self.api.post(self.jtb_url, data=self.jtb_payload, headers=self.header)
            potensis.append((kepmen.replace(' ', '_'), response.json()[0]))
            
        return potensis
        ...
        
    def get_angka_konsumsi_ikan(self) -> List[Tuple[str, str]]:
        response: Response = self.api.post(self.aki_url, data=self.angka_konsumsi_ikan_payload, headers=self.header)
        return [('Angka_Konsumsi_Ikan_(AKI)', response.json()[0])]
        ...
        
    def get_iku_kkp(self, html: PyQuery) -> List[Tuple[str, str]]:
        potensis: List[tuple] = list()
        kepmens = list(map(lambda x: PyQuery(x).text(), html.find('select#jns_iku > option')))
        
        for kepmen in kepmens[1:]:
            self.iku_kkp_payload["jns_iku_val"] = kepmen
            response: Response = self.api.post(self.search_aku, data=self.iku_kkp_payload, headers=self.header)
            potensis.append((kepmen.replace(' ', '_'), response.json()[0]))
            
        return potensis
        ...
        
    def get_unit_pengolahan_ikan(self, html: PyQuery) -> List[Tuple[str, str]]:
        response: Response = self.api.post(self.unit_pengolahan_ikan_url, data=self.unit_pengolahan_ikan_payload, headers=self.header)
        return [('Unit_Pengolahan_Ikan_(UPI)_Provinsi', response.json()[0])]
        
    def get_jadwal_rilis(self, html: PyQuery) -> List[Tuple[str, str]]:
        return [('Publikasi_KKP_2023', html.find('table').html())]
    
    def get_publikasi(self, html: PyQuery) -> List[Tuple[str, str]]:
        trs: List[PyQuery] = html.find('table tr')
        results: List[dict] = []
        for tr in trs[1:]:
            tr: PyQuery = PyQuery(tr)
            results.append({
                "gambar": 'https://statistik.kkp.go.id'+tr.find('td').eq(0).find('img').attr('src'),
                "tahun": tr.find('td').eq(1).text(),
                "judul": tr.find('td').eq(2).text(),
                "deskripsi": tr.find('td').eq(3).text(),
                "link": 'https://statistik.kkp.go.id'+tr.find('td').eq(4).find('a').attr('href')[1:]
            })
            ...
        return [('Publikasi', results)]
        ...
        
    def get_deskripsi(self, html: PyQuery) -> List[Tuple[str, str]]:
        trs: List[PyQuery] = html.find('table tr')
        results: List[dict] = []
        for tr in trs:
            tr: PyQuery = PyQuery(tr)
            results.append({
                tr.find('td').eq(0).text(): tr.find('td').eq(-1).text()
            })
        
        return [('Konsep_dan_Definisi', results)]