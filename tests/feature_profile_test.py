import allure
import random
import pytest

from base.base_test import BaseTest
@allure.feature("Profile Functionality ")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        random_number = random.randint(1, 100)


        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_open()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_open()
        self.personal_page.change_first_name(f"Test first name {random_number}")
        self.personal_page.change_middle_name(f"Test middle name {random_number}")
        self.personal_page.change_last_name(f"Test last name {random_number}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("Success")

