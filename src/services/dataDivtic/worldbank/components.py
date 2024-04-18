import settings
class WorldbankComponent:
    def __init__(self) -> None:
        self.csv_path = 'src/services/dataDivtic/worldbank/assets/API_CM.MKT.LDOM.NO_DS2_en_csv_v2_65874.csv'
        self.domain = 'worldbank.org'
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        ...