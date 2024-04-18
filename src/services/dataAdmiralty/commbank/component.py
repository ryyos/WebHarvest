import settings

class CommbankComponent:
    def __init__(self) -> None:
        
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.commbank.co.id'
        self.target_url = 'https://www.commbank.co.id/id/bod'
        self.domain = 'www.commbank.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/commbank/json/'
        ...

    