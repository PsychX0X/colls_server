import json
import os

import requests
import dotenv

from models import Call

dotenv.load_dotenv()

AERO_EMAIL = os.environ.get("AERO_EMAIL")
AERO_API_KEY = os.environ.get("AERO_API_KEY")


def flash_call(call: Call):
    url = f"https://{AERO_EMAIL}:{AERO_API_KEY}@gate.smsaero.ru/v2/flashcall/send"
    res = requests.get(url, params={
        "phone": call.phone_number,
        "code": call.code,
    })
    return json.loads(res.content)
