import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators


class Test:
    @pytest.mark.parametrize('link_to_constructor', [Locators.constructor_link, Locators.logo_link])
    def test_open_constructor_from_account_page_button(self, driver, link_to_constructor):
        email = 'burger_enjoyer@yandex.kz'
        password = '123456'
        """переходим к форме авторизации через кнопку на главной и авторизуемся"""
        driver.find_element(By.XPATH, Locators.signin_button_from_main_page).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, Locators.signin_form)))
        driver.find_element(By.XPATH, Locators.email_input_signin).send_keys(email)
        driver.find_element(By.XPATH, Locators.password_input_signin).send_keys(password)
        driver.find_element(By.XPATH, Locators.signin_button).click()

        """переходим в личный кабинет"""
        driver.find_element(By.XPATH, Locators.account_page_open_link).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, Locators.order_history_link)))

        """ переходим в конструктор """
        driver.find_element(By.XPATH, link_to_constructor).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, Locators.constructor_header)))

        """проверяем что перешли в конструктор"""
        element = driver.find_element(By.XPATH, Locators.constructor_header).text
        assert element == 'Соберите бургер'
