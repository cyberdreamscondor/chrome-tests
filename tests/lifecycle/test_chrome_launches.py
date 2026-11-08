from chrome_checks import check_browser_running, check_window_title_contains


def test_chrome_launches(chrome, test_input):
    check_browser_running(chrome)
    check_window_title_contains(chrome, test_input.asserts.title_contains)
