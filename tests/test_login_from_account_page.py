from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators


class Test:
    def test_login_from_account_page(self, driver):
        email = 'burger_enjoyer@yandex.kz'
        password = '123456'
        """заходим в личный кабинет и авторизуемся"""
        driver.find_element(By.XPATH, Locators.account_page_open_link).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, Locators.signin_form)))
        driver.find_element(By.XPATH, Locators.email_input_signin).send_keys(email)
        driver.find_element(By.XPATH, Locators.password_input_signin).send_keys(password)
        driver.find_element(By.XPATH, Locators.signin_button).click()

        """переходим в личный кабинет"""
        driver.find_element(By.XPATH, Locators.account_page_open_link).click()

        """ждем пока страничка отобразится"""
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, Locators.order_history_link)))

        """проверяем что страница профиля открылась (она доступна только авторизованным)"""
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/account/profile'