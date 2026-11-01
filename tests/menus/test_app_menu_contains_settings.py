"""Opening the three-dot menu reveals the Settings entry.

Exercises the full native path: focus the window, click the three-dot button
by its UI Automation class, wait for the menu, then read its items.

The label comes from MenuItem rather than from a config: which entry we mean
is stable, and the string Chrome shows for it lives in one place in the
framework.
"""

from chrome_checks import check_menu_has_item, check_menu_open
from chrome_menu import MenuItem


def test_app_menu_contains_settings(chrome):
    chrome.menu.open()

    check_menu_open(chrome.menu)
    check_menu_has_item(chrome.menu, MenuItem.SETTINGS)
