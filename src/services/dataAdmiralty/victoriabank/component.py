import settings

class VictoriabankComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = ['https://victoriabank.co.id/page/tentang-kami/manajemen/-direksi/', 'https://victoriabank.co.id/page/tentang-kami/manajemen/dewan-komisaris/']
        self.base_url = 'https://victoriabank.co.id'
        self.domain = 'victoriabank.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/victoriabank/json/'
        ...