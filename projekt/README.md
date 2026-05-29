# System zarzadzania zadaniami domowymi

Aplikacja webowa do zarzadzania zadaniami domowymi (Zadanie 4 z listy projektowej). Napisana w Pythonie w oparciu o Flask, zgodnie ze wzorcem MVC.

## Spis tresci

- [Opis](#opis)
- [Funkcjonalnosci](#funkcjonalnosci)
- [Instrukcja uruchomienia](#instrukcja-uruchomienia)
- [Logowanie](#logowanie)
- [Testy](#testy)
- [Struktura projektu](#struktura-projektu)
- [Technologie](#technologie)

## Opis

Aplikacja pozwala dodawac, edytowac, usuwac i przegladac zadania domowe. Kazde zadanie ma opis, termin wykonania, status, kategorie i priorytet. Mozna filtrowac liste po statusie i kategorii oraz szukac po tresci opisu.

Dane sa zapisywane w pliku `data.json`, konta uzytkownikow w `users.json` (hasla hashowane).

## Funkcjonalnosci

Podstawowe (CRUD):
- lista wszystkich zadan
- dodawanie nowego zadania
- edycja istniejacego zadania
- usuwanie zadania
- widok szczegolow zadania

Dodatkowo:
- dwa dodatkowe modele (Kategoria i Priorytet) powiazane z zadaniem
- ostylowanie Bootstrap 5 + wlasny CSS
- filtrowanie po statusie i kategorii + wyszukiwanie po opisie
- walidacja danych po stronie serwera (validators.py) i klienta (validation.js)
- logowanie i sesja uzytkownika (do dodawania/edycji/usuwania trzeba byc zalogowanym)
- ochrona CSRF (Flask-WTF) i usuwanie tylko przez POST
- integracja z zewnetrznym API (Nager.Date) - lista polskich swiat panstwowych pokazywana na liscie oraz oznaczenie czy termin zadania wypada w dzien swiateczny
- testy jednostkowe pytest
- konfiguracja Docker (gunicorn)

## Instrukcja uruchomienia

### Docker (zalecane)

```bash
cd projekt
docker compose up --build
```

Aplikacja: http://localhost:5000

Zatrzymanie:
```bash
docker compose down
```

### Lokalnie

Wymagania: Python 3.8+ i pip.

```bash
cd projekt
python -m venv venv
source venv/bin/activate          # Linux/Mac
# venv\Scripts\activate           # Windows
pip install -r requirements.txt
python app.py
```

Tryb deweloperski z autoreloadem:
```bash
FLASK_DEBUG=1 python app.py
```

## Logowanie

Konto demonstracyjne:
- login: `admin`
- haslo: `admin123`

Bez logowania mozna tylko przegladac liste i szczegoly zadan.

## Testy

```bash
cd projekt
pip install -r requirements.txt
pytest
```

Testy uzywaja tymczasowych plikow JSON, nie modyfikuja produkcyjnego `data.json`.

## Struktura projektu

```
projekt/
├── app.py              # Flask app, routing, CSRF
├── controllers.py      # Kontrolery (obsluga zadan HTTP)
├── models.py           # Modele: Task, Category, Priority, User
├── validators.py       # Walidacja danych formularza
├── services.py         # Integracja z API swiat panstwowych
├── auth.py             # Dekorator login_required
├── data.json           # Przykladowe zadania
├── users.json          # Konta uzytkownikow (hasla hashowane)
├── requirements.txt
├── pytest.ini
├── Dockerfile
├── docker-compose.yml
├── templates/          # Szablony Jinja2
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   ├── edit.html
│   ├── view.html
│   └── login.html
├── static/
│   ├── style.css
│   └── validation.js
└── tests/
    ├── conftest.py
    ├── test_models.py
    ├── test_validators.py
    └── test_controllers.py
```

## Technologie

- Flask 3.0
- Flask-WTF (CSRF)
- Bootstrap 5
- requests (do zewnetrznego API)
- gunicorn (serwer produkcyjny w Dockerze)
- pytest
