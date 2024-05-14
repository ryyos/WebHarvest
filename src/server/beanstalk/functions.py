import json
from .connection import ConnectionBeanstalk, TimedOutError, Client, Job
from typing import Generator, Dict

class Beanstalk:
    def __init__(self, host: str, port: str, tube: str) -> None:
        self.connection: ConnectionBeanstalk = ConnectionBeanstalk(host, port, tube)
        self.job: Job = None
        ...
        
    def get(self) -> Generator[Dict[str, any], any, None]:
        while True:
            try:
                self.job = self.connection.client.reserve(timeout=10)
                yield json.loads(self.job.body)
                self.__delete()
            except TimedOutError:
                yield None
            except BrokenPipeError:
                raise
            except Exception:
                raise
            
    def put(self, output: str, **kwargs) -> None:
        self.connection.client.put(body=output, **kwargs)
        ...

    def __delete(self) -> None:
        if self.job:
            self.connection.client.delete(self.job)
            self.job = None
        ...

    def __bury(self, **kwargs) -> None:
        if self.job:
            self.connection.client.bury(self.job, **kwargs)
            self.job = None
        ...

    def exception_handler(self, e, **kwargs) -> None:
        action = kwargs.get("action")
        if action == "delete":
            self.__delete()
        else:
            self.__bury()
