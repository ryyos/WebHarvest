import settings
class BankmayapadaComponent:
    def __init__(self) -> None:
        
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.bankmayapada.com'
        self.target_url = 'https://www.bankmayapada.com/id/tentang-kami/manajemen'
        self.domain = 'www.bankmayapada.com'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/bankmayapada/json/'

        self.temp_target = ''
        ...

    