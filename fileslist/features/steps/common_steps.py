from behave import step

@step("opened browser")
def my_step(context):
    pass

@step("I'm on the '{url}' page")
def my_step(context, url):
    pass

@step("Page title contains '{expected_title}'")
def my_step(context, expected_title):
    pass
