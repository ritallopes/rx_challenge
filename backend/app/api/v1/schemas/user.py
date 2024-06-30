from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class UserPublic(BaseModel):
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': [
                {
                    'email': 'example@example.com',
                    'name': 'Jane',
                }
            ]
        }
