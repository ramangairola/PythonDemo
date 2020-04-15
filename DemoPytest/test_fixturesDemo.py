import pytest


@pytest.mark.usefixtures("setup")
class Example:

    def test_fixturemethod(self):
        print("Method")
