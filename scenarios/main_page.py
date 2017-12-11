from scenarios.base import BaseScenario


class MainPageScenario(BaseScenario):

    def run(self):
        self.browser.get(self.app.MAIN_PAGE_URL)
