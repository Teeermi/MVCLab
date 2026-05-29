from functools import wraps
from flask import session, redirect, url_for, flash


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            flash('Zaloguj sie, aby wykonac te akcje.', 'warning')
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper
