import settings

class MayBankComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.maybank.co.id/'
        self.target_url = ['https://www.maybank.co.id/corporateinformation/BoardOfDirectors/', 'https://www.maybank.co.id/corporateinformation/BoardofCommissioners/']
        self.domain = 'www.maybank.co.id'
        self.type = ['direksi', 'komisaris']

        self.base_path = 'data/data_raw/admiralty/data_perbankan/maybank/json/'
        self.temp_target = ''
        ...