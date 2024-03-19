import settings

class GeospasialComponent:
    def __init__(self) -> None:
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://www.indonesia-geospasial.com'
        self.target_url = 'https://www.indonesia-geospasial.com/2020/09/download-shp-tutupan-lahan-tahun-2019.html'
        self.domain = 'www.indonesia-geospasial.com'
        self.password_rar = 'www.indonesia-geospasial.com'
        ...