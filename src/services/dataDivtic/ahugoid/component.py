import settings

class AhugoidComponent:
    def __init__(self) -> None:
        
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.base_url = 'https://ahu.go.id/pencarian/profil-pt/'
        self.domain = 'ahu.go.id'
        
        ...