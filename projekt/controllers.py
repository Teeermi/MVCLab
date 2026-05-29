from flask import render_template, request, redirect, url_for, flash, session
from models import Task, Category, Priority, User
from validators import validate_task
from services import upcoming_holidays, is_holiday
from auth import login_required


def index():
    status_filter = request.args.get('status')
    category_filter = request.args.get('category')
    search = (request.args.get('q') or '').strip()
    tasks = Task.get_all(status_filter=status_filter,
                         category_filter=category_filter,
                         search=search or None)
    return render_template('index.html',
                         tasks=tasks,
                         categories=Category.get_all(),
                         current_status=status_filter,
                         current_category=category_filter,
                         current_search=search,
                         holidays=upcoming_holidays())


def view(task_id):
    task = Task.get_by_id(task_id)
    if not task:
        flash('Nie znaleziono zadania.', 'danger')
        return redirect(url_for('index'))
    return render_template('view.html', task=task, holiday=is_holiday(task.termin_wykonania))


@login_required
def add():
    categories = Category.get_all()
    priorities = Priority.get_all()

    if request.method == 'POST':
        cat_ids = {c.id for c in categories}
        prio_ids = {p.id for p in priorities}
        data, errors = validate_task(request.form, cat_ids, prio_ids)
        if errors:
            return render_template('add.html', categories=categories, priorities=priorities,
                                   form=request.form, errors=errors)
        Task.create(**data)
        flash('Zadanie dodane.', 'success')
        return redirect(url_for('index'))

    return render_template('add.html', categories=categories, priorities=priorities,
                           form={}, errors={})


@login_required
def edit(task_id):
    task = Task.get_by_id(task_id)
    if not task:
        flash('Nie znaleziono zadania.', 'danger')
        return redirect(url_for('index'))

    categories = Category.get_all()
    priorities = Priority.get_all()

    if request.method == 'POST':
        cat_ids = {c.id for c in categories}
        prio_ids = {p.id for p in priorities}
        data, errors = validate_task(request.form, cat_ids, prio_ids)
        if errors:
            return render_template('edit.html', task=task, categories=categories,
                                   priorities=priorities, form=request.form, errors=errors)
        Task.update(task_id, **data)
        flash('Zapisano zmiany.', 'success')
        return redirect(url_for('view', task_id=task_id))

    return render_template('edit.html', task=task, categories=categories,
                           priorities=priorities, form=task.to_dict(), errors={})


@login_required
def delete(task_id):
    if Task.delete(task_id):
        flash('Zadanie usuniete.', 'success')
    else:
        flash('Nie znaleziono zadania.', 'danger')
    return redirect(url_for('index'))


def login():
    if 'user' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = (request.form.get('username') or '').strip()
        password = request.form.get('password') or ''
        user = User.authenticate(username, password)
        if user:
            session['user'] = user.username
            flash(f'Zalogowano jako {user.username}.', 'success')
            return redirect(url_for('index'))
        flash('Bledny login lub haslo.', 'danger')

    return render_template('login.html')


def logout():
    session.pop('user', None)
    flash('Wylogowano.', 'info')
    return redirect(url_for('index'))
