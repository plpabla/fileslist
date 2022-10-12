import time
from behave import step
from selenium import webdriver
from django.urls import reverse

def resolve_url(url, root=None):
    if root is None:
        return url

    full_url = root + reverse(url) 
    return full_url   

@step("opened browser")
def my_step(context):
    opts = webdriver.FirefoxOptions()
    # opts.add_argument("--headless")
    context.browser = webdriver.Firefox(options=opts)
    # context.browser.implicitly_wait(3)
    
@step("I'm on the '{url}' page")
def my_step(context, url):
    context.browser.get(resolve_url(url, root=context.test.live_server_url))

@step("Page title contains '{expected_title}'")
def my_step(context, expected_title):
    assert False, "ToDo!"
    context.browser.quit()
