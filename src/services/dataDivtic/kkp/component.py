import settings

class KkpComponent:
    def __init__(self) -> None:
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        
        self.home_url = 'https://satudata.kkp.go.id/'
        self.statistic_url = 'https://statistik.kkp.go.id/home.php'
        self.base_static_url = 'https://statistik.kkp.go.id/'
        
        self.jtb_url = 'https://statistik.kkp.go.id/service/search_sdi.php'
        self.aki_url = 'https://statistik.kkp.go.id/service/search_aki.php'
        self.search_aku = 'https://statistik.kkp.go.id/service/search_iku.php'
        self.unit_pengolahan_ikan_url = 'https://statistik.kkp.go.id/service/search_upi_new.php'
        
        self.header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://statistik.kkp.go.id',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }
        
        self.unit_pengolahan_ikan_payload = {
            'skala_usaha_val[]': [
                'Menengah Besar',
                'Mikro Kecil',
            ],
            'provinsi_val[]': [
                'ACEH',
                'BALI',
                'BANTEN',
                'BENGKULU',
                'DAERAH ISTIMEWA YOGYAKARTA',
                'DKI JAKARTA',
                'GORONTALO',
                'JAMBI',
                'JAWA BARAT',
                'JAWA TENGAH',
                'JAWA TIMUR',
                'KALIMANTAN BARAT',
                'KALIMANTAN SELATAN',
                'KALIMANTAN TENGAH',
                'KALIMANTAN TIMUR',
                'KALIMANTAN UTARA',
                'KEPULAUAN BANGKA BELITUNG',
                'KEPULAUAN RIAU',
                'LAMPUNG',
                'MALUKU',
                'MALUKU UTARA',
                'NUSA TENGGARA BARAT',
                'NUSA TENGGARA TIMUR',
                'PAPUA',
                'PAPUA BARAT',
                'RIAU',
                'SULAWESI BARAT',
                'SULAWESI SELATAN',
                'SULAWESI TENGAH',
                'SULAWESI TENGGARA',
                'SULAWESI UTARA',
                'SUMATERA BARAT',
                'SUMATERA SELATAN',
                'SUMATERA UTARA',
            ],
            'tahun_val[]': [
                '2018',
                '2019',
            ],
        }

        
        self.iku_kkp_payload = {
            'jns_iku_val': 'ANGKA KONSUMSI IKAN',
            'tahun_val[]': [
                '2010',
                '2011',
                '2012',
                '2013',
                '2014',
                '2015',
                '2016',
                '2017',
                '2018',
                '2019',
                '2020',
                '2021',
                '2022',
                '2023',
                '2024',
            ],
            'triwulan_val[]': [
                '0',
                '1',
                '2',
                '3',
                '4',
            ],
        }
        
        self.angka_konsumsi_ikan_payload = {
            'tahun_val[]': [
                '2010',
                '2011',
                '2012',
                '2013',
                '2014',
                '2015',
                '2016',
                '2017',
                '2018',
                '2019',
                '2020',
                '2021',
                '2022',
            ],
            'prov_val[]': [
                'ACEH',
                'BALI',
                'BANTEN',
                'BENGKULU',
                'DAERAH ISTIMEWA YOGYAKARTA',
                'DKI JAKARTA',
                'GORONTALO',
                'JAMBI',
                'JAWA BARAT',
                'JAWA TENGAH',
                'JAWA TIMUR',
                'KALIMANTAN BARAT',
                'KALIMANTAN SELATAN',
                'KALIMANTAN TENGAH',
                'KALIMANTAN TIMUR',
                'KALIMANTAN UTARA',
                'KEPULAUAN BANGKA BELITUNG',
                'KEPULAUAN RIAU',
                'LAMPUNG',
                'MALUKU',
                'MALUKU UTARA',
                'NASIONAL',
                'NUSA TENGGARA BARAT',
                'NUSA TENGGARA TIMUR',
                'PAPUA',
                'PAPUA BARAT',
                'RIAU',
                'SULAWESI BARAT',
                'SULAWESI SELATAN',
                'SULAWESI TENGAH',
                'SULAWESI TENGGARA',
                'SULAWESI UTARA',
                'SUMATERA BARAT',
                'SUMATERA SELATAN',
                'SUMATERA UTARA',
            ],
        }
                
        self.jtb_payload = {
            'jns_wpp_val[]': [
                'WPP 571',
                'WPP 572',
                'WPP 573',
                'WPP 711',
                'WPP 712',
                'WPP 713',
                'WPP 714',
                'WPP 715',
                'WPP 716',
                'WPP 717',
                'WPP 718',
            ],
            'jns_kelompok_val[]': [
                'Cumi-cumi',
                'Ikan Demersal',
                'Ikan Karang',
                'Ikan Pelagis Besar',
                'Ikan Pelagis Kecil',
                'Kepiting',
                'Lobster',
                'Rajungan',
                'Udang Penaeid',
            ],
            'kepmen': 'Kepmen KP 50/2017',
        }
        ...