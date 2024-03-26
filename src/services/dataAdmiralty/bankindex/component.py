import settings

class BankindexComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://www.bankindex.co.id/about/management'
        self.base_url = 'https://www.bankindex.co.id'
        self.domain = 'www.bankindex.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/bankindex/json/'

        ...