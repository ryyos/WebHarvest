import datetime as date

from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

from time import strftime, time, localtime, struct_time, mktime
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
    @staticmethod
    def epoch_today():
        current_time = time()
        local_time = localtime(current_time)
        midnight_time = struct_time((local_time.tm_year, local_time.tm_mon, local_time.tm_mday, 0, 0, 0, local_time.tm_wday, local_time.tm_yday, local_time.tm_isdst))
        midnight_epoch = mktime(midnight_time)
        return int(midnight_epoch)


    @staticmethod
    def relative2date(relative_time: str) -> str:
        if relative_time.startswith('se'):
            relative_time = f'1 {relative_time[2:]}'
            
        parsed_time = datetime.now()

        if 'menit' in relative_time:
            minutes_ago = int(relative_time.split()[0])
            parsed_time -= relativedelta(minutes=minutes_ago)

        elif 'jam' in relative_time:
            hours_ago = int(relative_time.split()[0])
            parsed_time -= relativedelta(hours=hours_ago)

        elif 'hari' in relative_time:
            days_ago = int(relative_time.split()[0])
            parsed_time -= relativedelta(days=days_ago)

        elif 'minggu' in relative_time:
            weeks_ago = int(relative_time.split()[0])
            parsed_time -= relativedelta(weeks=weeks_ago)

        elif 'bulan' in relative_time:
            months_ago = int(relative_time.split()[0])
            parsed_time -= relativedelta(months=months_ago)

        elif 'tahun' in relative_time:
            years_ago = int(relative_time.split()[0])
            parsed_time -= relativedelta(years=years_ago)

        return parsed_time.strftime('%Y-%m-%d %H:%M:%S')
        ...