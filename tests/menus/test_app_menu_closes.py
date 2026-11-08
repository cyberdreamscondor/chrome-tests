from chrome_checks import check_menu_closed, check_menu_open


def test_app_menu_closes(chrome):
    chrome.menu.open()
    check_menu_open(chrome.menu)

    chrome.menu.close()
    check_menu_closed(chrome.menu)
