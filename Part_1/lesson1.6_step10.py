from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("div.first_block > div.first_class > input")
    input1.send_keys("First")
    input2 = browser.find_element_by_css_selector("div.first_block > div.second_class > input")
    input2.send_keys("Second")
    input3 = browser.find_element_by_css_selector("div.first_block > div.third_class > input")
    input3.send_keys("Third")

    button = browser.find_element_by_css_selector(".btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()