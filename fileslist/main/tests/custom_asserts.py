from django.http import HttpResponse
import re


def assert_title_contains(response: HttpResponse, title: str) -> bool:
    regexp = re.compile(r"<title>.*%s.*</title>" % (title))
    assert regexp.search(
        response.content.decode()
    ), f"'{title}' not found in the page title"
