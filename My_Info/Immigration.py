from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Immigration:
    def test_immigration_details(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://opensource-demo.orangehrmlive.com/")

        # Find Element
        username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # My_Info Action
        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        # My_info link click
        driver.find_element(By.LINK_TEXT, 'My Info').click()

        # click Dependents

        driver.find_element(By.LINK_TEXT, 'Immigration').click()

        add = driver.find_element(By.ID, 'btnAdd')
        add.click()

        cancel = driver.find_element(By.ID, 'btnCancel')
        cancel.click()

        add = driver.find_element(By.ID, 'btnAdd')
        add.click()

obj = Immigration()
obj.test_immigration_details()
