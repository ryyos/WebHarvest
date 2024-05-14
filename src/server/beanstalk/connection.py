import atexit
from greenstalk import Client, TimedOutError, Job

class ConnectionBeanstalk:
    def __init__(self, host: str, port: str, tube: str) -> None:
        self.client = Client((host, port), use=tube, watch=tube)
        atexit.register(self.close)
        ...
        
    def close(self) -> None:
        self.client.close()
        ...