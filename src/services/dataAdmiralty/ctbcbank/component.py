import settings

class CtbcbankComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = ['https://www.ctbcbank.co.id/about-us/corporate-information/direksi', 'https://www.ctbcbank.co.id/about-us/corporate-information/dewan-komisaris']
        self.base_url = 'https://www.ctbcbank.co.id'
        self.domain = 'www.ctbcbank.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/ctbcbank/json/'
        ...