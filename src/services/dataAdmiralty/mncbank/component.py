import settings

class MncbankComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = ['https://mncbank.co.id/api/post/direksi?children=true&lang=id', 'https://mncbank.co.id/api/post/komisaris?children=true&lang=id']
        self.base_url = 'https://mncbank.co.id/'
        self.domain = 'mncbank.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/mncbank/json/'

        ...