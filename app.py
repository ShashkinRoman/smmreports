from projects import kans, beautymarket
from webdriver import webdriver_conf

driver = webdriver_conf.Webdriver.driver
try:
    beautymarket.main()
except Exception as exc: print('\n-----------------------------------------------'), \
                         print(exc), \
                         print('\n-----------------------------------------------')

try:
    kans.main()
except Exception as exc: print('\n-----------------------------------------------'), \
                         print(exc), \
                         print('\n-----------------------------------------------')

driver.close()
