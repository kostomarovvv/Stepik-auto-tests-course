from selenium import webdriver
import time
import math
import pytest

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', [
	"https://stepik.org/lesson/236895/step/1", 
	"https://stepik.org/lesson/236896/step/1",
	"https://stepik.org/lesson/236897/step/1",
	"https://stepik.org/lesson/236898/step/1",
	"https://stepik.org/lesson/236899/step/1",
	"https://stepik.org/lesson/236903/step/1",
	"https://stepik.org/lesson/236904/step/1",
	"https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, language):
    link = f"{language}"
    print(link)
    browser.implicitly_wait(15)
    browser.get(link)

    ans_element = browser.find_element_by_css_selector(".ember-text-area")
    ans_element.click()
    ans_element.clear()
    answer = math.log(int(time.time()))
    ans_element.send_keys(str(answer))


    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()

    msg_element = browser.find_element_by_css_selector(".smart-hints__hint")
    assert msg_element.text == "Correct!", msg_element.text



