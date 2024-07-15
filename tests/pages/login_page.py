# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textfield = (By.ID, "user-name")
        self.password_textfield = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.logo = (By.CLASS_NAME, "app_logo")
        self.add_cart_bag_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_cart_light_button = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.cart_button = (By.ID, "shopping_cart_container")
        self.checkout_button = (By.ID, "checkout")
        self.firstname_textfield = (By.ID, "first-name")
        self.lastname_textfield = (By.ID, "last-name")
        self.poscode_textfield = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.list_invoice = {
            "product_1": (By.XPATH, "//div[@class='cart_item'][1]"),
            "product_2": (By.XPATH, "//div[@class='cart_item'][2]"),
            "payment_code": (By.XPATH, "//div[@data-test='payment-info-value']"),
            "shipping_code": (By.XPATH, "//div[@data-test='shipping-info-value']"),
            "total": (By.XPATH, "//div[@data-test='total-label']")
        }
        self.finish_button = (By.ID, "finish")
        self.succes = (By.XPATH, "//div[@data-test='complete-text']")

    def open_login(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(*self.username_textfield).send_keys("standard_user")
        self.driver.find_element(*self.password_textfield).send_keys("secret_sauce")
        self.driver.find_element(*self.login_button).click()
    def wait_login(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(self.logo))
    def add_to_cart(self):
        self.driver.find_element(*self.add_cart_bag_button).click()
        self.driver.find_element(*self.add_cart_light_button).click()
        self.driver.find_element(*self.cart_button).click()
    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        self.driver.find_element(*self.firstname_textfield).send_keys("Rendy")
        self.driver.find_element(*self.lastname_textfield).send_keys("Ardiansyah")
        self.driver.find_element(*self.poscode_textfield).send_keys("15157")
        self.driver.find_element(*self.continue_button).click()
    def get_invoice(self):
        wait = WebDriverWait(self.driver, 10)
        list_invoice = {}
        for key, locator in self.list_invoice.items():
            element = wait.until(EC.presence_of_element_located(locator))
            list_invoice[key] = element.text
        return list_invoice
    def finish_order(self):
        self.driver.find_element(*self.finish_button).click()
    def get_label_succes(self):
        wait = WebDriverWait(self.driver, 10)
        succes_label = wait.until(EC.presence_of_element_located(self.succes))
        return succes_label.text

   
  