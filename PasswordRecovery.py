#Senaryo 4: Şifre kurtarma
#n11 sitesine gidin.
#giriş yap düğmesine tıkla
#"Şifrenizi mi unuttunuz?" bağlantısına tıkla
#E-posta adresinizi girin.
#"Şifremi Kurtar" düğmesine tıklayın.
#E-posta adresinize bir şifre sıfırlama bağlantısı gönderilecek
#E-postanızı kontrol edin ve bağlantıya tıklayarak şifreni sıfırla
#Yeni şifrenizle giriş yapın.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.n11.com/giris-yap"
        self.forgot_password_link = (By.LINK_TEXT, "Şifrenizi mi unuttunuz?")
        self.email_input = (By.ID, "email")
        self.reset_password_button = (By.ID, "resetPasswordButton")

    def load(self):
        self.driver.get(self.url)

    def click_forgot_password_link(self):
        self.driver.find_element(*self.forgot_password_link).click()

    def set_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def click_reset_password_button(self):
        self.driver.find_element(*self.reset_password_button).click()

# WebDriver'ı başlat
driver = webdriver.Chrome()

# n11 giriş sayfasını aç
login_page = LoginPage(driver)
login_page.load()

# "Şifrenizi mi unuttunuz?" bağlantısına tıkla
login_page.click_forgot_password_link()

# E-posta adresinizi girin
login_page.set_email("ornek_email@ornek.com")

# "Şifremi Kurtar" düğmesine tıklayın
login_page.click_reset_password_button()



# Yeni şifrenizle giriş yapın
# Burada e-postayı kontrol ederek yeni şifremizi alabiliriz ve yeni şifreyle giriş yapabiliriz.

# WebDriver'ı kapat
driver.quit()