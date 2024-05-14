import settings

class BankmasComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = ['https://bankmas.co.id/id/tentang-kami/manajemen/jajaran-direksi/', 'https://bankmas.co.id/id/tentang-kami/manajemen/jajaran-komisaris/']
        self.base_url = 'https://bankmas.co.id'
        self.domain = 'bankmas.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/bankmas/json/'
        ...