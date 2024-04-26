import settings

class BankneocommerceComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://www.bankneocommerce.co.id/id/company-information/management'
        self.base_url = 'https://www.bankneocommerce.co.id'
        self.domain = 'www.bankneocommerce.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/bankneocommerce/json/'
        ...