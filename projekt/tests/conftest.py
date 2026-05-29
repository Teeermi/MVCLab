import os
import sys
import json
import hashlib
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def tmp_data(tmp_path):
    data = tmp_path / 'data.json'
    data.write_text('{"tasks": []}', encoding='utf-8')
    users = tmp_path / 'users.json'
    pw = hashlib.sha256(('mvclab' + 'haslo123').encode('utf-8')).hexdigest()
    users.write_text(json.dumps({'users': [{'username': 'admin', 'password_hash': pw}]}), encoding='utf-8')
    os.environ['DATA_FILE'] = str(data)
    os.environ['USERS_FILE'] = str(users)
    yield {'data': data, 'users': users}
    os.environ.pop('DATA_FILE', None)
    os.environ.pop('USERS_FILE', None)


@pytest.fixture
def client(tmp_data):
    from app import app
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    return app.test_client()


@pytest.fixture
def logged_client(client):
    client.post('/login', data={'username': 'admin', 'password': 'haslo123'})
    return client
