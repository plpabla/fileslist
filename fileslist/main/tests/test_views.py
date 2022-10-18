from django.http import HttpResponse
from django.urls import reverse
import logging
from pytest_django.asserts import assertTemplateUsed


import re
def assert_title_contains(response: HttpResponse, title:str) -> bool:
    regexp = re.compile(r"<title>.*%s.*</title>" % (title))
    assert regexp.search(response.content.decode()), f"'{title}' not found in the page title"

def test_root_url_resolves_to_home_page():
    page_found = reverse("home")

    assert page_found == r"/"

def test_home_page_renders_home_template(client):
    res = client.get(reverse("home"))
    logging.info(f"\nHome page response: {res.content.decode()}")
    
    assertTemplateUsed(res, "home.html")
    
def test_home_page_has_given_title(client):
    res = client.get(reverse("home"))

    assert_title_contains(res, "FilesList")