from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element_by_id("num1")
    num1 = int(num1_element.text)

    num2_element = browser.find_element_by_id("num2")
    num2 = int(num2_element.text)

    print(num1+num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(num1+num2))


    button = browser.find_element_by_css_selector(".btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()