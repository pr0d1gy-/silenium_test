from scenarios.base import BaseScenario
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import \
    presence_of_element_located
from selenium.webdriver.common.by import By


class ProfilePageScenario(BaseScenario):

    def run(self):
        # Close fade screen if exists
        try:
            fade_screen_close_button = WebDriverWait(self.browser, 10).until(
                presence_of_element_located(
                    (By.XPATH, '/html/body/div/div/button')
                )
            )
        except NoSuchElementException:
            pass
        else:
            fade_screen_close_button.click()

        # Click for profile link button
        link_button = self.get_x_el(
            '//*[@id="react-root"]/section/nav/div[2]/'
            'div/div/div[3]/div/div[3]/a')
        link_button.click()
