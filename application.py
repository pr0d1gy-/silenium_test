import os

from worker import Worker


class Application(object):

    USER_AGENT = 'Anonymous'
    BROWSER_SIZE = (1024, 768)

    MAIN_PAGE_URL = 'https://www.instagram.com/'

    browser = None
    following_list = None
    following_count = None

    def __init__(self, arguments):
        self.config = arguments

        self.check_config()

        self.following_list = []
        self.following_count = 0

    def check_config(self):
        if self.config.un_follow_only:
            if not self.config.un_follow:
                raise AttributeError('Un-follow option is required.')

        if self.config.un_follow:
            if not os.path.exists(self.config.un_follow):
                raise AttributeError('Un-follow file was not found.')
            self.read_unfollow_list()

    def run(self):
        Worker.set_application(self)
        Worker.start_browser()
        Worker.start_scenarios()

        self.close()

        if not self.config.un_follow_only:
            self.save_to_csv()

    def close(self):
        # Close browser
        if self.browser:
            self.browser.close()
            self.browser.quit()
            self.browser = None

    def save_to_csv(self):
        with open('{}.csv'.format(self.config.output), 'w') as csv:
            csv.write('\n'.join(self.following_list))

    def read_unfollow_list(self):
        with open(self.config.un_follow, 'r') as csv:
            self.unfollowing_list = csv.read().split('\n')
