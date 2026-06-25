from backend.utils.tension_curves import default_curve


def test_default_curve_has_beats():
    curve = default_curve()
    assert len(curve.beats) == 5
