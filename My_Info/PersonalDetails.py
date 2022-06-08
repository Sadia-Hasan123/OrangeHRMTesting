from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Personal:
    def test_personal_details(self):
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
        time.sleep(2)

        # input

        Edit1 = driver.find_element(By.ID, 'btnSave')

        #checkbox = driver.find_element(By.XPATH, '//*[@id="btnDeleteAttachment"]')

        Edit1.click()
        Firstname = driver.find_element(By.XPATH, '//*[@id="personal_txtEmpFirstName"]')
        Firstname.clear()
        Firstname.send_keys('Sadia')
        #time.sleep(3)

        MiddleName = driver.find_element(By.XPATH, '//*[@id="personal_txtEmpMiddleName"]')
        MiddleName.clear()
        MiddleName.send_keys('Hasan')
        # time.sleep(3)

        Lastname = driver.find_element(By.XPATH, '//*[@id="personal_txtEmpLastName"]')
        Lastname.clear()
        Lastname.send_keys('Hima')
        # time.sleep(3)

        EmpId = driver.find_element(By.XPATH, '//*[@id="personal_txtEmployeeId"]')
        EmpId.clear()
        EmpId.send_keys('12345456')
        # time.sleep(3)

        OtherId = driver.find_element(By.XPATH, '//*[@id="personal_txtOtherID"]')
        OtherId.clear()
        OtherId.send_keys("54767565")
        # time.sleep(3)

        DriverLicenseNumber = driver.find_element(By.XPATH, '//*[@id="personal_txtLicenNo"]')
        DriverLicenseNumber.clear()
        DriverLicenseNumber.send_keys(23424)
        # time.sleep(3)

        SSNnumber = driver.find_element(By.XPATH, '//*[@id="personal_txtNICNo"]')
        SSNnumber.clear()
        SSNnumber.send_keys('87347')
        # time.sleep(3)

        SINnumber = driver.find_element(By.XPATH, '//*[@id="personal_txtSINNo"]')
        SINnumber.clear()
        SINnumber.send_keys('78689')
        # time.sleep(3)

        radio2 = driver.find_element(By.XPATH, '//*[@id="personal_optGender_2"]')
        status = radio2.is_selected()
        if not status:
            radio2.click()
        # time.sleep(3)

        maritalStatus = driver.find_element(By.ID, 'personal_cmbMarital')
        sel = Select(maritalStatus)
        sel.select_by_value('Single')
        time.sleep(2)

        Nationality = driver.find_element(By.ID, 'personal_cmbNation')
        sel2 = Select(Nationality)
        sel2.select_by_value("15")
        time.sleep(2)

        NickName = driver.find_element(By.XPATH, '//*[@id="personal_txtEmpNickName"]')
        NickName.clear()
        NickName.send_keys('Himu')

        Military = driver.find_element(By.XPATH, '//*[@id="personal_txtMilitarySer"]')
        Military.clear()
        Military.send_keys('sdsdffd')
        # time.sleep(3)

        Smoker = driver.find_element(By.ID, 'personal_chkSmokeFlag')
        status2 = Smoker.is_selected()
        if not status2:
            Smoker.click()
        time.sleep(2)

        LicenseExpDate = driver.find_element(By.XPATH, '//*[@id="personal_txtLicExpDate"]')
        LicenseExpDate.clear()
        LicenseExpDate.send_keys('1997-07-11')
        time.sleep(2)

        Dob = driver.find_element(By.XPATH, '//*[@id="personal_DOB"]')
        Dob.clear()
        Dob.send_keys('1997-07-11')
        time.sleep(2)

        Edit1.click()
        time.sleep(3)
        '''
        Edit2 = driver.find_element(By.ID, 'btnEditCustom')
        Edit2.click()
        time.sleep(2)

        Blood = driver.find_element(By.XPATH, '///*[@id="frmEmpCustomFields"]/ol/li/select')
        Bsel = Select(Blood)
        Bsel.select_by_value('A+')
        Edit2.click()
        time.sleep(2)
        '''

        add = driver.find_element(By.ID, 'btnAddAttachment')
        Delete = driver.find_element(By.ID, 'btnDeleteAttachment')
        add.click()

        selectFile = driver.find_element(By.ID, 'ufile')
        selectFile.send_keys('C:\\Users\\Hp\\Pictures\\images.JPG')

        comment = driver.find_element(By.ID, 'txtAttDesc')
        comment.send_keys('hello')

        upload = driver.find_element(By.ID, 'btnSaveAttachment')
        upload.click()

        checkbox = driver.find_element(By.XPATH, '//*[@id="tblAttachments"]/tbody/tr[1]/td[1]/input')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
        time.sleep(2)

        delete = driver.find_element(By.ID, 'btnDeleteAttachment')
        delete.click()

        driver.close()


test_obj = Personal()

test_obj.test_personal_details()
