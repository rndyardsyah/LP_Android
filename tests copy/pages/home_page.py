from appium.webdriver.common.appiumby import AppiumBy

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.lion_parcel_button = (AppiumBy.ACCESSIBILITY_ID, "Lion Parcel")
        self.image_button = (AppiumBy.XPATH, "(//android.widget.ImageView[@content-desc=\"Ini merupakan sebuah gambar\"])[6]")

    def click_lion_parcel(self):
        self.driver.find_element(*self.lion_parcel_button).click()

    def click_image(self):
        self.driver.find_element(*self.image_button).click()
