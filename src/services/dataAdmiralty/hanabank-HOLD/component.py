import settings

class HanabankComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://www.hanabank.co.id/about/company/management'
        self.base_url = 'https://www.hanabank.co.id'
        self.domain = 'www.hanabank.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/hanabank/json/'

        ...