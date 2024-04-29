import settings
class DephubComponent:
    def __init__(self) -> None:
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        
        self.domain = 'simpel.dephub.go.id'
        self.base_url = 'https://simpel.dephub.go.id'
        self.row_url = 'https://simpel.dephub.go.id/index.php/outerapp/pageinfo/92c7b0031b935ca78d4891c6c08d657b/'
        self.target_url = 'https://simpel.dephub.go.id/index.php/front/service/9cdb33b45a1d1128dacbb756773a7a24/grid'
        
        self.url_dataDermaga = 'https://simpel.dephub.go.id/index.php/front/service/0cac347133ddf8ad24d160ba45e436d0/dataDermaga/'
        self.url_getTrestle = 'https://simpel.dephub.go.id/index.php/front/service/0cac347133ddf8ad24d160ba45e436d0/getTrestle/'
        self.url_getCauseway = 'https://simpel.dephub.go.id/index.php/front/service/0cac347133ddf8ad24d160ba45e436d0/getCauseway/'
        self.fasilitas_cookies = {
            'simpelsess': 'ufje9kf7erc6tui6g3hlthdbudpi9h1i',
        }
        
        self.cookies = {
            'simpelsess': 'cglvg4q9613kqtceronpjfgion103odh',
        }
        

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://simpel.dephub.go.id',
            'Connection': 'keep-alive',
            # 'Referer': 'https://simpel.dephub.go.id/index.php/front',
            # 'Cookie': 'simpelsess=cglvg4q9613kqtceronpjfgion103odh',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }
        
        self.data = {
            'draw': '1',
            'columns[0][data]': 'IDpel',
            'columns[0][name]': 'IDpel',
            'columns[0][searchable]': 'true',
            'columns[0][orderable]': 'true',
            'columns[0][search][value]': '',
            'columns[0][search][regex]': 'false',
            'columns[1][data]': 'kode_pelabuhan',
            'columns[1][name]': 'kode_pelabuhan',
            'columns[1][searchable]': 'true',
            'columns[1][orderable]': 'true',
            'columns[1][search][value]': '',
            'columns[1][search][regex]': 'false',
            'columns[2][data]': 'nama_pelabuhan',
            'columns[2][name]': 'nama_pelabuhan',
            'columns[2][searchable]': 'true',
            'columns[2][orderable]': 'true',
            'columns[2][search][value]': '',
            'columns[2][search][regex]': 'false',
            'columns[3][data]': 'nama_kabkota',
            'columns[3][name]': 'nama_kabkota',
            'columns[3][searchable]': 'true',
            'columns[3][orderable]': 'true',
            'columns[3][search][value]': '',
            'columns[3][search][regex]': 'false',
            'columns[4][data]': 'unitkerja',
            'columns[4][name]': 'unitkerja',
            'columns[4][searchable]': 'true',
            'columns[4][orderable]': 'true',
            'columns[4][search][value]': '',
            'columns[4][search][regex]': 'false',
            'columns[5][data]': 'alamatkantor',
            'columns[5][name]': 'alamatkantor',
            'columns[5][searchable]': 'true',
            'columns[5][orderable]': 'true',
            'columns[5][search][value]': '',
            'columns[5][search][regex]': 'false',
            'order[0][column]': '1',
            'order[0][dir]': 'asc',
            'start': '0',
            'length': '700',
            'search[value]': '',
            'search[regex]': 'false',
        }
        
        self.data_dataDermaga = {
            'draw': '1',
            'columns[0][data]': 'id',
            'columns[0][name]': 'id',
            'columns[0][searchable]': 'true',
            'columns[0][orderable]': 'true',
            'columns[0][search][value]': '',
            'columns[0][search][regex]': 'false',
            'columns[1][data]': 'nama',
            'columns[1][name]': 'nama',
            'columns[1][searchable]': 'true',
            'columns[1][orderable]': 'true',
            'columns[1][search][value]': '',
            'columns[1][search][regex]': 'false',
            'columns[2][data]': 'typedermaga',
            'columns[2][name]': 'typedermaga',
            'columns[2][searchable]': 'true',
            'columns[2][orderable]': 'true',
            'columns[2][search][value]': '',
            'columns[2][search][regex]': 'false',
            'columns[3][data]': 'ukuran',
            'columns[3][name]': 'ukuran',
            'columns[3][searchable]': 'true',
            'columns[3][orderable]': 'true',
            'columns[3][search][value]': '',
            'columns[3][search][regex]': 'false',
            'columns[4][data]': 'panjang',
            'columns[4][name]': 'panjang',
            'columns[4][searchable]': 'true',
            'columns[4][orderable]': 'true',
            'columns[4][search][value]': '',
            'columns[4][search][regex]': 'false',
            'columns[5][data]': 'konstruksi',
            'columns[5][name]': 'konstruksi',
            'columns[5][searchable]': 'true',
            'columns[5][orderable]': 'true',
            'columns[5][search][value]': '',
            'columns[5][search][regex]': 'false',
            'columns[6][data]': 'kedalaman',
            'columns[6][name]': 'kedalaman',
            'columns[6][searchable]': 'true',
            'columns[6][orderable]': 'true',
            'columns[6][search][value]': '',
            'columns[6][search][regex]': 'false',
            'columns[7][data]': 'fungsi',
            'columns[7][name]': 'fungsi',
            'columns[7][searchable]': 'true',
            'columns[7][orderable]': 'true',
            'columns[7][search][value]': '',
            'columns[7][search][regex]': 'false',
            'columns[8][data][data]': 'binary',
            'columns[8][name]': '',
            'columns[8][searchable]': 'true',
            'columns[8][orderable]': 'true',
            'columns[8][search][value]': '',
            'columns[8][search][regex]': 'false',
            'order[0][column]': '1',
            'order[0][dir]': 'asc',
            'start': '0',
            'length': '-1',
            'search[value]': '',
            'search[regex]': 'false',
        }
        
        self.data_getTrestle = {
            'draw': '1',
            'columns[0][data]': 'id',
            'columns[0][name]': 'id',
            'columns[0][searchable]': 'true',
            'columns[0][orderable]': 'true',
            'columns[0][search][value]': '',
            'columns[0][search][regex]': 'false',
            'columns[1][data]': 'nama',
            'columns[1][name]': 'nama',
            'columns[1][searchable]': 'true',
            'columns[1][orderable]': 'true',
            'columns[1][search][value]': '',
            'columns[1][search][regex]': 'false',
            'columns[2][data]': 'ukuran',
            'columns[2][name]': 'ukuran',
            'columns[2][searchable]': 'true',
            'columns[2][orderable]': 'true',
            'columns[2][search][value]': '',
            'columns[2][search][regex]': 'false',
            'columns[3][data]': 'konstruksi',
            'columns[3][name]': 'konstruksi',
            'columns[3][searchable]': 'true',
            'columns[3][orderable]': 'true',
            'columns[3][search][value]': '',
            'columns[3][search][regex]': 'false',
            'columns[4][data]': 'keterangan',
            'columns[4][name]': 'keterangan',
            'columns[4][searchable]': 'true',
            'columns[4][orderable]': 'true',
            'columns[4][search][value]': '',
            'columns[4][search][regex]': 'false',
            'order[0][column]': '1',
            'order[0][dir]': 'asc',
            'start': '0',
            'length': '-1',
            'search[value]': '',
            'search[regex]': 'false',
        }
        
        self.data_getCauseway = {
            'draw': '1',
            'columns[0][data]': 'id',
            'columns[0][name]': 'id',
            'columns[0][searchable]': 'true',
            'columns[0][orderable]': 'true',
            'columns[0][search][value]': '',
            'columns[0][search][regex]': 'false',
            'columns[1][data]': 'nama',
            'columns[1][name]': 'nama',
            'columns[1][searchable]': 'true',
            'columns[1][orderable]': 'true',
            'columns[1][search][value]': '',
            'columns[1][search][regex]': 'false',
            'columns[2][data]': 'ukuran',
            'columns[2][name]': 'ukuran',
            'columns[2][searchable]': 'true',
            'columns[2][orderable]': 'true',
            'columns[2][search][value]': '',
            'columns[2][search][regex]': 'false',
            'columns[3][data]': 'konstruksi',
            'columns[3][name]': 'konstruksi',
            'columns[3][searchable]': 'true',
            'columns[3][orderable]': 'true',
            'columns[3][search][value]': '',
            'columns[3][search][regex]': 'false',
            'columns[4][data]': 'keterangan',
            'columns[4][name]': 'keterangan',
            'columns[4][searchable]': 'true',
            'columns[4][orderable]': 'true',
            'columns[4][search][value]': '',
            'columns[4][search][regex]': 'false',
            'order[0][column]': '1',
            'order[0][dir]': 'asc',
            'start': '0',
            'length': '-1',
            'search[value]': '',
            'search[regex]': 'false',
        }
        ...