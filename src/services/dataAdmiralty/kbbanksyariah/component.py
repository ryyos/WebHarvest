import settings

class KbbanksyariahComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.kbbanksyariah.co.id'
        self.target_url = ['https://www.kbbanksyariah.co.id/direksi', 'https://www.kbbanksyariah.co.id/dewankomisaris']
        self.domain = 'www.kbbanksyariah.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/kbbanksyariah/json/'
        ...