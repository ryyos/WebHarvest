import settings

class OcbcComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.ocbc.id'
        self.target_url = 'https://www.ocbc.id/id/tentang-ocbc-nisp/profile/manajemen'
        self.domain = 'www.ocbc.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/ocbc/json/'

        ...