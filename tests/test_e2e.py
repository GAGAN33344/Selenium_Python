
from pageObjects.homePage import homePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        # //a[contains(@href, 'shop')] - Xpath
        # a[href*='shop'] - CSS
        homepage = homePage(self.driver)
        shoppage = homepage.clickshoptext()

        log.info("Getting the all cart titles")
        products = shoppage.getCartItemsText()
        i = -1
        for product in products:
            i = i +1
            CartText = product.text
            log.info("Cart text is : " + CartText)
            if CartText == "Blackberry":  # Getting Balckberry text
                shoppage.getAddButton()[i].click()  # After getting Blackberry text then click on Add
                break
        checkoutpage = shoppage.clickcheckout()

        confirmpage = checkoutpage.clickoncheckoutconfirm()
        log.info("Entering Country Name as in Ind")
        confirmpage.getcountryfield().send_keys("Ind")

        self.verifyLinkPresence(confirmpage.indiaText)

        confirmpage.getindiatext().click()
        confirmpage.gettermscheckbox().click()
        confirmpage.getsubmit().click()
        successAlert = confirmpage.getsuccessalert().text
        log.info("Text received from application is : " + successAlert)
        assert "Success! Thank you!" in successAlert