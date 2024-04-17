import settings

class MegasyariahComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = ['https://www.megasyariah.co.id/id/tentang-kami/profil-manajemen/dewan-direksi', 'https://www.megasyariah.co.id/id/tentang-kami/profil-manajemen/dewan-komisaris']
        self.base_url = 'https://www.megasyariah.co.id'
        self.domain = 'www.megasyariah.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/megasyariah/json/'

        ...