from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestLoginPage:

    def setup(self):
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)

    def test_login_in_account(self):
        self.loginPage.open()
        self.loginPage.enter_username()
        self.loginPage.enter_password()
        self.loginPage.click_on_login_button()
        self.dashboardPage.is_opened()