"""The application menu offers the entries this suite cares about.

Which entries matter is a decision of this suite, so the list lives in the
config. It names them symbolically (SETTINGS, not "Settings"), so the label
Chrome actually shows still exists in exactly one place - MenuItem.

A typo in the config raises KeyError naming the bad entry, rather than
silently becoming a literal label that is then reported as missing.
"""

from chrome_checks import check_menu_has_items
from chrome_menu import MenuItem


def test_app_menu_expected_entries(chrome, config):
    chrome.menu.open()

    expected = [MenuItem[name] for name in config.expected["menu_items"]]
    check_menu_has_items(chrome.menu, expected)
