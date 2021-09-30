from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link) 
    product_page.open()                   
    product_page.should_be_product_page()
    browser.implicitly_wait(10)
    product_page.solve_quiz_and_get_code()
    product_page.should_be_see_msg_basket()
    time.sleep(30)	
	
	