import pytest
import time
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_beli(driver):
    login_page = LoginPage(driver)
    login_page.open_login()
    logo = login_page.wait_login()
    assert logo, "Gagal Login"
    print("Sukses login")
    login_page.add_to_cart()
    login_page.checkout()

    list_invoice = login_page.get_invoice()
    print(f"Produk Pertama : {list_invoice['product_1']}")
    print(f"Produk Kedua : {list_invoice['product_2']}")
    print(f"Kode Pembayaran : {list_invoice['payment_code']}")
    print(f"Motede Pengiriman: {list_invoice['shipping_code']}")
    print(f"{list_invoice['total']}")
    time.sleep(2)
    login_page.finish_order()


    succes_text = login_page.get_label_succes()
    print(f"{succes_text}")

    