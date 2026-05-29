from datetime import datetime


def validate_task(form, category_ids, priority_ids):
    errors = {}

    opis = (form.get('opis') or '').strip()
    if not opis:
        errors['opis'] = 'Opis jest wymagany.'
    elif len(opis) < 3:
        errors['opis'] = 'Opis musi miec co najmniej 3 znaki.'
    elif len(opis) > 500:
        errors['opis'] = 'Opis nie moze byc dluzszy niz 500 znakow.'

    termin = (form.get('termin_wykonania') or '').strip()
    if not termin:
        errors['termin_wykonania'] = 'Termin jest wymagany.'
    else:
        try:
            datetime.strptime(termin, '%Y-%m-%d')
        except ValueError:
            errors['termin_wykonania'] = 'Termin musi byc w formacie YYYY-MM-DD.'

    status = form.get('status')
    if status not in ('do_zrobienia', 'w_trakcie', 'zakonczone'):
        errors['status'] = 'Nieprawidlowy status.'

    try:
        category_id = int(form.get('category_id'))
        if category_id not in category_ids:
            errors['category_id'] = 'Wybierz poprawna kategorie.'
    except (TypeError, ValueError):
        errors['category_id'] = 'Wybierz kategorie.'
        category_id = None

    try:
        priority_id = int(form.get('priority_id'))
        if priority_id not in priority_ids:
            errors['priority_id'] = 'Wybierz poprawny priorytet.'
    except (TypeError, ValueError):
        errors['priority_id'] = 'Wybierz priorytet.'
        priority_id = None

    if errors:
        return None, errors

    return {
        'opis': opis,
        'termin_wykonania': termin,
        'status': status,
        'category_id': category_id,
        'priority_id': priority_id,
    }, {}
