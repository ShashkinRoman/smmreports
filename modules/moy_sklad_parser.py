from time import sleep
from modules import config


def ms_authorization(driver, login_ms, pass_ms):
    driver.get("https://www.moysklad.ru/login/")
    login = driver.find_element_by_xpath('/html/body/div[3]/main/div[1]/div/div[2]/div[1]/form/fieldset[1]/input')
    # login.click()
    login.send_keys(login_ms)
    # search and input pass
    password = driver.find_element_by_xpath(
        '/html/body/div[3]/main/div[1]/div/div[2]/div[1]/form/fieldset[2]/input')
    password.send_keys(pass_ms)
    # search and click button login
    login_button = driver.find_element_by_xpath(
        '/html/body/div[3]/main/div[1]/div/div[2]/div[1]/form/fieldset[3]/button')
    login_button.click()


def get_info_ms(ms_driver, ms_url_first_part, ms_url_second_part):
    url = config.Weekday().url_ms( ms_url_first_part, ms_url_second_part)
    ms_driver.get(url)
    sleep(3)
    ms_driver.execute_script("window.scrollBy(0,3000)")
    val = ms_driver.find_element_by_xpath('//*[@id="DocumentTablePnl"]/tfoot/tr[2]/th[6]/div')
    final_val = str(val.text).replace(' ', '')
    # print(final_val)
    cost = ms_driver.find_element_by_xpath(
        '/html/body/div[4]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td/div/div/table/tbody/tr[5]/td/table/tfoot/tr[2]/th[8]/div')
    final_cost = str(cost.text).replace(' ', '')
    # print(final_cost)
    ms_driver.execute_script("window.scrollBy(0,-3000)")
    button_buyer = ms_driver.find_element_by_xpath(
        '//*[@id="site"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td/div/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/div/div[3]')
    button_buyer.click()
    sleep(3)
    ms_driver.execute_script("window.scrollBy(0,3000)")
    documents = ms_driver.find_element_by_class_name('pages')
    final_doc = str(documents.text).split()[-1]
    # print(final_doc)
    return final_val, final_cost, final_doc
