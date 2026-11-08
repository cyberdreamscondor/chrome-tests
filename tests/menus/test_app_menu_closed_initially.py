from chrome_checks import check_menu_closed


def test_app_menu_closed_initially(chrome):
    check_menu_closed(chrome.menu)
