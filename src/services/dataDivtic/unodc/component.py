import settings
class UnodcComponent:
    def __init__(self) -> None:

        self.base_api = 'https://sherloc.unodc.org/cld//v3/sherloc/cldb/data.json'
        self.base_url = 'https://sherloc.unodc.org/cld/'
        self.home_url = 'https://sherloc.unodc.org'
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.domain = 'sherloc.unodc.org'
        self.path = 'data/data_raw/unodc/title/json'
        ...