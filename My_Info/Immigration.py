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

        passport = driver.find_element(By.ID, 'immigration_type_flag_1')
        status = passport.is_selected()
        if not status:
            passport.click()

        number = driver.find_element(By.ID, 'immigration_number')
        number.clear()
        number.send_keys('27836648283')

        Idate = driver.find_element(By.ID,'immigration_passport_issue_date')
        Idate.clear()
        Idate.send_keys('2022-05-11')

        Edate = driver.find_element(By.ID, 'immigration_passport_expire_date')
        Edate.clear()
        Edate.send_keys('2023-05-11')

        ElStatus = driver.find_element(By.ID, 'immigration_i9_status')
        ElStatus.clear()
        ElStatus.send_keys('eligible')

        Issue = driver.find_element(By.ID, 'immigration_country')
        sel = Select(Issue)
        sel.select_by_value('BD')

        Eldate = driver.find_element(By.ID, 'immigration_i9_review_date')
        Eldate.clear()
        Eldate.send_keys('2023-05-11')

        comments = driver.find_element(By.ID, 'immigration_comments')
        comments.clear()
        comments.send_keys('abcksjldfheuir')

        save = driver.find_element(By.ID, 'btnSave')
        save.click()

        # attachment

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


obj = Immigration()
obj.test_immigration_details()
