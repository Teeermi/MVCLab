from models import Task


def test_index(client):
    r = client.get('/')
    assert r.status_code == 200


def test_anon_cant_add(client):
    r = client.get('/add')
    assert r.status_code == 302
    assert '/login' in r.headers['Location']


def test_anon_cant_delete(client, tmp_data):
    Task.create('x', '2026-06-01', 'do_zrobienia', 1, 1)
    r = client.post('/delete/1')
    assert r.status_code == 302
    assert Task.get_by_id(1) is not None


def test_login_ok(client):
    r = client.post('/login', data={'username': 'admin', 'password': 'haslo123'})
    assert r.status_code == 302


def test_login_bad(client):
    r = client.post('/login', data={'username': 'admin', 'password': 'zle'}, follow_redirects=True)
    assert b'Bledny login' in r.data


def test_add_task(logged_client, tmp_data):
    r = logged_client.post('/add', data={
        'opis': 'nowe zadanie',
        'termin_wykonania': '2026-07-01',
        'status': 'do_zrobienia',
        'category_id': '1',
        'priority_id': '2',
    })
    assert r.status_code == 302
    assert len(Task.get_all()) == 1


def test_add_invalid(logged_client, tmp_data):
    r = logged_client.post('/add', data={
        'opis': 'x',
        'termin_wykonania': 'zle',
        'status': 'do_zrobienia',
        'category_id': '1',
        'priority_id': '2',
    })
    assert r.status_code == 200
    assert Task.get_all() == []


def test_edit(logged_client, tmp_data):
    Task.create('stary opis', '2026-06-01', 'do_zrobienia', 1, 1)
    r = logged_client.post('/edit/1', data={
        'opis': 'nowy opis',
        'termin_wykonania': '2026-08-15',
        'status': 'w_trakcie',
        'category_id': '2',
        'priority_id': '3',
    })
    assert r.status_code == 302
    assert Task.get_by_id(1).opis == 'nowy opis'


def test_delete(logged_client, tmp_data):
    Task.create('do usuniecia', '2026-06-01', 'do_zrobienia', 1, 1)
    r = logged_client.post('/delete/1')
    assert r.status_code == 302
    assert Task.get_by_id(1) is None


def test_delete_get_not_allowed(logged_client, tmp_data):
    Task.create('x', '2026-06-01', 'do_zrobienia', 1, 1)
    r = logged_client.get('/delete/1')
    assert r.status_code == 405


def test_view_missing(client):
    r = client.get('/task/999')
    assert r.status_code == 302


def test_search_in_index(logged_client, tmp_data):
    Task.create('kupic chleb', '2026-06-01', 'do_zrobienia', 3, 1)
    Task.create('zrobic kawe', '2026-06-02', 'do_zrobienia', 1, 1)
    r = logged_client.get('/?q=chleb')
    assert b'chleb' in r.data
    assert b'kawe' not in r.data


def test_logout(logged_client):
    r = logged_client.post('/logout')
    assert r.status_code == 302
    r2 = logged_client.get('/add')
    assert '/login' in r2.headers['Location']
