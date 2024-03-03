import time

from selenium import  webdriver
from Locators.LoginPage import LoginLoc
from PageObject.LoginPage import Login
from TestCases.conftest import setup

from Helpers.LoginHelpers import Loginhelp
from Credentials.LoginCred import CredentialsLogin


class Test_login_001(CredentialsLogin, Loginhelp ):

    def test_login_page(self, setup ):
        self.driver = setup
        self.driver.get(CredentialsLogin.base_URL)
        self.driver.maximize_window()
        self.login = Login(self.driver)
        time.sleep(10)
        self.login.Loginhelp(self.login_title)
        self.login.login_page(CredentialsLogin.username, CredentialsLogin.password)
        self.click = self.login.do_click()
        time.sleep(10)







