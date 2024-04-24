import settings

class BtpnComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = 'https://www.btpn.com/id/tentang-kami/manajemen#komisioner-0'
        self.base_url = 'https://www.btpn.com'
        self.domain = 'www.btpn.com'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/btpn/json/'

        ...