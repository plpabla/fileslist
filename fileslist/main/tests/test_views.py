from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from custom_asserts import assert_title_contains


def test_home_page_resolves_to_root():
    page_found = reverse("home")

    assert page_found == r"/"


def test_home_page_renders_home_template(client):
    res = client.get(reverse("home"))

    assertTemplateUsed(res, "home.html")


def test_home_page_has_given_title(client):
    res = client.get(reverse("home"))

    assert_title_contains(res, "FilesList")
