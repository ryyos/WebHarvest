import settings

class BankmuamalatComponent:
    def __init__(self) -> None:
        
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.bankmuamalat.co.id'
        self.target_url = ['https://www.bankmuamalat.co.id/index.php/direksi', 'https://www.bankmuamalat.co.id/index.php/dewan-komisaris']
        self.domain = 'www.bankmuamalat.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/bankmuamalat/json/'
        ...

    