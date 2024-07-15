import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.home_page import HomePage
from pages.destination_page import DestinationPage

capabilities = dict(
    platformName='Android',
    deviceName="Vivo V25",
    platformVersion='14',
    # mainActivity = 'com.lionparcel.services.consumer.view.tariff.CheckTariffActivit',
    # appPackage = 'com.lionparcel.services.consumer',
    automationName='UiAutomator2'
)

appium_server_url = 'http://localhost:4723'

 
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
        self.home_page = HomePage(self.driver)
        self.destination_page = DestinationPage(self.driver)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_search_lokasi(self) -> None:
        self.home_page.click_lion_parcel()
        time.sleep(6)
        self.home_page.click_image()
        time.sleep(1)
        self.destination_page.enter_destination_address()
        self.destination_page.search_route("parung")
        tujuan = self.destination_page.get_destination()
        print(f"Tujuan: {tujuan}")

    def test_tukar_asal_dan_tujuan(self):
        self.destination_page.tukar()
        tujuan = self.destination_page.get_destination()
        print(f"Tujuan: {tujuan}")

        aasal = self.destination_page.get_asal()
        print(f"Asal: {aasal}")

if __name__ == '__main__':
    unittest.main()