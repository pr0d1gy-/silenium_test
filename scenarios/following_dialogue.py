from scenarios.base import BaseScenario
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import \
    presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class FollowingDialogueScenario(BaseScenario):

    def run(self):
        # Get the button for showing following dialogue
        try:
            following_button = WebDriverWait(self.browser, 10).until(
                presence_of_element_located(
                    (By.XPATH, '//*[@id="react-root"]/section/main/article/'
                               'header/section/ul/li[3]/a')
                )
            )
        except NoSuchElementException:
            following_button = self.get_x_el(
                '//*[@id="react-root"]/section/main/article/ul/li[3]/a')

        # Get total following count
        following_count_element = following_button.find_element(
            By.TAG_NAME, 'span')
        following_count = following_count_element.text
        # Set total following count
        try:
            self.app.following_count = int(following_count)
        except ValueError:
            self.app.following_count = 0

        # Click the button for showing the following dialogue
        following_button.click()

        # Ul with users list (li)
        following_ul = WebDriverWait(self.browser, 10).until(
            presence_of_element_located(
                (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/ul')
            )
        )

        # Scroll dialogue to the end for load all followings
        self.scroll_dialogue_to_end(following_ul)

    def scroll_dialogue_to_end(self, following_ul):
        # Following div for scrolling
        following_div = self.get_x_el(
            '/html/body/div[4]/div/div[2]/div/div[2]')

        # Function for counting loaded followings
        now_count = lambda: len(following_ul.find_elements(By.TAG_NAME, 'li'))  # noqa: E731,E501

        # Scroll while loaded count is not exact total count
        while now_count() < self.app.following_count:
            self.browser.execute_script(
                'arguments[0].scrollTo(0, 99999999)', following_div)
