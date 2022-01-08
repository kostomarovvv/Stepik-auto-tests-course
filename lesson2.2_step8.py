from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Victor")
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Kostomarov")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("vkostomarov@vkostomarov.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))    
    file_path = os.path.join(current_dir, 'file1.txt') 
    file1 = browser.find_element_by_css_selector("[type='file']")
    file1.send_keys(file_path)

    button = browser.find_element_by_css_selector(".btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()