import settings

class OkbankComponent:
    def __init__(self) -> None:

        self.base_path_s3 = settings.S3_CONFIGURATIONS["base_path_s3"]
        self.target_url = ['https://www.okbank.co.id/id/about/profile/leader/board-of-directors', 'https://www.okbank.co.id/id/about/profile/leader/board-of-commissioners']
        self.base_url = 'https://www.okbank.co.id'
        self.domain = 'www.okbank.co.id'
        self.type = ['direksi', 'komisaris']
        self.base_path = 'data/data_raw/admiralty/data_perbankan/okbank/json/'
        self.cookies = {
            'XSRF-TOKEN': 'eyJpdiI6IlF3bVcrN2kwR01TNEN1M04yWHlOMGc9PSIsInZhbHVlIjoiOUZHYWZjRDZVS0J3MGhFUzlHcW9CRGlmcWdnbXRQSXlsOGQrRW5XQ3gzZ3M4NkhGcmNoand2RXRuOXJ5STNVQjFlZkdkS2g4UGVGM1VKUUpPRmFYZmtJNXcxS01IWVV1SU1oOXBnenF3cnhucUZnYk5JbW1SdHJGek9pNkJQVm0iLCJtYWMiOiIyNDg0NGQ0ZjlhMGQ3ODJjYzljMDNhMWUxZmIzZTgwMTg5ZmVlZDU3MzcyMGQxMTE0NDlhOWI5NjllMGZjMmRiIiwidGFnIjoiIn0%3D',
            'laravel_session': 'eyJpdiI6InY1N0hveFpCU1VtTUpURlNwMzJHbmc9PSIsInZhbHVlIjoicFR0eGdTVWRYZ3ViVEpIZEQ5aDRsa0gwcEkwYmUrV0RwVUpoMWFmbytRUlJ4d1Vkc0tlQjVhckkwd011RzE5dGhYa0F4UXBWeTdUOW1nTXJIN28ycExhSGN6eWo1NDVKS0NEK1lyYVNwSlVSTERWZ0hScUFsWDFNRWI3RjlYcmEiLCJtYWMiOiIyZDEwMmNmYjhjOGE3ODdlMjljOTgwNzMwMGI4NmUxOTQxMmQ2MjgwMTRjODNmMDgwNGMzMzM4N2M2N2FhZWE4IiwidGFnIjoiIn0%3D',
            'TawkConnectionTime': '0',
            'twk_idm_key': 'wOvJnQDeaPYKVBet9TYXp',
            'twk_uuid_621343b61ffac05b1d7adf45': '%7B%22uuid%22%3A%221.SwsupyuvbIYhDWcMFyaLGojaXLhOoQcZWoE6yhB8qaIzSRLuZjMA2X1BlrFOicyRi2kNItxG48dFa4JRyNZqiKzkCLtXjt0wnFEQGkwwcicwXjegDDPAp%22%2C%22version%22%3A3%2C%22domain%22%3A%22okbank.co.id%22%2C%22ts%22%3A1714628323693%7D',
        }

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
            'Accept': 'text/html, application/xhtml+xml',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Inertia': 'true',
            'X-Inertia-Version': 'fc6fad2656c7f301bde08325f2572b58',
            'Content-Type': 'application/json',
            'X-XSRF-TOKEN': 'eyJpdiI6IlF3bVcrN2kwR01TNEN1M04yWHlOMGc9PSIsInZhbHVlIjoiOUZHYWZjRDZVS0J3MGhFUzlHcW9CRGlmcWdnbXRQSXlsOGQrRW5XQ3gzZ3M4NkhGcmNoand2RXRuOXJ5STNVQjFlZkdkS2g4UGVGM1VKUUpPRmFYZmtJNXcxS01IWVV1SU1oOXBnenF3cnhucUZnYk5JbW1SdHJGek9pNkJQVm0iLCJtYWMiOiIyNDg0NGQ0ZjlhMGQ3ODJjYzljMDNhMWUxZmIzZTgwMTg5ZmVlZDU3MzcyMGQxMTE0NDlhOWI5NjllMGZjMmRiIiwidGFnIjoiIn0=',
            'Connection': 'keep-alive',
            'Referer': 'https://www.okbank.co.id/id/about/profile/leader/board-of-directors',
            # 'Cookie': 'XSRF-TOKEN=eyJpdiI6IlF3bVcrN2kwR01TNEN1M04yWHlOMGc9PSIsInZhbHVlIjoiOUZHYWZjRDZVS0J3MGhFUzlHcW9CRGlmcWdnbXRQSXlsOGQrRW5XQ3gzZ3M4NkhGcmNoand2RXRuOXJ5STNVQjFlZkdkS2g4UGVGM1VKUUpPRmFYZmtJNXcxS01IWVV1SU1oOXBnenF3cnhucUZnYk5JbW1SdHJGek9pNkJQVm0iLCJtYWMiOiIyNDg0NGQ0ZjlhMGQ3ODJjYzljMDNhMWUxZmIzZTgwMTg5ZmVlZDU3MzcyMGQxMTE0NDlhOWI5NjllMGZjMmRiIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6InY1N0hveFpCU1VtTUpURlNwMzJHbmc9PSIsInZhbHVlIjoicFR0eGdTVWRYZ3ViVEpIZEQ5aDRsa0gwcEkwYmUrV0RwVUpoMWFmbytRUlJ4d1Vkc0tlQjVhckkwd011RzE5dGhYa0F4UXBWeTdUOW1nTXJIN28ycExhSGN6eWo1NDVKS0NEK1lyYVNwSlVSTERWZ0hScUFsWDFNRWI3RjlYcmEiLCJtYWMiOiIyZDEwMmNmYjhjOGE3ODdlMjljOTgwNzMwMGI4NmUxOTQxMmQ2MjgwMTRjODNmMDgwNGMzMzM4N2M2N2FhZWE4IiwidGFnIjoiIn0%3D; TawkConnectionTime=0; twk_idm_key=wOvJnQDeaPYKVBet9TYXp; twk_uuid_621343b61ffac05b1d7adf45=%7B%22uuid%22%3A%221.SwsupyuvbIYhDWcMFyaLGojaXLhOoQcZWoE6yhB8qaIzSRLuZjMA2X1BlrFOicyRi2kNItxG48dFa4JRyNZqiKzkCLtXjt0wnFEQGkwwcicwXjegDDPAp%22%2C%22version%22%3A3%2C%22domain%22%3A%22okbank.co.id%22%2C%22ts%22%3A1714628323693%7D',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }
        ...