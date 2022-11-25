from typing import Union

from fastapi import FastAPI
from pydantic import ValidationError

from models import Call, CallResponse
from service import flash_call

app = FastAPI(title="Call API")


@app.post("/flashcall", response_model=CallResponse)
async def index(payload: Call) -> Union[CallResponse, ValidationError]:
    call_response = flash_call(payload)
    return call_response
