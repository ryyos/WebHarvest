import settings

class SeabankComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://www.seabank.co.id/perusahaan/info/seabank'
        self.base_url = 'https://www.seabank.co.id'
        self.domain = 'www.seabank.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/seabank/json/'
        ...