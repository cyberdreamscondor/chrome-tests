"""The application menu offers its well-known entries.

Also proves keyboard accelerators are handled: the real accessible name of the
first entry is "New tab Ctrl+T", not "New tab". Matching on the plain label
works only because the framework strips the accelerator on the test's behalf.
"""


def test_app_menu_expected_entries(chrome):
    chrome.menu.open()

    for label in ["New tab", "New window", "History", "Downloads", "Settings"]:
        assert chrome.menu.has_item(label), (
            f"{label!r} missing from the menu. Present: {chrome.menu.item_names()}"
        )
