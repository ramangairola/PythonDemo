import pytest


@pytest.fixture(scope="class")
def setup():
    print("Before")
    yield
    print("After")


@pytest.fixture()
def dataLoad():
    return ["Raman", "Gairola"]


@pytest.fixture(params=[("Chrome", "Raman"), ("IE", "Chandler")])
def cross_browser(request):
    return request.param
