from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Victor")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Kostomarov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Brest")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Belarus")
    button = browser.find_element_by_css_selector("#submit_button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

