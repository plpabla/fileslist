import time
from behave import step
from django.urls import reverse
import logging

BUTTON_IDS = {"login": "id_login", "logout": "id_logut"}


def resolve_url(url, root=None):
    if root is None:
        return url

    full_url = root + reverse(url)
    return full_url


@step("I'm on the '{url}' page")
def my_step(context, url):
    context.browser.get(resolve_url(url, root=context.test.live_server_url))


@step("Page title contains '{expected_title}'")
def my_step(context, expected_title):
    assert expected_title in context.browser.title


@step("I'm logged out")
def my_step(context):
    pass


@step("I'm logged in")
def my_step(context):
    pass


@step("I see '{button}' button")
def my_step(context, button):
    logging.info(f"Searching for button: {BUTTON_IDS[button]}")
    assert False, "TO DO"
