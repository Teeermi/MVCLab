import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')


class Priority:
    def __init__(self, id, nazwa, kolor):
        self.id = id
        self.nazwa = nazwa
        self.kolor = kolor

    def to_dict(self):
        return {'id': self.id, 'nazwa': self.nazwa, 'kolor': self.kolor}

    @staticmethod
    def get_all():
        return [
            Priority(1, 'Niski', '#28a745'),
            Priority(2, 'Sredni', '#ffc107'),
            Priority(3, 'Wysoki', '#dc3545')
        ]

    @staticmethod
    def get_by_id(priority_id):
        for p in Priority.get_all():
            if p.id == priority_id:
                return p
        return None


class Category:
    def __init__(self, id, nazwa):
        self.id = id
        self.nazwa = nazwa

    def to_dict(self):
        return {'id': self.id, 'nazwa': self.nazwa}

    @staticmethod
    def get_all():
        return [
            Category(1, 'Dom'),
            Category(2, 'Praca'),
            Category(3, 'Zakupy'),
            Category(4, 'Zdrowie'),
            Category(5, 'Inne')
        ]

    @staticmethod
    def get_by_id(category_id):
        for c in Category.get_all():
            if c.id == category_id:
                return c
        return None


class Task:
    def __init__(self, id, opis, termin_wykonania, status, category_id, priority_id):
        self.id = id
        self.opis = opis
        self.termin_wykonania = termin_wykonania
        self.status = status
        self.category_id = category_id
        self.priority_id = priority_id

    @property
    def category(self):
        return Category.get_by_id(self.category_id)

    @property
    def priority(self):
        return Priority.get_by_id(self.priority_id)

    def to_dict(self):
        return {
            'id': self.id,
            'opis': self.opis,
            'termin_wykonania': self.termin_wykonania,
            'status': self.status,
            'category_id': self.category_id,
            'priority_id': self.priority_id
        }

    @staticmethod
    def _load_data():
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {'tasks': []}

    @staticmethod
    def _save_data(data):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def get_all(status_filter=None, category_filter=None):
        data = Task._load_data()
        tasks = []
        for t in data['tasks']:
            task = Task(t['id'], t['opis'], t['termin_wykonania'],
                       t['status'], t['category_id'], t['priority_id'])
            if status_filter and task.status != status_filter:
                continue
            if category_filter and task.category_id != int(category_filter):
                continue
            tasks.append(task)
        return tasks

    @staticmethod
    def get_by_id(task_id):
        data = Task._load_data()
        for t in data['tasks']:
            if t['id'] == task_id:
                return Task(t['id'], t['opis'], t['termin_wykonania'],
                           t['status'], t['category_id'], t['priority_id'])
        return None

    @staticmethod
    def create(opis, termin_wykonania, status, category_id, priority_id):
        data = Task._load_data()
        new_id = max([t['id'] for t in data['tasks']], default=0) + 1
        task = Task(new_id, opis, termin_wykonania, status, category_id, priority_id)
        data['tasks'].append(task.to_dict())
        Task._save_data(data)
        return task

    @staticmethod
    def update(task_id, opis, termin_wykonania, status, category_id, priority_id):
        data = Task._load_data()
        for t in data['tasks']:
            if t['id'] == task_id:
                t['opis'] = opis
                t['termin_wykonania'] = termin_wykonania
                t['status'] = status
                t['category_id'] = category_id
                t['priority_id'] = priority_id
                Task._save_data(data)
                return True
        return False

    @staticmethod
    def delete(task_id):
        data = Task._load_data()
        data['tasks'] = [t for t in data['tasks'] if t['id'] != task_id]
        Task._save_data(data)
