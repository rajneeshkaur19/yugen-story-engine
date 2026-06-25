from backend.services.restraint_filter import RestraintFilter


def test_restraint_filter_allows_clean_text():
    filter = RestraintFilter(restricted_terms=["violence"])
    assert filter.is_allowed("A peaceful scene")


def test_restraint_filter_blocks_restricted_text():
    filter = RestraintFilter(restricted_terms=["violence"])
    assert not filter.is_allowed("A scene with violence")
