from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure

@allure.severity(allure.severity_level.NORMAL)
class TestLogin:
    @allure.severity(allure.severity_level.NORMAL)
    def test_LGN01(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print("Page tittle is:" + self.driver.title)


        self.driver.implicitly_wait(2)
        self.driver.find_element(By.NAME, 'username').send_keys('Admin')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(5)
        self.driver.save_screenshot("loginvalid.png")
        self.driver.quit()

    def test_login_LGN02(self):
        pytest.skip("not running")


    def test_login_LGN03(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print("Page tittle is:" + self.driver.title)

        self.driver.implicitly_wait(2)
        self.driver.find_element(By.NAME, 'username').send_keys('')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        print('error massage username is:', self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span').text)
        time.sleep(5)
        self.driver.save_screenshot("LGN03.png")
        self.driver.quit()
