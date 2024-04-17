import settings

class BoiindonesiaComponent:
    def __init__(self) -> None:
        
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.boiindonesia.co.id/'
        self.target_url = 'https://www.boiindonesia.co.id/main.php?hal=management'
        self.domain = 'www.boiindonesia.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/boiindonesia/json/'

        self.temp_target = ''
        ...

    