import settings
class DephubComponent:
    def __init__(self) -> None:
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://simpel.dephub.go.id'
        self.target_url = 'https://simpel.dephub.go.id/index.php/front/service/92c7b0031b935ca78d4891c6c08d657b/grid'
        self.row_url = 'https://simpel.dephub.go.id/index.php/outerapp/pageinfo/92c7b0031b935ca78d4891c6c08d657b/'
        self.cookies = 'cookies'
        self.headers = {
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
        ...