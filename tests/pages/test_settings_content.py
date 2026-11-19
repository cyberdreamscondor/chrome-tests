from chrome_checks import check_page_shows, check_page_title
from chrome_menu import MenuItem


def test_settings_shows_its_sections(chrome, test_input):
    chrome.menu.open()
    chrome.menu.click_item(MenuItem.SETTINGS)

    page = chrome.page(test_input.asserts.page_url)

    check_page_title(page, test_input.asserts.page_title)
    for section in test_input.asserts.page_sections:
        check_page_shows(page, section)
