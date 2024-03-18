import settings

class JtrustbankComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.jtrustbank.co.id'
        self.target_url = ['https://www.jtrustbank.co.id/id/information/corporate-information/board-of-director', 'https://www.jtrustbank.co.id/id/information/corporate-information/board-of-commissioner']
        self.domain = 'www.jtrustbank.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/Jtrustbank/json/'

        self.temp_target = ''
        ...