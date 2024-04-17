import settings

class KbbukopinsyariahComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = ['https://www.kbbukopinsyariah.com/direksi', 'https://www.kbbukopinsyariah.com/dewankomisaris']
        self.base_url = 'https://www.kbbukopinsyariah.com'
        self.domain = 'www.kbbukopinsyariah.com'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/kbbukopinsyariah/json/'

        ...