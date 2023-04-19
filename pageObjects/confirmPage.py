from selenium.webdriver.common.by import By


class confirmPage():

    def __init__(self, driver):
        self.driver = driver

    countryInput = (By.ID, "country")
    indiaText = (By.LINK_TEXT, "India")
    termsCheckbox = (By.CSS_SELECTOR, ".checkbox")
    purchaseButton = (By.XPATH, "//input[@type='submit']")
    successAlert = (By.CSS_SELECTOR, ".alert-success")

    def getcountryfield(self):
        return self.driver.find_element(*confirmPage.countryInput)

    def getindiatext(self):
        return self.driver.find_element(*confirmPage.indiaText)

    def gettermscheckbox(self):
        return self.driver.find_element(*confirmPage.termsCheckbox)

    def getsubmit(self):
        return self.driver.find_element(*confirmPage.purchaseButton)

    def getsuccessalert(self):
        return self.driver.find_element(*confirmPage.successAlert)
