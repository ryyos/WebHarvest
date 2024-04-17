import settings

class DbsComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.dbs.com'
        self.target_url = ['https://www.dbs.com/indonesia/bh/about-us/our-management/board-of-directors/default.page', 'https://www.dbs.com/indonesia/bh/about-us/our-management/board-of-commisioners/default.page']
        self.domain = 'www.dbs.com'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/dbs/json/'
        ...