import settings

class BankganeshaComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.bankganesha.co.id'
        self.target_url = ['https://www.bankganesha.co.id/index.php/aboutus/direksi', 'https://www.bankganesha.co.id/index.php/aboutus/komisaris']
        self.domain = 'www.bankganesha.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/bankganesha/json/'
        ...