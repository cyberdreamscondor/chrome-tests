from chrome_checks import check_page_open
from chrome_menu import MenuItem


def test_settings_opens_from_the_app_menu(chrome, test_input):
    chrome.menu.open()
    chrome.menu.click_item(MenuItem.SETTINGS)

    check_page_open(chrome.devtools, test_input.asserts.page_url)
