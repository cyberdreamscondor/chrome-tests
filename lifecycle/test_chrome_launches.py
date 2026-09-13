"""Chrome starts and the framework finds its window.

The most basic end-to-end check there is. Reaching the assertion at all means
process launch, window discovery by process id, and the wait for the
accessibility tree have every one of them worked.
"""


def test_chrome_launches(chrome):
    assert chrome.is_running
    assert "Google Chrome" in chrome.title
