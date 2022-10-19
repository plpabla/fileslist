from django.urls import reverse
import logging
from pytest_django.asserts import assertTemplateUsed
from custom_asserts import assert_title_contains


def test_root_url_resolves_to_home_page():
    page_found = reverse("home")

    assert page_found == r"/"


def test_home_page_renders_home_template(client):
    res = client.get(reverse("home"))
    
    assertTemplateUsed(res, "home.html")


def test_home_page_has_given_title(client):
    res = client.get(reverse("home"))

    assert_title_contains(res, "FilesList")