import os
from flask import Flask, session
from flask_wtf.csrf import CSRFProtect
import controllers

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'tajny_klucz_aplikacji')
CSRFProtect(app)


@app.context_processor
def inject_user():
    return {'current_user': session.get('user')}


app.add_url_rule('/', 'index', controllers.index)
app.add_url_rule('/task/<int:task_id>', 'view', controllers.view)
app.add_url_rule('/add', 'add', controllers.add, methods=['GET', 'POST'])
app.add_url_rule('/edit/<int:task_id>', 'edit', controllers.edit, methods=['GET', 'POST'])
app.add_url_rule('/delete/<int:task_id>', 'delete', controllers.delete, methods=['POST'])
app.add_url_rule('/login', 'login', controllers.login, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', controllers.logout, methods=['POST'])


if __name__ == '__main__':
    debug = os.environ.get('FLASK_DEBUG') == '1'
    app.run(debug=debug, host='0.0.0.0', port=5000)
