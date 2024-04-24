import settings

class KromComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://krom.id/informasi-perusahaan/'
        self.base_url = 'https://krom.id'
        self.domain = 'krom.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/krom/json/'
        ...