from time import sleep

from scenarios.base import BaseScenario
from selenium.webdriver.common.by import By


class FollowingDialogueUnsubscribeScenario(BaseScenario):

    def run(self):
        if not self.app.unfollowing_list:
            return

        following_ul = self.get_x_el(
            '/html/body/div[4]/div/div[2]/div/div[2]/ul')

        return self.unsubscribe_followings(following_ul)

    def unsubscribe_followings(self, following_ul):
        while len(self.app.unfollowing_list) > 0:
            username = self.app.unfollowing_list.pop().strip()
            for following_li in following_ul.find_elements(By.TAG_NAME, 'li'):
                if self.check_to_unsubscribe(following_li, username):
                    self.unsubscribe(following_li)
        sleep(2)

    @staticmethod
    def check_to_unsubscribe(following_li, username):
        following_link = following_li.find_element_by_xpath(
            'div/div[1]/div/div[1]/a')
        return following_link.text.strip() == username

    @staticmethod
    def unsubscribe(following_li):
        unfollow_button = following_li.find_element_by_xpath(
            'div/div[2]/span/button')
        unfollow_button.click()
