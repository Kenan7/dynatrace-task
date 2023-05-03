import requests
from fastapi import HTTPException, APIRouter
from datetime import date

from .api_utils import (
    build_api_url_for_n_quotations,
    build_api_url_for_specific_currency_and_date
)
from .services import (
    calculate_exchange_rate_average,
    calculate_exchange_rate_extremes,
    calculate_exchange_rate_diff
)
from .params import (
    currency_code_param,
    date_param,
    n_param
)
from .example_responses import (
    example_response_for_get_exchange_rate_by_date,
    example_response_for_get_exchange_rate_extremes,
    example_response_for_get_exchange_rate_diff
)

router = APIRouter()

TABLE_A = 'a'
TABLE_C = 'c'


@router.get(
    path='/exchanges/{currency_code}/{date}',
    responses={
        200: {
            'model': example_response_for_get_exchange_rate_by_date,
            'description': 'Exchange rate for given currency and date',
        },
    }
)
async def get_exchange_rate_by_date(
    currency_code: str = currency_code_param, date: date = date_param
) -> dict:

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


@router.get(
    path='/exchanges/{currency_code}/extremes/last/{n}/',
    responses={
        200: {
            'model': example_response_for_get_exchange_rate_extremes,
            'description': 'Exchange rate extremes for given currency',
        },
    }
)
async def get_exchange_rate_extremes(
    currency_code: str = currency_code_param, n: int = n_param
) -> dict:

    url = build_api_url_for_n_quotations(TABLE_A, currency_code, n)
    response = requests.get(url)
    response.raise_for_status()

    response_data = response.json()
    exchange_rate_extreme_data = calculate_exchange_rate_extremes(response_data)
    return {
        'currency': currency_code,
        **exchange_rate_extreme_data
    }


@router.get(
    path='/exchanges/{currency_code}/diff/last/{n}/',
    responses={
        200: {
            'model': example_response_for_get_exchange_rate_diff,
            'description': 'Exchange rate diff for given currency',
        },
    }
)
async def get_exchange_rate_diff(
    currency_code: str = currency_code_param, n: int = n_param
) -> dict:

    url = build_api_url_for_n_quotations(TABLE_C, currency_code, n)

    response = requests.get(url)
    response.raise_for_status()
    
    response_data = response.json()
    exchange_rate_diff_data = calculate_exchange_rate_diff(response_data)
    return {
        'currency': currency_code,
        **exchange_rate_diff_data
    }