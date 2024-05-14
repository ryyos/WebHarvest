import settings
from typing import List
from src.utils import File

class BpsPublikasiComponent:
    def __init__(self) -> None:
        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        
        self.domain = 'bps.go.id'
        self.path_target = 'src/services/dataDivtic/bps_publikasi/database/bps_publication_target.json'
        self.path_target_prov = 'src/services/dataDivtic/bps_publikasi/database/bps_publikasi_prov.json'
        self.path_done = 'src/services/dataDivtic/bps_publikasi/database/bps_publication_done.json'
        self.path_err = 'src/services/dataDivtic/bps_publikasi/database/bps_publication_error.json'
        
        self.targets: List[str] = File.read_list_json(self.path_target)
        self.targets_prov: List[str] = File.read_list_json(self.path_target_prov)
        self.error: List[str] = File.read_list_json(self.path_err)
        self.dones: List[str] = File.read_list_json(self.path_done)
        ...