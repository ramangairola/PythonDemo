import pytest


@pytest.fixture(scope="class")
def setup():
    print("Before")
    yield
    print("After")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome","Rahul","shetty"), ("Firefox","shetty"), ("IE","SS")])
def crossBrowser(request):
    return request.param
