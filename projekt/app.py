from flask import Flask
import controllers

app = Flask(__name__)
app.secret_key = 'tajny_klucz_aplikacji'

app.add_url_rule('/', 'index', controllers.index)
app.add_url_rule('/task/<int:task_id>', 'view', controllers.view)
app.add_url_rule('/add', 'add', controllers.add, methods=['GET', 'POST'])
app.add_url_rule('/edit/<int:task_id>', 'edit', controllers.edit, methods=['GET', 'POST'])
app.add_url_rule('/delete/<int:task_id>', 'delete', controllers.delete)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
