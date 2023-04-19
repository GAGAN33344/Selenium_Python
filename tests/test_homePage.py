import time

import pytest

from pageObjects.homePage import homePage
from testData.homePageData import homePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        log = self.getLogger()
        homepage = homePage(self.driver)
        log.info("Name is : " + getData["name"])
        homepage.getnameinput().send_keys(getData["name"]) # Name Field
        log.info("emailID is : " + getData["emailID"])
        homepage.getemailinput().send_keys(getData["emailID"]) # Email Field
        homepage.getpasswordinput().send_keys(getData["password"]) # Password Field
        homepage.getcheckbox().click() # click Icon

        log.info("Gender is : " + getData["gender"])
        self.selectValueByTextThroughDropdown(homepage.getgenderdropdown(), getData["gender"])

        homepage.getstudentradiobutton().click()
        homepage.getsubmitbutton().click()

        successMessage = homepage.getsuccessalert().text
        print(successMessage)
        assert "Success!" in successMessage
        homepage.getexampletextbox().clear()
        homepage.getexampletextbox().send_keys(getData["exampleText"])
        #time.sleep(4)
        self.driver.refresh()

    @pytest.fixture(params=homePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param