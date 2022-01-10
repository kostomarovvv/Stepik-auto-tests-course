from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    found_link = str(math.ceil(math.pow(math.pi, math.e)*10000))

    link = browser.find_element_by_partial_link_text(found_link)
    link.click()

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Victor")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Kostomarov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Brest")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Belarus")
    button = browser.find_element_by_css_selector(".btn-default")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

