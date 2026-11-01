"""A closed application menu really is empty.

The validity check, and the reason the other menu tests mean anything. If the
accessibility tree exposed the menu model while the menu was shut, asserting
that an entry exists would pass without the menu ever opening - a test that
cannot fail.

No config file: there is nothing here a suite would want to vary.
"""

from chrome_checks import check_menu_closed


def test_app_menu_closed_initially(chrome):
    check_menu_closed(chrome.menu)
