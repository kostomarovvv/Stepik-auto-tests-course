from cgitb import text
from itertools import tee
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON) 
        add_button.click()
        self.solve_quiz_and_get_code()
        productName = self.get_product_name()
        self.test_product_name(productName)
        productPrice = self.get_product_price()
        self.test_product_price(productPrice)

    def just_add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON) 
        add_button.click()

    def test_product_name(self, productName):
        messageElement = self.browser.find_element(*ProductPageLocators.MESSAGE_ELEMENT)
        print(f'Message Name: {messageElement.text}')
        print(f'Product Name: {productName}')
        assert messageElement.text==productName, "Name of product is incorrect"

    def test_product_price(self, productPrice):
        basketElement = self.browser.find_element(*ProductPageLocators.BASKET_ELEMENT)
        print(f'Product price: {productPrice}')
        print(f'Basket  price: {basketElement.text}')
        assert productPrice==basketElement.text, "Price in the basket is incorrect"

    def get_product_name(self):
        productElement = self.browser.find_element(*ProductPageLocators.PRODUCT_ELEMENT)
        return productElement.text

    def get_product_price(self):
        priceElement = self.browser.find_element(*ProductPageLocators.PRICE_ELEMENT)
        return priceElement.text       

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ELEMENT), \
        "Success message is presented, but should not be" 

    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ELEMENT), \
        "Disappear message is not disappeared"