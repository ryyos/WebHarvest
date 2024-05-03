import settings

class AmarbankComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = ['https://amarbank.co.id/management/direksi', 'https://amarbank.co.id/management/dewan-komisaris']
        self.base_url = 'https://amarbank.co.id'
        self.domain = 'amarbank.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/amarbank/json/'
        ...