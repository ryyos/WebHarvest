import settings


class ShinhanComponent:
    def __init__(self) -> None:
        
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.shinhan.co.id/management'
        self.target_url = 'https://www.shinhan.co.id/management'
        self.domain = 'www.shinhan.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/shinhan/json/'
        ...

    