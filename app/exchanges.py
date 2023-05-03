import requests
from fastapi import FastAPI, HTTPException, APIRouter
from datetime import date, timedelta

from .api_utils import (
    build_api_url_for_n_quotations,
    build_api_url_for_specific_currency_and_date
)
from .services import (
    calculate_exchange_rate_average,
    calculate_exchange_rate_extremes,
    calculate_exchange_rate_diff
)

router = APIRouter()

TABLE_A = 'A'
TABLE_C = 'C'

@router.get('/exchanges/{currency_code}/{date}')
async def get_exchange_rate_by_date(currency_code: str, date: date):
    url = build_api_url_for_specific_currency_and_date(TABLE_A, currency_code, date)
    response = requests.get(url)
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail='Data not found')
    response.raise_for_status()

    response_data = response.json()
    exchange_rate_data = calculate_exchange_rate_average(response_data)
    return {
        'currency': currency_code,
        'date': date,
        'mid': exchange_rate_data,
    }


@router.get('/exchanges/{currency_code}/extremes/last/{n}/')
async def get_exchange_rate_extremes(currency_code: str, n: int = 255):
    if n < 1 or n > 255:
        raise HTTPException(status_code=400, detail='Invalid n value')
    
    url = build_api_url_for_n_quotations(TABLE_A, currency_code, n)
    response = requests.get(url)
    response.raise_for_status()

    response_data = response.json()
    exchange_rate_extreme_data = calculate_exchange_rate_extremes(response_data)
    return {
        'currency': currency_code,
        **exchange_rate_extreme_data
    }


@router.get('/exchanges/{currency_code}/diff/last/{n}/')
async def get_exchange_rate_diff(currency_code: str, n: int = 255):
    if n < 1 or n > 255:
        raise HTTPException(status_code=400, detail='Invalid n value')
    
    url = build_api_url_for_n_quotations(TABLE_C, currency_code, n)

    response = requests.get(url)
    response.raise_for_status()
    
    response_data = response.json()
    exchange_rate_diff_data = calculate_exchange_rate_diff(response_data)
    return {
        'currency': currency_code,
        **exchange_rate_diff_data
    }