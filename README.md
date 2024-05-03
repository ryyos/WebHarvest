`
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/")
`
