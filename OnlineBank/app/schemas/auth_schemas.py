from pydantic import BaseModel

class LoginUserSchema(BaseModel):
    email: str
    password: str
