import settings

class BanksinarmasComponent:
    def __init__(self) -> None:
        
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.banksinarmas.com/id/'
        self.target_url = 'https://www.banksinarmas.com/id/informasiumum/tentangkami/managemen-bank-sinarmas'
        self.domain = 'www.banksinarmas.com'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/banksinarmas/json/'
        ...

    