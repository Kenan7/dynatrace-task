from fastapi import Path

currency_code_param = Path(
    ...,
    description='Currency code in format XXX (e.g. USD)',
    min_length=3,
    max_length=3,
    regex='^[A-Z]{3}$'
)

date_param = Path(
    ...,
    description='Date in format YYYY-MM-DD (e.g. 2023-05-02)',
)

n_param = Path(
    ...,
    description='Number of quotations to calculate',
    ge=1,
    le=255
)