from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Experience:
    def test_experience_details(self):
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

        driver.find_element(By.LINK_TEXT, 'Qualifications').click()

        # Add work experience

        add = driver.find_element(By.ID, 'addWorkExperience')
        add.click()

        cancel = driver.find_element(By.ID, 'btnWorkExpCancel')
        cancel.click()

        add = driver.find_element(By.ID, 'addWorkExperience')
        add.click()

        company = driver.find_element(By.ID, 'experience_employer')
        company.clear()
        company.send_keys('Abc')

        job = driver.find_element(By.ID, 'experience_jobtitle')
        job.clear()
        job.send_keys('SQA Tester')

        FromDate = driver.find_element(By.ID, 'experience_from_date')
        FromDate.clear()
        FromDate.send_keys('2019-05-11')

        TDate = driver.find_element(By.ID, 'experience_to_date')
        TDate.clear()
        TDate.send_keys('2022-05-11')

        comment = driver.find_element(By.ID, 'experience_comments')
        comment.clear()
        comment.send_keys('astrfhjgkhj')

        save = driver.find_element(By.ID, 'btnWorkExpSave')
        save.click()

        # Education

        add2 = driver.find_element(By.ID, 'addEducation')
        add2.click()

        cancel2 = driver.find_element(By.ID, 'btnEducationCancel')
        cancel2.click()

        add2 = driver.find_element(By.ID, 'addEducation')
        add2.click()

        level = driver.find_element(By.ID, 'education_code')
        sel = Select(level)
        sel.select_by_value('4')

        Institute = driver.find_element(By.ID, 'education_institute')
        Institute.clear()
        Institute.send_keys('ULab')

        Major = driver.find_element(By.ID, 'education_major')
        Major.clear()
        Major.send_keys('CSE')

        year = driver.find_element(By.ID, 'education_year')
        year.clear()
        year.send_keys('2021')

        Gpa = driver.find_element(By.ID, 'education_gpa')
        Gpa.clear()
        Gpa.send_keys('3.50')

        Sdate = driver.find_element(By.ID, 'education_start_date')
        Sdate.clear()
        Sdate.send_keys('2016-02-01')

        Edate = driver.find_element(By.ID, 'education_end_date')
        Edate.clear()
        Edate.send_keys('2021-02-01')

        save2 = driver.find_element(By.ID, 'btnEducationSave')
        save2.click()
        time.sleep(2)

        # add skills

        add3 = driver.find_element(By.ID, 'addSkill')
        add3.click()
        time.sleep(2)

        skill = driver.find_element(By.ID, 'skill_code')
        sel2 = Select(skill)
        sel2.select_by_value('2')

        yearOfExp = driver.find_element(By.ID,'skill_years_of_exp')
        yearOfExp.clear()
        yearOfExp.send_keys('5')

        comment2 = driver.find_element(By.ID, 'skill_comments')
        comment2.clear()
        comment2.send_keys('cjdhkdj')

        save3 = driver.find_element(By.ID, 'btnSkillSave')
        save3.click()
        time.sleep(2)

        # Language

        add4 = driver.find_element(By.ID, 'addLanguage')
        add4.click()

        language = driver.find_element(By.ID, 'language_code')
        sel3 = Select(language)
        sel3.select_by_value('3')

        fluency = driver.find_element(By.ID, 'language_lang_type')
        sel4 = Select(fluency)
        sel4.select_by_visible_text('Speaking')

        competency = driver.find_element(By.ID, 'language_competency')
        sel5 = Select(competency)
        sel5.select_by_value('3')

        comment3 = driver.find_element(By.ID, 'language_comments')
        comment3.clear()
        comment3.send_keys('aksjdhaskdj')

        save4 = driver.find_element(By.ID, 'btnLanguageSave')
        save4.click()
        time.sleep(2)

        #License

        add5 = driver.find_element(By.ID, 'addLicense')
        add5.click()

        ltype = driver.find_element(By.ID, 'license_code')
        sel6 = Select(ltype)
        sel6.select_by_value('4')

        lNumber = driver.find_element(By.ID, 'license_license_no')
        lNumber.clear()
        lNumber.send_keys('263738273')

        Idate = driver.find_element(By.ID, 'license_date')
        Idate.clear()
        Idate.send_keys('2021-05-11')

        EXdate = driver.find_element(By.ID, 'license_renewal_date')
        EXdate.clear()
        EXdate.send_keys('2023-05-11')

        save5 = driver.find_element(By.ID, 'btnLicenseSave')
        save5.click()
        time.sleep(2)

        # attachment

        add6 = driver.find_element(By.ID, 'btnAddAttachment')
        add6.click()
        time.sleep(2)

        cancel = driver.find_element(By.ID, 'cancelButton')
        cancel.click()
        time.sleep(2)

        add6 = driver.find_element(By.ID, 'btnAddAttachment')
        add6.click()
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


obj = Experience()
obj.test_experience_details()