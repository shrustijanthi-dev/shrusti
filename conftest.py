import pytest


@pytest.fixture(scope="class")
def setup_zemicon(browser):
    page = browser.new_page()
    page.goto("https://zemicon.in/")
    yield page
    page.close()
ijkiuh
