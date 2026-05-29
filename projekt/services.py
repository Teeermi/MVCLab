import time
from datetime import date, datetime
import requests

_cache = {}
_TTL = 24 * 60 * 60


def fetch_holidays(year):
    if year in _cache and time.time() - _cache[year]['time'] < _TTL:
        return _cache[year]['data']
    try:
        r = requests.get(f'https://date.nager.at/api/v3/PublicHolidays/{year}/PL', timeout=3)
        r.raise_for_status()
        data = r.json()
    except Exception:
        return _cache.get(year, {}).get('data', [])
    _cache[year] = {'time': time.time(), 'data': data}
    return data


def is_holiday(iso_date):
    try:
        d = datetime.strptime(iso_date, '%Y-%m-%d').date()
    except (TypeError, ValueError):
        return None
    for h in fetch_holidays(d.year):
        if h.get('date') == iso_date:
            return h.get('localName') or h.get('name')
    return None


def upcoming_holidays(limit=3):
    today = date.today()
    result = []
    for h in fetch_holidays(today.year):
        try:
            d = datetime.strptime(h['date'], '%Y-%m-%d').date()
        except (KeyError, ValueError):
            continue
        if d >= today:
            result.append({'date': h['date'], 'name': h.get('localName') or h.get('name')})
        if len(result) >= limit:
            break
    return result
