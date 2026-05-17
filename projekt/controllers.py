from flask import render_template, request, redirect, url_for
from models import Task, Category, Priority


def index():
    status_filter = request.args.get('status')
    category_filter = request.args.get('category')
    tasks = Task.get_all(status_filter=status_filter, category_filter=category_filter)
    categories = Category.get_all()
    return render_template('index.html',
                         tasks=tasks,
                         categories=categories,
                         current_status=status_filter,
                         current_category=category_filter)


def view(task_id):
    task = Task.get_by_id(task_id)
    if not task:
        return redirect(url_for('index'))
    return render_template('view.html', task=task)


def add():
    categories = Category.get_all()
    priorities = Priority.get_all()

    if request.method == 'POST':
        opis = request.form.get('opis')
        termin = request.form.get('termin_wykonania')
        status = request.form.get('status', 'do_zrobienia')
        category_id = int(request.form.get('category_id', 5))
        priority_id = int(request.form.get('priority_id', 2))

        if opis and termin:
            Task.create(opis, termin, status, category_id, priority_id)
            return redirect(url_for('index'))

    return render_template('add.html', categories=categories, priorities=priorities)


def edit(task_id):
    task = Task.get_by_id(task_id)
    if not task:
        return redirect(url_for('index'))

    categories = Category.get_all()
    priorities = Priority.get_all()

    if request.method == 'POST':
        opis = request.form.get('opis')
        termin = request.form.get('termin_wykonania')
        status = request.form.get('status')
        category_id = int(request.form.get('category_id'))
        priority_id = int(request.form.get('priority_id'))

        if opis and termin:
            Task.update(task_id, opis, termin, status, category_id, priority_id)
            return redirect(url_for('index'))

    return render_template('edit.html', task=task, categories=categories, priorities=priorities)


def delete(task_id):
    Task.delete(task_id)
    return redirect(url_for('index'))
