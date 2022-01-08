from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)

    ans_element = browser.find_element_by_id("answer")
    ans_element.send_keys(y)

    browser.execute_script("window.scrollBy(0, 100);")

    robotcb = browser.find_element_by_css_selector("#robotCheckbox")
    robotcb.click()

    robotrb = browser.find_element_by_css_selector("#robotsRule")
    robotrb.click()

    button = browser.find_element_by_css_selector(".btn")
    #browser.execute_script("window.scrollBy(0, 100);")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    time.sleep(10)
    browser.quit()