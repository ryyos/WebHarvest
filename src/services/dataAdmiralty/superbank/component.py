import settings

class SuperbankComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://www.superbank.id/tentang-kami/manajemen-dewan-komisaris'
        self.base_url = 'https://www.superbank.id'
        self.domain = 'www.superbank.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/superbank/json/'
        ...