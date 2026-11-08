from chrome_checks import check_profile_isolated


def test_throwaway_profile(chrome, test_input):
    check_profile_isolated(chrome, test_input.asserts.profile_marker)
