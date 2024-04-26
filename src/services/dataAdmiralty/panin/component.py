import settings

class PaninComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://www.panin.co.id/id/about-panin/info-korporasi/management'
        self.base_url = 'https://www.panin.co.id'
        self.domain = 'www.panin.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/panin/json/'
        ...