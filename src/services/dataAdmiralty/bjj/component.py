import settings

class BjjComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://www.bjj.co.id/id/about-us'
        self.base_url = 'https://www.bjj.co.id'
        self.domain = 'www.bjj.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/bjj/json/'
        ...