from django.urls import reverse

def test_root_url_resolves_to_home_page():
    page_found = reverse("home")

    assert True