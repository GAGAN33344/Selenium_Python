from selenium.webdriver.common.by import By

from pageObjects.shopPage import shopPage


class homePage():

    def __init__(self, driver):
        self.driver = driver

    shopText = (By.XPATH, "//a[text()='Shop']")
    nameInput = (By.CSS_SELECTOR, "input[name='name']")
    emailInput = (By.NAME, "email")
    passwordInput = (By.ID, "exampleInputPassword1")
    iceCreamsCheckbox = (By.ID, "exampleCheck1")
    genderDropdown = (By.ID, "exampleFormControlSelect1")
    studentRadiobutton = (By.CSS_SELECTOR, "#inlineRadio1")
    submitButton = (By.XPATH, "//input[@value='Submit']")
    successAlert = (By.CLASS_NAME, "alert-success")
    exampleInput = (By.XPATH, "(//input[@name='name'])[2]")

    def getnameinput(self):
        return self.driver.find_element(*homePage.nameInput)

    def getemailinput(self):
        return self.driver.find_element(*homePage.emailInput)

    def getpasswordinput(self):
        return self.driver.find_element(*homePage.passwordInput)

    def getcheckbox(self):
        return self.driver.find_element(*homePage.iceCreamsCheckbox)

    def getgenderdropdown(self):
        return self.driver.find_element(*homePage.genderDropdown)

    def getstudentradiobutton(self):
        return self.driver.find_element(*homePage.studentRadiobutton)

    def getsubmitbutton(self):
        return self.driver.find_element(*homePage.submitButton)

    def getsuccessalert(self):
        return self.driver.find_element(*homePage.successAlert)

    def getexampletextbox(self):
        return self.driver.find_element(*homePage.exampleInput)

    def clickshoptext(self):
        self.driver.find_element(*homePage.shopText).click()
        shoppage = shopPage(self.driver)
        return shoppage