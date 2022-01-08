from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try: 
    browser = webdriver.Chrome()
#    browser.execute_script("alert('Robots at work');")
#    browser.execute_script("document.title='Script executing';")
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    time.sleep(10)
    browser.quit()