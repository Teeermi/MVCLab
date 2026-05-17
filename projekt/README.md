# System zarzadzania zadaniami domowymi

Aplikacja webowa do zarzadzania zadaniami domowymi zbudowana w oparciu o wzorzec architektoniczny MVC z wykorzystaniem frameworka Flask.

## Spis tresci

- [Opis projektu](#opis-projektu)
- [Funkcjonalnosci](#funkcjonalnosci)
- [Struktura projektu](#struktura-projektu)
- [Instrukcja uruchomienia](#instrukcja-uruchomienia)
- [Uzytkowanie](#uzytkowanie)

## Opis projektu

Aplikacja umozliwia zarzadzanie lista zadan domowych. Kazde zadanie posiada opis, termin wykonania, status oraz przypisana kategorie i priorytet. System pozwala na dodawanie, edycje, usuwanie oraz przegladanie zadan z mozliwoscia filtrowania.

## Funkcjonalnosci

### Podstawowe (CRUD)
- Wyswietlanie listy wszystkich zadan
- Dodawanie nowych zadan
- Edycja istniejacych zadan
- Usuwanie zadan
- Podglad szczegolowy zadania

### Dodatkowe
- **Dwa dodatkowe modele z relacjami:**
  - Kategoria (Dom, Praca, Zakupy, Zdrowie, Inne)
  - Priorytet (Niski, Sredni, Wysoki) z kolorowym oznaczeniem
- **Ostylowane widoki** z wykorzystaniem Bootstrap 5
- **Filtrowanie zadan** po statusie i kategorii

## Struktura projektu

```
projekt/
├── app.py              # Glowna aplikacja Flask
├── models.py           # Definicje modeli (Task, Category, Priority)
├── controllers.py      # Kontrolery obslugi zadan HTTP
├── templates/          # Szablony HTML (widoki)
│   ├── base.html       # Szablon bazowy
│   ├── index.html      # Lista zadan
│   ├── add.html        # Formularz dodawania
│   ├── edit.html       # Formularz edycji
│   └── view.html       # Szczegoly zadania
├── static/
│   └── style.css       # Dodatkowe style CSS
├── data.json           # Plik z danymi
├── requirements.txt    # Zaleznosci Python
└── README.md           # Dokumentacja
```

## Instrukcja uruchomienia

### Wymagania
- Python 3.8 lub nowszy
- pip (menedzer pakietow Python)

### Instalacja

1. Przejdz do folderu projektu:
```bash
cd projekt
```

2. Utworz srodowisko wirtualne (opcjonalnie):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Zainstaluj zaleznosci:
```bash
pip install -r requirements.txt
```

4. Uruchom aplikacje:
```bash
python app.py
```

5. Otworz przegladarke i przejdz pod adres:
```
http://localhost:5000
```

## Uzytkowanie

### Lista zadan
Na stronie glownej wyswietlana jest tabela ze wszystkimi zadaniami. Mozna filtrowac zadania po statusie (Do zrobienia, W trakcie, Zakonczone) oraz po kategorii.

### Dodawanie zadania
Kliknij przycisk "Dodaj nowe zadanie" i wypelnij formularz:
- Opis zadania
- Termin wykonania
- Status
- Kategoria
- Priorytet

### Edycja zadania
Przy kazdym zadaniu w tabeli znajduje sie przycisk "Edytuj", ktory pozwala zmodyfikowac dane zadania.

### Usuwanie zadania
Przycisk "Usun" pozwala trwale usunac zadanie z listy.

### Szczegoly zadania
Przycisk "Szczegoly" wyswietla pelne informacje o wybranym zadaniu.

## Technologie

- **Flask** - mikro-framework webowy dla Python
- **Jinja2** - silnik szablonow
- **Bootstrap 5** - framework CSS
- **JSON** - format przechowywania danych
