import settings

class BankmandiritaspenComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://www.bankmandiritaspen.co.id/article/id-manajemen/id'
        self.base_url = 'https://www.bankmandiritaspen.co.id'
        self.domain = 'www.bankmandiritaspen.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/bankmandiritaspen/json/'
        ...