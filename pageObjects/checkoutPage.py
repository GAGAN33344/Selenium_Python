from selenium.webdriver.common.by import By

from pageObjects.confirmPage import confirmPage


class checkoutPage():

    def __init__(self, driver):
        self.driver = driver

    checkoutConfirm = (By.CSS_SELECTOR, ".btn.btn-success")

    def clickoncheckoutconfirm(self):
        self.driver.find_element(*checkoutPage.checkoutConfirm).click()
        confirmpage = confirmPage(self.driver)
        return confirmpage
