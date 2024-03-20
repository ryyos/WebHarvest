import settings

class BankbsiComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = ['https://ir.bankbsi.co.id/board_of_directors.html', 'https://ir.bankbsi.co.id/board_of_commissioners.html']
        self.base_url = 'https://ir.bankbsi.co.id'
        self.domain = 'ir.bankbsi.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/bankbsi/json/'

        ...