import pandas

from ApiRetrys import ApiRetry
from requests import Response
from pyquery import PyQuery
from typing import Generator, List, Dict, Tuple
from icecream import ic
from pandas import DataFrame
from io import BytesIO

from .component import SipsnComponent

class SipsnLibs(SipsnComponent):
    def __init__(self) -> None:
        super().__init__()
        
        self.api = ApiRetry(show_logs=True)
        ...
        
    def generate_prov(self, url: str) -> Generator[Tuple[str], None, None]:
        response: Response = self.api.get(url)
        html: PyQuery = PyQuery(response.text)
        
        for id in html.find('select#filter_id_propinsi > option'):
            yield (PyQuery(id).attr('value'), PyQuery(id).text())
            
    def update_payload(self, id: str) -> Dict[str, any]:
        self.data["id_propinsi"] = id
        return self.data
        ...
        
    def mappings(self, data: Dict[str, any]) -> List[Dict[str, any]]:
        
        result_mappings: List[dict] = []
        for item in data["data"]:
            result_mappings.append({
                "Tahun": item["tahun"],
                "Periode": item["periode"],
                "Provinsi": item["nama_propinsi"],
                "Kabupaten/Kota": item["nama_dati2"],
                "Nama Fasilitas": item["nama"],
                "Jenis": item["jenis"],
                "Status": item["status"],
                "Sampahmasuk (ton/thn)": item["sampah_diterima_tahun"],
                "Sampahmasuk Landfill (ton/thn)": item["sampah_landfill_tahun"],
                "Sampah Organikterolah (ton/thn)": item["organik_tahun"],
                "Sampah An-Organikterolah (ton/thn)": item["anorganik_tahun"],
                "RecoveryPemulung (ton/thn)": item["rp_tahun"],
                "Energi(MW)": item["energi_listrik"],
                "Alamat": item["alamat"],
                "Kelurahan": item["kelurahan"],
                "Kecamatan": item["kecamatan"],
                "Pengelola": item["kelola"],
                "Luas (hektar)": item["luas"],
                "Sistem Operasional": item["sistem_operasional"],
                "Tgl Awal Operasi": item["tgl_awal_operasi"],
                "Tgl. Akhir Operasi": item["tgl_akhir_operasi"],
                "Luas Landfill Aktif (m2)": item["luas_landfill_aktif"],
                "Pencatatan": item["pencatatan"],
                "Jembatan Timbang": item["jembatan_timbang"],
                "Penutupan Sampah Zona Aktif": item["penutupan_sampah_zona_aktif"],
                "Jml Sumur Pantau": item["jml_sumur_pantau"],
                "IPL": item["ada_ipal"],
                "Jml Uji Lindi": item["jml_uji_lindi"],
                "Ada Drainase": item["ada_drainase"],
                "Pemanfaatan Gas Metana": item["pemanfaatan_methan_rev"],
                "Jumlah KK yang memanfaatkan gas Metana": item["jml_kk_manfaat_methan"]
            })
            ...
            
        return result_mappings
        ...
        
    def convert_xlsx(self, datas: List[Dict[str, any]]) -> bytes:
        data_frame: DataFrame = pandas.json_normalize(datas)
        bytes_io = BytesIO()

        data_frame.to_excel(bytes_io, index=False)
        bytes_io.seek(0)
        
        return bytes_io.read()
        ...
