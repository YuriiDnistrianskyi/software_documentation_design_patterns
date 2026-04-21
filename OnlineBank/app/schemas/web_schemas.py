from pydantic import BaseModel

class CreateCashAccountRequest(BaseModel):
    number_account: str
    CVV: str
