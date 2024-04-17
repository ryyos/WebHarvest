import settings
class ImdiComponent:
    def __init__(self) -> None:

        self.base_api = 'https://imdi.sdmdigital.id/getDataKabupaten'
        self.base_api_all = 'https://imdi.sdmdigital.id/get_pilar'
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.domain = 'imdi.sdmdigital.id'
        ...