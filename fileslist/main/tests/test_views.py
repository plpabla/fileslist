from django.urls import reverse
import logging
from pytest_django.asserts import assertTemplateUsed

def test_root_url_resolves_to_home_page():
    page_found = reverse("home")

    assert page_found == r"/"

def test_home_page_renders_home_template(client):
    res = client.get(reverse("home"))
    logging.info(f"\nHome page response: {res.content.decode()}")
    
    assertTemplateUsed(res, "home.html")
    
