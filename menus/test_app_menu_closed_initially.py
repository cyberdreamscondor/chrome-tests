"""A closed application menu really is empty.

This is the validity check, and the reason the other menu tests mean anything.
Chrome's accessibility tree could in principle expose the menu model even while
the menu is shut. If it did, asserting that "Settings" exists would pass
without the menu ever opening - a test that cannot fail, which is worse than no
test at all. This pins the behaviour down.
"""


def test_app_menu_closed_initially(chrome):
    assert not chrome.menu.is_open
    assert chrome.menu.item_names() == []
