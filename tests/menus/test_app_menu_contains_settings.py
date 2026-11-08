from chrome_checks import check_menu_has_item, check_menu_open
from chrome_menu import MenuItem


def test_app_menu_contains_settings(chrome):
    chrome.menu.open()

    check_menu_open(chrome.menu)
    check_menu_has_item(chrome.menu, MenuItem.SETTINGS)
