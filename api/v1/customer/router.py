from typing import Annotated, List
from uuid import UUID

from fastapi import APIRouter, Depends, status

from api.v1.customer.dependencies import get_customer_service
from api.v1.customer.schemas.customer import CustomerRead, CustomerCreate, CustomerUpdate
from api.v1.customer.services.customer import CustomerService

router = APIRouter(prefix="/api/v1/customer", tags=["Customer Management"])


@router.get("", response_model=List[CustomerRead])
async def get_all_customers(customer_service: Annotated[CustomerService, Depends(get_customer_service)]):
    return customer_service.get_all_customers()


@router.get("/{customer_id}", response_model=CustomerRead)
async def get_customer(customer_id: UUID, customer_service: Annotated[CustomerService, Depends(get_customer_service)]):
    return customer_service.get_customer_by_id(customer_id)


@router.post("", response_model=CustomerRead, dependencies=[Depends(get_customer_service)],
             status_code=status.HTTP_201_CREATED)
async def create_customer(customer: CustomerCreate, customer_service: Annotated[CustomerService,
                          Depends(get_customer_service)]):
    return customer_service.create_customer(customer)


@router.put("/{customer_id}", response_model=CustomerRead)
async def update_customer(customer_id: UUID, customer_data: CustomerUpdate,
                          customer_service: Annotated[CustomerService, Depends(get_customer_service)]):
    return customer_service.update_customer(customer_id, customer_data)


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(customer_id: UUID, customer_service: Annotated[CustomerService,
                          Depends(get_customer_service)]):
    return customer_service.delete_customer(customer_id)
