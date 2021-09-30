from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_cart_btn()
		
    def should_be_add_cart_btn(self):
        add_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_CART_BTN)
        add_cart_btn.click()
		
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(answer)
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
			
    def should_be_see_msg_basket(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_product_in_msg = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_MSG)
        assert name_product.text in name_product_in_msg.text