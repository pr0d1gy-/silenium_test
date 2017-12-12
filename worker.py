from selenium.webdriver import Chrome, ChromeOptions

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
        capabilities = ChromeOptions()
        capabilities.add_argument('--disable-application-cache')
        # Set user agent
        capabilities.add_argument('--user-agent={}'.format(
            (
                cls.app.USER_AGENT if not cls.app.config.user_agent else
                cls.app.config.user_agent
            )
        ))
        # Set proxy server
        if cls.app.config.proxy_server:
            capabilities.add_argument('--proxy-server={}'.format(
                cls.app.config.proxy_server
            ))

        return capabilities.to_capabilities()

    @classmethod
    def start_scenarios(cls):
        for scenario_class in scenarios_list:
            scenario = scenario_class(cls.app, cls.app.browser)
            scenario.run()
