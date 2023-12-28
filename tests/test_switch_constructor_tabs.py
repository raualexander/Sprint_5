from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators


class Test:

    def test_switch_to_sauces(self, driver):
        """переходим к вкладке 'соусы' """
        driver.find_element(By.XPATH, Locators.sauces).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, Locators.sauce_item)))
        """выбираем и кликаем на первый отобразившийся элемент"""
        driver.find_element(By.XPATH, Locators.sauce_item).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, Locators.item_name_in_card)))
        """проверяем что это соус"""
        element = driver.find_element(By.XPATH, Locators.item_name_in_card).text
        assert 'Соус' in element

    def test_switch_to_fillings(self, driver):
        """переходим к вкладке 'булки' """
        driver.find_element(By.XPATH, Locators.fillings).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, Locators.fillings_item)))
        """выбираем и кликаем на первый отобразившийся элемент"""
        driver.find_element(By.XPATH, Locators.fillings_item).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, Locators.item_name_in_card)))
        """проверяем что открылась карточка с начинкой"""
        element = driver.find_element(By.XPATH, Locators.item_name_in_card).text
        assert 'Мясо' in element

    def test_switch_to_buns(self, driver):
        """сначала выбираем вкладку 'начинки' т.к булки выбраны по дефолту """
        driver.find_element(By.XPATH, Locators.fillings).click()
        """переходим к булкам"""
        driver.find_element(By.XPATH, Locators.buns).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, Locators.buns_item)))
        """выбираем и кликаем на первый отобразившийся элемент"""
        driver.find_element(By.XPATH, Locators.buns_item).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, Locators.item_name_in_card)))
        """проверяем что открылась карточка с булкой"""
        element = driver.find_element(By.XPATH, Locators.item_name_in_card).text
        assert 'булка' in element
