from ninja import Schema

class LoginSchema(Schema):
    email: str
    password: str


class ChangePasswordSchema(Schema):
    old_password: str
    new_password: str
    confirm_password: str