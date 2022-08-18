from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    element = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert element is not None, "not"