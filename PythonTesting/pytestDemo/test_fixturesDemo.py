import pytest


# @pytest.fixture
# def setup():
#     print("I will execute script first")
#     yield
#     print("I will be execute at last")

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute fiture demo methods")

    def test_fixtureDemo2(self):
        print("I will execute fiture2 demo methods")

    def test_fixtureDemo3(self):
        print("I will execute fiture3 demo methods")

    def test_fixtureDemo4(self):
        print("I will execute fiture4 demo methods")