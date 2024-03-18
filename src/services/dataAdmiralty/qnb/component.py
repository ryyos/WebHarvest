import settings

class QnbComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://qnb.co.id'
        self.target_url = ['https://qnb.co.id/site/default/master/qnb-indonesia/id/aboutqnb/management/boardofdirector', 'https://qnb.co.id/site/default/master/qnb-indonesia/id/aboutqnb/management/boardofcommissioners']
        self.domain = 'qnb.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/qnb/json/'
        ...