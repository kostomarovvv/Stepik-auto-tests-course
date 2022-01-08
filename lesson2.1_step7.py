from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)

    ans_element = browser.find_element_by_id("answer")
    ans_element.send_keys(y)

    robotcb = browser.find_element_by_css_selector("#robotCheckbox")
    robotcb.click()

    robotrb = browser.find_element_by_css_selector("#robotsRule")
    robotrb.click()

    button = browser.find_element_by_css_selector(".btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()