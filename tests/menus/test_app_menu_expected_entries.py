from chrome_checks import check_menu_has_items


def test_app_menu_expected_entries(chrome, test_input):
    chrome.menu.open()

    check_menu_has_items(chrome.menu, test_input.asserts.menu_items)
