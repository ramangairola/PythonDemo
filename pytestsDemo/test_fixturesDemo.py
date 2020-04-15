import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixturemethod(self):
        print("Method")