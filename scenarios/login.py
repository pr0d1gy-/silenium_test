from time import sleep
from selenium.common.exceptions import NoSuchElementException

from scenarios.base import BaseScenario


class LoginScenario(BaseScenario):

    def run(self):
        # Switch to login form
        enter_button = self.get_x_el(
            '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
        enter_button.click()

        # Enter username
        input_username = self.get_x_el(
            '//*[@id="react-root"]/section/main/article/div[2]'
            '/div[1]/div/form/div[1]/div/input')
        input_username.send_keys(self.app.config.username)

        # Enter password
        input_password = self.get_x_el(
            '//*[@id="react-root"]/section/main/article/div[2]/'
            'div[1]/div/form/div[2]/div/input')
        input_password.send_keys(self.app.config.password)

        # Submit form
        input_submit = self.get_x_el(
            '//*[@id="react-root"]/section/main/article/div[2]/'
            'div[1]/div/form/span/button')
        input_submit.click()

        # Check success login
        try:
            sleep(2)
            error = self.get_x_el('//*[@id="slfErrorAlert"]')
            if error.text:
                raise AttributeError(error.text)
        except NoSuchElementException:
            pass
