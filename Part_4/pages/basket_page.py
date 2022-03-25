from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_LIST), \
        "Products are presented in busket, but should not be" 
    
    def should_be_empty_basket_text(self):
        textElement = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY)
        assert "Your basket is empty. Continue shopping"==textElement.text, "Empty basket text is not present"