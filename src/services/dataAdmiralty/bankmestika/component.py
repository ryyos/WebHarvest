import settings

class BankmestikaComponent:
    def __init__(self) -> None:
        
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.bankmestika.co.id'
        self.target_url = 'https://www.bankmestika.co.id/id/aboutus/structural-organization'
        self.domain = 'www.bankmestika.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/bankmestika/json/'
        ...    