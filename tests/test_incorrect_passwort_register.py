from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators

faker = Faker()


class Test:
    def test_incorrect_password_input(self, driver):
        email = faker.email()

        """используем пароль с количеством символов < 6"""
        password = '1234'
        print(email)

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

        """проверяем что на экране появилось предупреждение о недопустимом пароле"""
        warning_message = driver.find_element(By.XPATH, Locators.incorrect_password_warning).text
        assert warning_message == 'Некорректный пароль'
