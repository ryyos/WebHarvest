import settings
class IcbcComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.icbc.co.id'
        self.target_url = 'https://www.icbc.co.id/en/column/1438058492253847611.html'
        self.domain = 'www.icbc.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/icbc/json/'
        ...