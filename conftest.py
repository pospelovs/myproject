import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='None',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
    browser = webdriver.Chrome(options=options)
    language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    browser.get(link)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()

