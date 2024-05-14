from src.utils import Time
class GetDayTrendsComponent:
    def __init__(self) -> None:
        self.target_urls = ['https://getdaytrends.com/', 'https://getdaytrends.com/indonesia/']
        self.path_done = f'logs/GetDayTrends/{Time.now()}.log'
        ...