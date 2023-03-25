#Senaryo 3: Geçersiz e-posta adresi formatı
#n11 sitesine git.
#giriş yap düğmesine tıkla
#Geçersiz bir e-posta adresi formatı girin (e-posta adresinde @ işareti yok).
#Şifrenizi girin.
#"Giriş Yap" butonuna tıkla
#Hata mesajı görüntülenirse, doğru formatta bir e-posta adresi girmelisin.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class N11LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.n11.com/giris-yap"
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "loginButton")
        self.error_message = (By.CSS_SELECTOR, ".error .errorMessage")

    def load(self):
        self.driver.get(self.url)

    def set_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text


# WebDriver'ı başlat
driver = webdriver.Chrome()

# n11 giriş sayfasını aç
login_page = N11LoginPage(driver)
login_page.load()

# Geçersiz bir e-posta adresi formatı girin
login_page.set_email("mmjcrevolutiongmail.com")

# Şifrenizi girin
login_page.set_password("12345678b")

# "Giriş Yap" düğmesine tıklayın
login_page.click_login_button()


try:
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(login_page.error_message))
    error_message = login_page.get_error_message()
    print("Hata Mesajı:", error_message)
except:
    print("Başarılı Giriş")

# WebDriver'ı kapat
driver.quit()
