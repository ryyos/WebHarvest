import settings

class BankcapitalComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.bankcapital.co.id'
        self.target_url = ['https://www.bankcapital.co.id/id/direktur', 'https://www.bankcapital.co.id/id/dewan-komisaris']
        self.domain = 'www.bankcapital.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/bankcapital/json/'
        ...