from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Login(unittest.TestCase):
    def test_login_using_standard_user(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        print("Page tittle is:" + self.driver.title)

        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.NAME, "login-button").click()

        time.sleep(5)
        self.driver.save_screenshot("login_using_standard_user.png")
        self.driver.quit()

    def test_login_using_locked_user(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        print("Page tittle is:" + self.driver.title)

        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, 'user-name').send_keys('locked_out_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.NAME, "login-button").click()
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3'))

        time.sleep(5)
        self.driver.save_screenshot("login_using_locked_user.png")
        self.driver.quit()

    def test_login_using_problem_user(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        print("Page tittle is:" + self.driver.title)

        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, 'user-name').send_keys('problem_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.NAME, "login-button").click()
        if self.driver.find_element(By.CSS_SELECTOR, "img[alt='Sauce Labs Backpack']"):
            print("image displayed")
        else:
            print("image hidden")

    def test_login_using_performance_user(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        print("Page tittle is:" + self.driver.title)

        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, 'user-name').send_keys('performance_glitch_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.NAME, "login-button").click()

        delay = 3  # seconds
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.title')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        time.sleep(5)
        self.driver.save_screenshot("login_using_performance_user.png")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
