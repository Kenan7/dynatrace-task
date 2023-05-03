from pydantic import BaseModel
from datetime import date


class example_response_for_get_exchange_rate_by_date(BaseModel):
    currency: str = 'USD'
    date: date
    mid: float = 1.0

class example_response_for_get_exchange_rate_extremes(BaseModel):
    currency: str = 'USD'
    max: float = 1.0
    min: float = 1.0

class example_response_for_get_exchange_rate_diff(BaseModel):
    currency: str = 'USD'
    diff: float = 1.0
