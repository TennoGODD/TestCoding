import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class PersonalPage(BasePage):

    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    MIDDLE_NAME_FIELD = ("xpath", "//input[@name='middleName']")
    LAST_NAME_FIELD = ("xpath", "//input[@name='lastName']")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def change_first_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name_field.send_keys(Keys.CONTROL + "A")
            first_name_field.send_keys(Keys.DELETE)
            first_name_field.send_keys(new_name)
            self.firts_name = new_name

    def change_middle_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            middle_name_field = self.wait.until(EC.element_to_be_clickable(self.MIDDLE_NAME_FIELD))
            middle_name_field.send_keys(Keys.CONTROL + "A")
            middle_name_field.send_keys(Keys.DELETE)
            middle_name_field.send_keys(new_name)
            self.middle_name = new_name

    def change_last_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            last_name_field = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD))
            last_name_field.send_keys(Keys.CONTROL + "A")
            last_name_field.send_keys(Keys.DELETE)
            last_name_field.send_keys(new_name)
            self.last_name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Changes has been saved successfuly")
    def is_changes_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.firts_name))
        self.wait.until(EC.visibility_of_element_located(self.MIDDLE_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.MIDDLE_NAME_FIELD, self.middle_name))
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.LAST_NAME_FIELD, self.last_name))