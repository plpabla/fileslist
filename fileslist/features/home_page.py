from selenium.webdriver.common.by import By
from django.urls import reverse

def resolve_url(url, root=None):
    if root is None:
        return url

    full_url = root + reverse(url)
    return full_url

class Page(object):
    def __init__(self, context):
        self.context = context

    def get_body(self):
        return self.context.browser.find_element(By.TAG_NAME, "body").text


class HomePage(Page):
    def __init__(self, context):
        super().__init__(context)
        self.context.browser.get(resolve_url("home", root=self.context.test.live_server_url))
