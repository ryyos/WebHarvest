import settings
class AladinbankComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://aladinbank.id/manajemen/'
        self.base_url = 'https://aladinbank.id'
        self.domain = 'aladinbank.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/aladinbank/json/'
        ...