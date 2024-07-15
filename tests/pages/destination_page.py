from appium.webdriver.common.appiumby import AppiumBy

class DestinationPage:
    def __init__(self, driver):
        self.driver = driver
        self.destination_address_field = (AppiumBy.ID, "com.lionparcel.services.consumer:id/edtDestinationAddress")
        self.route_search_field = (AppiumBy.ID, "com.lionparcel.services.consumer:id/edtRouteSearch")
        self.parung_option = (AppiumBy.XPATH, "(//android.widget.LinearLayout[@resource-id='com.lionparcel.services.consumer:id/llDestinationRoute'])[1]")
        self.check_tariff_button = (AppiumBy.ID, "com.lionparcel.services.consumer:id/btnCheckTariff")
        self.total_tariff_estimation = (AppiumBy.ID, "com.lionparcel.services.consumer:id/txtTotalTariffEstimation")
        self.jumbo_pack = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.lionparcel.services.consumer:id/txtEstimatedPrice' and @text='Rp105.000']")
        self.request_pick_up = (AppiumBy.ID, "com.lionparcel.services.consumer:id/buttonPickUp")
        self.request_drop = (AppiumBy.ID, "com.lionparcel.services.consumer:id/buttonDropOff")
        self.asal = (AppiumBy.ID, "com.lionparcel.services.consumer:id/edtOriginAddress")
        self.total_berat = (AppiumBy.ID, "com.lionparcel.services.consumer:id/edtTotalWeight")
        self.allert_berat = (AppiumBy.ID, "com.lionparcel.services.consumer:id/textinput_helper_text")
        self.back = (AppiumBy.ID, "com.lionparcel.services.consumer:id/vWTToolbar")



    def enter_destination_address(self):
        self.driver.find_element(*self.destination_address_field).click()

    def get_destination(self):
        return self.driver.find_element(*self.destination_address_field).text
    
    def get_asal(self):
        return self.driver.find_element(*self.asal).text

    def search_route(self, route_name):
        self.driver.find_element(*self.route_search_field).send_keys(route_name)
        self.driver.find_element(*self.parung_option).click()

    def check_tariff(self):
        self.driver.find_element(*self.check_tariff_button).click()
    
    def tukar(self):
        self.driver.find_element(AppiumBy.ID, "com.lionparcel.services.consumer:id/llReverse").click()

    def click_jumbopack(self):
        self.driver.find_element(*self.jumbo_pack).click()

    def click_request_pickup(self):
        self.driver.find_element(*self.request_pick_up).click()
    
    def click_request_drop(self):
        self.driver.find_element(*self.request_drop).click()

    def get_total_tariff_estimation(self):
        return self.driver.find_element(*self.total_tariff_estimation).text

    def get_total_jumbo(self):
        return self.driver.find_element(*self.total_tariff_estimation).text

    def send_berat(self, berat):
        self.driver.find_element(*self.total_berat).send_keys(berat)

    def get_allert_berat(self):
        return self.driver.find_element(*self.allert_berat).text
    def click_back(self):
        self.driver.find_element(*self.back).click()


    
