from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import checkoutPage


class shopPage():

    def __init__(self, driver):
        self.driver = driver

    productName = (By.CSS_SELECTOR, ".card-title a")
    productsFooterAddButton = (By.CSS_SELECTOR, ".btn.btn-info")
    checkoutButton = (By.CSS_SELECTOR, ".btn-primary")

    def getCartItemsText(self):
        return self.driver.find_elements(*shopPage.productName)

    def getAddButton(self):
        return self.driver.find_elements(*shopPage.productsFooterAddButton)

    def clickcheckout(self):
        self.driver.find_element(*shopPage.checkoutButton).click()
        checkoutpage = checkoutPage(self.driver)
        return checkoutpage