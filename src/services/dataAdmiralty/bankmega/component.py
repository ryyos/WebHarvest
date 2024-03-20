import settings

class BankmegaComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://bankmega.com/id/tentang-kami/manajemen-komite/'
        self.base_url = 'https://bankmega.com'
        self.domain = 'bankmega.com'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/bankmega/json/'

        ...