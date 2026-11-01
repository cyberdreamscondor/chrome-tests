"""Chrome starts and the framework finds its window.

The most basic end-to-end check. Reaching the checks at all means process
launch, window discovery by process id, and the wait for the accessibility
tree have every one of them worked.
"""

from chrome_checks import check_browser_running, check_window_title_contains


def test_chrome_launches(chrome, config):
    check_browser_running(chrome)
    check_window_title_contains(chrome, config.expected["title_contains"])
