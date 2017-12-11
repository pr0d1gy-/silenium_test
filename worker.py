from selenium.webdriver import PhantomJS, DesiredCapabilities, Chrome, ChromeOptions

from scenarios import scenarios_list


class Worker(object):

    app = None

    @classmethod
    def set_application(cls, app):
        cls.app = app

    @classmethod
    def start_browser(cls):
        cls.app.browser = Chrome(
            executable_path='./chromedriver',
            desired_capabilities=cls.default_capabilities()
        )
        cls.app.browser.set_window_size(*cls.app.BROWSER_SIZE)

    @classmethod
    def default_capabilities(cls):
        return ChromeOptions().to_capabilities()

    @classmethod
    def start_scenarios(cls):
        for scenario_class in scenarios_list:
            scenario = scenario_class(cls.app, cls.app.browser)
            scenario.run()
