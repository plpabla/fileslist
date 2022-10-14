from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    res = HttpResponse()
    res.write("<p>Hello!</p>")
    return res