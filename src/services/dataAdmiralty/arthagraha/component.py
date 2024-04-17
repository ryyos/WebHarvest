import settings
class ArthagrahaComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.arthagraha.com'
        self.target_url = ['https://www.arthagraha.com/direksi', 'https://www.arthagraha.com/dewan-komisaris']
        self.domain = 'www.arthagraha.com'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/arthagraha/json/'
        ...