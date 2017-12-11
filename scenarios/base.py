class BaseScenario(object):

    def __init__(self, app, browser):
        self.app = app
        self.browser = browser

    def get_x_el(self, xpath):
        return self.browser.find_element_by_xpath(xpath)

    def run(self):
        raise NotImplementedError()
