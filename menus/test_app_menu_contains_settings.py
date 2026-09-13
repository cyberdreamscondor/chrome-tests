"""Opening the three-dot menu reveals the Settings entry.

The prototype test this phase of the framework was built to serve. It exercises
the full native path: focus the window, click the three-dot button by its UI
Automation class, wait for the menu to appear, then read its items.
"""


def test_app_menu_contains_settings(chrome):
    chrome.menu.open()

    assert chrome.menu.is_open
    assert chrome.menu.has_item("Settings")
