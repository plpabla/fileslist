import time
import os
from pathlib import Path
import logging
from selenium import webdriver
from behave.model import Status

TAG_WEBBROWSER_REQUIRED = "webbrowser_required"

def webbrowser_required_in_scenario(scenario) -> bool:
    return TAG_WEBBROWSER_REQUIRED in [*scenario.tags, *scenario.feature.tags]


def create_browser() -> webdriver:
    opts = webdriver.FirefoxOptions()
    # opts.add_argument("--headless")
    # context.browser.implicitly_wait(3)
    return webdriver.Firefox(options=opts)
    

def setup_logger() -> None:
    BASE_DIR = Path(__file__).resolve().parent
    LOG_DIR = os.path.join(BASE_DIR, "logs")
    run_id = os.environ.get("RUN_ID","manual")

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    filename = os.path.join(LOG_DIR,f"{run_id}_behave.log")
    
    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s - %(levelname)s: %(message)s",
        filename=filename,
        )

    logging.info(f"=== Starting new test suite ===")


def before_all(context):
    setup_logger()

def before_scenario(context, scenario):
    if webbrowser_required_in_scenario(scenario):
        context.browser = create_browser()


def after_scenario(context, scenario):
    if webbrowser_required_in_scenario(scenario):
        time.sleep(3)
        context.browser.quit() 

    if scenario.status == Status.failed:
        logging.error(f"Scenario {scenario.feature.name}-{scenario.name} failed")