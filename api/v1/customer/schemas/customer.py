from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class BaseCustomer(BaseModel):
    email: EmailStr
    name: str
    address: str
    phone: Optional[str]


class CustomerCreate(BaseCustomer):
    pass


class CustomerUpdate(BaseCustomer):
    pass


class CustomerRead(BaseCustomer):
    model_config = ConfigDict(from_attributes=True)
    customer_id: UUID
