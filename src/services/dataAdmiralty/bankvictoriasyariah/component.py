import settings

class BankvictoriasyariahComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = ['https://bankvictoriasyariah.co.id/page/sub/direksi', 'https://bankvictoriasyariah.co.id/page/sub/dewan-komisaris']
        self.base_url = 'https://bankvictoriasyariah.co.id'
        self.domain = 'bankvictoriasyariah.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/bankvictoriasyariah/json/'

        ...