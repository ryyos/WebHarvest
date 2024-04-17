import settings

class HibankComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://hibank.co.id/backoffice/api/id/v2/managements'
        self.base_url = 'https://www.hibank.co.id'
        self.domain = 'www.hibank.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/hibank/json/'

        ...