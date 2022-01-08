from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".btn")
    button.click()

    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)

    time.sleep(1)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)

    ans_element = browser.find_element_by_id("answer")
    ans_element.send_keys(y)

    button = browser.find_element_by_css_selector(".btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()