import time
from behave import step
from django.urls import reverse
import logging


def resolve_url(url, root=None):
    if root is None:
        return url

    full_url = root + reverse(url)
    return full_url


@step("opened browser")
def my_step(context):
    pass


@step("I'm on the '{url}' page")
def my_step(context, url):
    context.browser.get(resolve_url(url, root=context.test.live_server_url))


@step("Page title contains '{expected_title}'")
def my_step(context, expected_title):
    logging.info("TODO")
    assert True
    # assert False, "ToDo!"
