"""The browser under test uses its own disposable profile.

Protects the safety property the whole framework depends on. Without an
isolated profile directory, automation drives the real browser: real tabs,
real history, real logged-in sessions.
"""

from chrome_checks import check_profile_isolated


def test_throwaway_profile(chrome, config):
    check_profile_isolated(chrome, config.expected["profile_marker"])
