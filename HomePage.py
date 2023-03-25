class HomePage():

    def __init__(self,driver):
        self.driver=driver

        self.welcome_xpath='/html/body/div[1]/header/div/div/div/div[2]/div[5]/div[1]/a'
        self.loguot_xpath='/html/body/div[1]/header/div/div/div/div[2]/div[5]/div[2]/div/a[10]'

    def click_Welcome(self):
        self.driver.find_element(self.welcome_xpath).click()

    def click_Logout(self):
        self.driver.find_element(self.loguot_xpath).click()
