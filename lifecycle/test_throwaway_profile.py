"""The browser under test uses its own disposable profile.

Protects the safety property the whole framework depends on. Without an
isolated --user-data-dir, automation drives the real browser - real tabs, real
history, real logged-in sessions - and trips over "restore pages?" prompts.
"""


def test_throwaway_profile(chrome):
    profile = chrome.profile_directory

    assert profile.exists(), "the browser should have been given a profile directory"
    assert "test-conductor" in str(profile), f"not a framework-managed profile: {profile}"
