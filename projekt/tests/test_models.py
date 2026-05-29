from models import Task, Category, Priority, User


def test_categories_count():
    assert len(Category.get_all()) == 5


def test_priorities_count():
    assert len(Priority.get_all()) == 3


def test_category_lookup():
    assert Category.get_by_id(1).nazwa == 'Dom'
    assert Category.get_by_id(99) is None


def test_priority_lookup():
    assert Priority.get_by_id(3).nazwa == 'Wysoki'
    assert Priority.get_by_id(99) is None


def test_task_create(tmp_data):
    t = Task.create('zrobic cos', '2026-06-01', 'do_zrobienia', 1, 2)
    assert t.id == 1
    assert Task.get_by_id(1).opis == 'zrobic cos'


def test_task_ids_increment(tmp_data):
    Task.create('a', '2026-06-01', 'do_zrobienia', 1, 1)
    Task.create('b', '2026-06-02', 'do_zrobienia', 1, 1)
    tasks = Task.get_all()
    assert [t.id for t in tasks] == [1, 2]


def test_task_update(tmp_data):
    Task.create('stary', '2026-06-01', 'do_zrobienia', 1, 1)
    assert Task.update(1, 'nowy', '2026-06-02', 'w_trakcie', 2, 3)
    t = Task.get_by_id(1)
    assert t.opis == 'nowy'
    assert t.status == 'w_trakcie'


def test_task_update_missing(tmp_data):
    assert Task.update(999, 'x', '2026-06-01', 'do_zrobienia', 1, 1) is False


def test_task_delete(tmp_data):
    Task.create('do usuniecia', '2026-06-01', 'do_zrobienia', 1, 1)
    assert Task.delete(1) is True
    assert Task.get_by_id(1) is None


def test_task_delete_missing(tmp_data):
    assert Task.delete(999) is False


def test_filter_status(tmp_data):
    Task.create('a', '2026-06-01', 'do_zrobienia', 1, 1)
    Task.create('b', '2026-06-02', 'zakonczone', 1, 1)
    assert len(Task.get_all(status_filter='zakonczone')) == 1


def test_filter_category(tmp_data):
    Task.create('a', '2026-06-01', 'do_zrobienia', 1, 1)
    Task.create('b', '2026-06-02', 'do_zrobienia', 3, 1)
    assert len(Task.get_all(category_filter='3')) == 1


def test_search(tmp_data):
    Task.create('kupic mleko', '2026-06-01', 'do_zrobienia', 3, 1)
    Task.create('wyniesc smieci', '2026-06-02', 'do_zrobienia', 1, 1)
    results = Task.get_all(search='mleko')
    assert len(results) == 1
    assert results[0].opis == 'kupic mleko'


def test_user_login_ok(tmp_data):
    u = User.authenticate('admin', 'haslo123')
    assert u is not None
    assert u.username == 'admin'


def test_user_login_bad_password(tmp_data):
    assert User.authenticate('admin', 'zle') is None


def test_user_login_unknown(tmp_data):
    assert User.authenticate('nieznany', 'haslo123') is None
