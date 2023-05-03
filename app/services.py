def calculate_exchange_rate_average(data: dict) -> float:
    return data['rates'][0]['mid']

def calculate_exchange_rate_extremes(data: dict):
    rates = data['rates']
    max_value = max(r['mid'] for r in rates)
    min_value = min(r['mid'] for r in rates)
    return {'max': max_value, 'min': min_value}

def calculate_exchange_rate_diff(data: dict):
    rates = data['rates']
    diff = max(r['ask'] - r['bid'] for r in rates)
    return {'diff': diff}
