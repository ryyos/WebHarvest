import settings
class AnzComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.anz.com'
        self.target_url = 'https://www.anz.com/institutional/global/indonesia/ind/management-team/#:~:text=Jodi%20West&text=Jodi%20West%20saat%20ini%20menjabat,Juli%202018%20%E2%80%93%20Juli%202023).'
        self.domain = 'www.anz.com'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/anz/json/'
        ...