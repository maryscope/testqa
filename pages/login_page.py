import allure

from pages.basePage import BasePage
from data.links import Links

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    LOGIN_BUTTON = ("xpath", "//button[@type='submit']")
    FORGOT_PASSWORD_LINK = ("xpath", "//p[contains(@class, 'orangehrm-login-forgot-header')]")

    @allure.step("Ввод логина")
    def enter_username(self):
        self.helper.enter_text(self.USERNAME_FIELD, self.data.USERNAME, check_value=True)

    @allure.step("Ввод пароля")
    def enter_password(self):
        self.helper.enter_text(self.PASSWORD_FIELD, self.data.PASSWORD)

    @allure.step("Клик на кнопку логина")
    def click_on_login_button(self):
        self.helper.click_on(self.LOGIN_BUTTON, "Login button was not clicked")