from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class EmergencyContact:
    def test_Emergencycontact_details(self):
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

        #Click Emergency contact

        driver.find_element(By.LINK_TEXT, 'Emergency Contacts').click()

        add = driver.find_element(By.ID, 'btnAddContact')
        add.click()

        name = driver.find_element(By.ID, 'emgcontacts_name')
        name.clear()
        name.send_keys('Kamrul Hasan')

        relationship = driver.find_element(By.ID, 'emgcontacts_relationship')
        relationship.clear()
        relationship.send_keys('Ftaher')

        Htele = driver.find_element(By.ID, 'emgcontacts_homePhone')
        Htele.clear()
        Htele.send_keys('28774839')

        Mobile = driver.find_element(By.ID, 'emgcontacts_mobilePhone')
        Mobile.clear()
        Mobile.send_keys('01928638888')

        WTele = driver.find_element(By.ID, 'emgcontacts_workPhone')
        WTele.clear()
        WTele.send_keys('23456789')

        Save = driver.find_element(By.ID, 'btnSaveEContact')
        Save.click()
        time.sleep(2)

        checkbox1 = driver.find_element(By.XPATH, '//*[@id="emgcontact_list"]/tbody/tr[5]/td[1]/input')
        status = checkbox1.is_selected()
        if not status:
            checkbox1.click()
        time.sleep(2)

        delete = driver.find_element(By.ID, 'delContactsBtn')
        delete.click()

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
        driver.close()


obj = EmergencyContact()
obj.test_Emergencycontact_details()
