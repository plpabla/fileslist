import time
from xmlrpc.client import Boolean
from selenium import webdriver

TAG_WEBBROWSER_REQUIRED = "webbrowser_required"
def create_browser() -> webdriver:
    opts = webdriver.FirefoxOptions()
    # opts.add_argument("--headless")
    # context.browser.implicitly_wait(3)
    return webdriver.Firefox(options=opts)

def webbrowser_required_in_scenario(scenario) -> Boolean:
    return TAG_WEBBROWSER_REQUIRED in [*scenario.tags, *scenario.feature.tags]
    

def before_scenario(context, scenario):
    if webbrowser_required_in_scenario(scenario):
        context.browser = create_browser()


def after_scenario(context, scenario):
    if webbrowser_required_in_scenario(scenario):
        time.sleep(3)
        context.browser.quit() 
