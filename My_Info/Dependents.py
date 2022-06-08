from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class dependents:
    def test_dependents_details(self):
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

        driver.find_element(By.LINK_TEXT, 'Dependents').click()

        add = driver.find_element(By.ID, 'btnAddDependent')
        add.click()

        cancel = driver.find_element(By.ID, 'btnCancel')
        cancel.click()

        add = driver.find_element(By.ID, 'btnAddDependent')
        add.click()

        Name = driver.find_element(By.ID, 'dependent_name')
        Name.clear()
        Name.send_keys('Brishti')

        relation = driver.find_element(By.ID, 'dependent_relationshipType')
        sel = Select(relation)
        sel.select_by_value('other')
        time.sleep(2)

        Dob = driver.find_element(By.ID, 'dependent_dateOfBirth')
        Dob.clear()
        Dob.send_keys('2015-03-12')
        time.sleep(2)

        save = driver.find_element(By.ID, 'btnSaveDependent')
        save.click()
        time.sleep(2)

        # add attachment

        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(2)

        cancel = driver.find_element(By.ID, 'cancelButton')
        cancel.click()
        time.sleep(2)

        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(2)

        selectFile = driver.find_element(By.ID, 'ufile')
        selectFile.send_keys('C:\\Users\\Hp\\Pictures\\images.JPG')
        time.sleep(2)

        comment = driver.find_element(By.ID, 'txtAttDesc')
        comment.send_keys('hello')

        upload = driver.find_element(By.ID, 'btnSaveAttachment')
        upload.click()
        time.sleep(2)

        checkbox = driver.find_element(By.ID, 'attachmentsCheckAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
        time.sleep(2)

        delete = driver.find_element(By.ID, 'btnDeleteAttachment')
        delete.click()
        time.sleep(2)


obj = dependents()
obj.test_dependents_details()
