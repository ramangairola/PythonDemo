import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_fistmethod():
    msg = "Valar"
    assert msg == "Hi", "Failed as message is " + msg


@pytest.mark.xfail
def test_secondvalarmethod(setup):
    a = 4
    b = 6
    assert a + 2 == b, "Pass"
