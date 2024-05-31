from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v1.customer.repositories.customer import CustomerRepository
from api.v1.customer.services.customer import CustomerService
from api.v1.db import get_db


def get_customer_service(session: Annotated[Session, Depends(get_db)]) -> CustomerService:
    repo = CustomerRepository(db=session)
    return CustomerService(customer_repository=repo)
