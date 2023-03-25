#Senaryo 1: Başarılı giriş
#n11 sitesine gittim
#Giriş yap butonuna tıkladım
#E-posta adresinizi girdim.
#Şifreyi girdim
#Giriş Yap" butonuna tıkladım
#Giriş işlemi başarılı testini gerçekleştirdin.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from pythonProject.PomProjectDemo.pages.loginpage import  LoginPage
from pythonProject.PomProjectDemo.pages.homepage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Chrome(executable_path="/tests/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver=self.driver

        driver.get("https://www.n11.com/giris-yap")

        login=LoginPage(driver)
        login.enter_username('mmjcrevolution@gmail.com')
        login.enter_password('12345678b')
        login.click_login()

        homepage=HomePage(driver)
        homepage.click_Welcome()
        homepage.click_Logout()

        #self.driver.find_element(By.ID, "email").send_keys("mmjcrevolution@gmail.com")
        #self.driver.find_element(By.ID, "password").send_keys("12345678b")
        #self.driver.find_element(By.ID, 'loginButton').click()
        #self.driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div/div/div[2]/div[5]/div[1]/a').click()
        #self.driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div/div/div[2]/div[5]/div[2]/div/a[10]').click()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('Test completed')

if __name__=='__main__':
    unittest.main()












