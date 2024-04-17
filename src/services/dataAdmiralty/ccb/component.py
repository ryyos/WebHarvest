import settings


class CcbComponent:
    def __init__(self) -> None:
        
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://idn.ccb.com/profil-lengkap'
        self.base_url = 'https://idn.ccb.com'
        self.domain = 'idn.ccb.com'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/ccb/json/'
        ...

    