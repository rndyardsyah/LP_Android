import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
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

    def test_cek_tarif(self) -> None:
        self.home_page.click_lion_parcel()
        time.sleep(6)
        self.home_page.click_image()
        time.sleep(1)
        self.destination_page.enter_destination_address()
        self.destination_page.search_route("parung")
        self.destination_page.check_tariff()

        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(515, 1885)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(515, 510)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        self.destination_page.click_jumbopack()

        total_tariff = self.destination_page.get_total_jumbo()
        print(f"Total Tariff Jumbo: {total_tariff}")

        self.destination_page.click_request_drop()
        

if __name__ == '__main__':
    unittest.main()
