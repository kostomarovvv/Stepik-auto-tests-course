from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ELEMENT = (By.CSS_SELECTOR, '[name="registration-email"]')
    PASSWORD_ELEMENT = (By.CSS_SELECTOR, '[name="registration-password1"]')
    CONFIRM_ELEMENT = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-primary")   
    MESSAGE_ELEMENT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > .alertinner > strong")    
    PRODUCT_ELEMENT = (By.CSS_SELECTOR, ".col-sm-6 h1")    
    PRICE_ELEMENT = (By.CSS_SELECTOR, ".col-sm-6 .price_color")    
    BASKET_ELEMENT = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > .alertinner p strong")    

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LIST = (By.CSS_SELECTOR, "#content_inner form")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")