from urllib import request
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

def test_root_url_resolves_to_home_page():
    page_found = reverse("home")

    assert page_found == r"/"

def test_home_page_renders_home_template(client):
    res = client.get(reverse("home"))
    print(f"\n*** response: {res.content.decode()}")
    assert False, "ToDo!"
    
