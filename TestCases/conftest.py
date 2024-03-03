#he conftest.py file in a pytest project is a special module where you can define fixtures, hooks,
# and other configurations that are shared across multiple test files.
#pytest --browser=firefox
#pytest --browser=chrome


from selenium import webdriver
import pytest



@pytest.fixture()
def setup(request):
    global driver
    browser_type = request.config.getoption("--browser")

    if browser_type == "chrome":
        driver = webdriver.Chrome()

    elif browser_type == "firefox":
        driver = webdriver.Firefox()
    return driver



def pytest_addoption(parser):
    parser.addoption( "--browser")


'''
@pytest
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("./Reports,", today.strftime("%y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Report_ {'%y%m%d%H%M'}.html"
    config.option.htmlpath = report_dir
    config.option.self_contained_html = True'''










