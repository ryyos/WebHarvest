import datetime as date

from time import strftime, time
from requests_html import HTMLSession
from datetime import datetime, timezone

class Time:

    @staticmethod
    def convert_time(times: str) -> int:
        dt = date.datetime.fromisoformat(times)
        dt = dt.replace(tzinfo=timezone.utc) 
        return int(dt.timestamp())
        ...

    @staticmethod
    def now():
        return strftime('%Y-%m-%d %H:%M:%S')
        ...

    @staticmethod
    def today():
        return datetime.now().strftime("%Y-%m-%d")
        ...

    @staticmethod
    def change_format(dates: str) -> str:
        try: return dates.replace('T', ' ')
        except Exception: return dates
        ...

    @staticmethod
    def epoch():
        return int(time())
        ...

    @staticmethod
    def epoch_ms():
        return str(round(time() * 1000))
        ...