from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators

faker = Faker()


class Test:
    def test_registration_check_account_page(self, driver):
        email = faker.email()
        password = '123456'
        """заходим в личный кабинет без авторизации и попадаем на форму для входа"""
        driver.find_element(By.XPATH, Locators.account_page_open_link).click()

        """прокручиваем страниицу до ссылки на страницу регистрации и кликаем на нее"""
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, 'Auth_login__3hAey')))
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div')
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.find_element(By.XPATH, Locators.register_page_link).click()

        """регистрируемся"""
        driver.find_element(By.XPATH, Locators.name_input_register).send_keys('Test')
        driver.find_element(By.XPATH, Locators.email_input_register).send_keys(email)
        driver.find_element(By.XPATH, Locators.password_input_register).send_keys(password)
        driver.find_element(By.XPATH, Locators.registration_button).click()

        """переходим в личный кабинет для входа с готовым юзером и логинимся"""
        driver.find_element(By.XPATH, Locators.account_page_open_link).click()
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
