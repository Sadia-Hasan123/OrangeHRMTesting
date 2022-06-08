from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Contact:
    def test_contact_details(self):
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

        # click contact details
        driver.find_element(By.LINK_TEXT, 'Contact Details').click()
        # Input field

        Edit1 = driver.find_element(By.ID, 'btnSave')
        Edit1.click()

        addStreet1 = driver.find_element(By.ID, 'contact_street1')
        addStreet1.clear()
        addStreet1.send_keys('12,Halim Raod')

        addStreet2 = driver.find_element(By.ID, 'contact_street2')
        addStreet2.clear()
        addStreet2.send_keys('12, Mirpur Raod')

        city = driver.find_element(By.ID, 'contact_city')
        city.clear()
        city.send_keys('Dhaka')

        state = driver.find_element(By.ID, 'contact_province')
        state.clear()
        state.send_keys('Dhaka')

        Zip = driver.find_element(By.ID, 'contact_emp_zipcode')
        Zip.clear()
        Zip.send_keys('1234')

        country = driver.find_element(By.ID, 'contact_country')
        sel = Select(country)
        sel.select_by_value('BD')

        HomeTele = driver.find_element(By.ID, 'contact_emp_hm_telephone')
        HomeTele.clear()
        HomeTele.send_keys('27474858')

        Mobile = driver.find_element(By.ID, 'contact_emp_mobile')
        Mobile.clear()
        Mobile.send_keys('01829373783')

        wtele = driver.find_element(By.ID, 'contact_emp_work_telephone')
        wtele.clear()
        wtele.send_keys('23456744')

        wEmail = driver.find_element(By.ID, 'contact_emp_work_email')
        wEmail.clear()
        wEmail.send_keys('abc@gmail.com')

        oEmail = driver.find_element(By.ID, 'contact_emp_oth_email')
        oEmail.clear()
        oEmail.send_keys('bcd@gmail.com')
        time.sleep(3)

        Edit1 = driver.find_element(By.ID, 'btnSave')
        Edit1.click()

        time.sleep(3)

        #Add Attachment

        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()

        selectFile = driver.find_element(By.ID, 'ufile')
        selectFile.send_keys('C:\\Users\\Hp\\Pictures\\images.JPG')

        comment = driver.find_element(By.ID, 'txtAttDesc')
        comment.send_keys('hello')

        upload = driver.find_element(By.ID, 'btnSaveAttachment')
        upload.click()

        checkbox = driver.find_element(By.ID, 'attachmentsCheckAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
        time.sleep(2)

        delete = driver.find_element(By.ID, 'btnDeleteAttachment')
        delete.click()
        driver.close()


test_obj = Contact()
test_obj.test_contact_details()
