from scenarios.base import BaseScenario
from selenium.webdriver.common.by import By


class FollowingDialogueParseScenario(BaseScenario):

    def run(self):
        if self.app.config.un_follow_only:
            return

        following_ul = self.get_x_el(
            '/html/body/div[4]/div/div[2]/div/div[2]/ul')

        return self.parse_following_list(following_ul)

    def parse_following_list(self, following_ul):
        for following_li in following_ul.find_elements(By.TAG_NAME, 'li'):
            self.parse_following_li(following_li)

    def parse_following_li(self, following_li):
        # Get link to following user
        following_link = following_li.find_element_by_xpath(
            'div/div[1]/div/div[1]/a')

        # Get following username and add to the list of users
        username = following_link.text
        self.app.following_list.append(username)
