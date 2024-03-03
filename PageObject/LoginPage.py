from Locators.LoginPage import LoginLoc
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Helpers.LoginHelpers import Loginhelp
from PageObject.BasePage import BasePage


class Login(BasePage, Loginhelp):
    def Loginhelp(self, act_title):
        if act_title == Loginhelp.login_title:
            assert True
        else:
            assert False


    def login_page(self, username, password):

        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, LoginLoc.text_username_xpath).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
        LoginLoc.text_username_xpath)))

        self.driver.find_element(By.XPATH, LoginLoc.text_password_xpath).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
        LoginLoc.text_password_xpath)))

    def do_click(self):
        self.driver.find_element(By.XPATH, LoginLoc.text_login_button_xapth).click()
        self.driver.implicitly_wait(10)
