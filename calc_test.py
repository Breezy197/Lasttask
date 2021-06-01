from calc import translation

digit = 10


def test_translation_from_m_to_dm():
    assert translation(digit, "m", "dm") == 100.0


def test_translation_from_dm_to_m():
    assert translation(digit, "dm", "m") == 1.0


def test_translation_from_mm_to_km():
    assert translation(digit, "cm", "km") == 0.00010


def test_translation_from_dm_to_km():
    assert translation(digit, "dm", "km") == 0.0010
