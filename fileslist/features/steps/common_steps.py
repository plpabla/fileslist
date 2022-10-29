import time
from behave import step
from django.urls import reverse
import logging
from home_page import HomePage

BUTTON_IDS = {"login": "id_login", "logout": "id_logut"}


# PAGES = {"home": HomePage, ...}

@step("I'm on the '{url}' page")
def my_step(context, url):
    # context.browser.get(resolve_url(url, root=context.test.live_server_url))
    # TODO - it should use factory to return correct page based on url
    context.page = HomePage(context)


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
