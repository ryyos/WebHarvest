import settings

class UobComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.uob.co.id'
        self.target_url = ['https://www.uob.co.id/about-us/company-information/our-management/direksi-uob-indonesia.page?', 'https://www.uob.co.id/about-us/company-information/our-management/dewan-komisaris-uob-indonesia.page?']
        self.domain = 'www.uob.co.id'
        self.type = ['direksi', 'komisaris']
        self.temp_target = ''
        self.base_path = 'data/data_raw/admiralty/data_perbankan/uob/json/'
        ...