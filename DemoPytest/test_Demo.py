import pytest


def test_fistmethod():
    print("YO")

@pytest.mark.smoke
def test_secondvalarmethod():
    print("Mama")