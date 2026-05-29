from validators import validate_task


CATS = {1, 2, 3, 4, 5}
PRIOS = {1, 2, 3}


def good_form(**over):
    f = {
        'opis': 'jakies zadanie',
        'termin_wykonania': '2026-06-01',
        'status': 'do_zrobienia',
        'category_id': '1',
        'priority_id': '2',
    }
    f.update(over)
    return f


def test_valid_passes():
    data, errors = validate_task(good_form(), CATS, PRIOS)
    assert errors == {}
    assert data['category_id'] == 1


def test_empty_opis():
    _, errors = validate_task(good_form(opis=''), CATS, PRIOS)
    assert 'opis' in errors


def test_short_opis():
    _, errors = validate_task(good_form(opis='ab'), CATS, PRIOS)
    assert 'opis' in errors


def test_long_opis():
    _, errors = validate_task(good_form(opis='x' * 600), CATS, PRIOS)
    assert 'opis' in errors


def test_bad_date():
    _, errors = validate_task(good_form(termin_wykonania='01.06.2026'), CATS, PRIOS)
    assert 'termin_wykonania' in errors


def test_no_date():
    _, errors = validate_task(good_form(termin_wykonania=''), CATS, PRIOS)
    assert 'termin_wykonania' in errors


def test_bad_status():
    _, errors = validate_task(good_form(status='xxx'), CATS, PRIOS)
    assert 'status' in errors


def test_bad_category():
    _, errors = validate_task(good_form(category_id='99'), CATS, PRIOS)
    assert 'category_id' in errors


def test_category_not_int():
    _, errors = validate_task(good_form(category_id='abc'), CATS, PRIOS)
    assert 'category_id' in errors


def test_bad_priority():
    _, errors = validate_task(good_form(priority_id='99'), CATS, PRIOS)
    assert 'priority_id' in errors


def test_trim_opis():
    data, _ = validate_task(good_form(opis='   opis z paddingiem   '), CATS, PRIOS)
    assert data['opis'] == 'opis z paddingiem'
