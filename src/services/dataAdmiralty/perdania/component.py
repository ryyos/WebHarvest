import settings


class PerdaniaComponent:
    def __init__(self) -> None:
        
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://www.perdania.co.id/about-perdania/company-profile/management-and-executive-officer/'
        self.base_url = 'https://www.perdania.co.id'
        self.domain = 'www.perdania.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/perdania/json/'
        ...

    