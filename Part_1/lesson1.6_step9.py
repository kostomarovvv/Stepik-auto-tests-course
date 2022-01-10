from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_class_name("first")
    input1.send_keys("Brest")
    input2 = browser.find_element_by_class_name("second")
    input2.send_keys("Brest")
    input3 = browser.find_element_by_class_name("third")
    input3.send_keys("Brest")

    button = browser.find_element_by_css_selector(".btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    print('Ok!')
finally:
    time.sleep(10)
    browser.quit()