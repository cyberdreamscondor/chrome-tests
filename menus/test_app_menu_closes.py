"""The application menu can be closed again.

Closing must genuinely close. A menu left open sits on top of the UI that the
next interaction needs, so this protects every later test as much as itself.
"""


def test_app_menu_closes(chrome):
    chrome.menu.open()
    assert chrome.menu.is_open

    chrome.menu.close()

    assert not chrome.menu.is_open
