from datetime import date


NBP_API_URL = 'http://api.nbp.pl/api/exchangerates'

def build_api_url_for_specific_currency_and_date(table: str, currency_code: str, date: date) -> str:
    return f'{NBP_API_URL}/rates/{table}/{currency_code}/{date}?format=json'

def build_api_url_for_n_quotations(table: str, currency_code: str, n: int) -> str:
    return f'{NBP_API_URL}/rates/{table}/{currency_code}/last/{n}?format=json'