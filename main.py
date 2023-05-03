from typing import List
import requests
from fastapi import FastAPI, HTTPException

from app.exchanges import router as exchanges_router

app = FastAPI()

app.include_router(exchanges_router)
