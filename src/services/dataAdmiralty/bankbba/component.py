import settings

class BankbbaComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.bankbba.co.id'
        self.target_url = ['https://www.bankbba.co.id/bumiarta/id/dewan-direksi/index', 'https://www.bankbba.co.id/bumiarta/id/dewan-komisaris/index']
        self.domain = 'www.bankbba.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/bankbba/json/'
        ...