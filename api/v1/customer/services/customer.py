import uuid
from typing import List, Type

from sqlalchemy.orm import Session

from api.v1.customer.models.customer import Customer
from api.v1.customer.repositories.customer import CustomerRepository
from api.v1.customer.schemas.customer import CustomerCreate, CustomerUpdate
from api.v1.exceptions import NotFoundException, BadRequestException


class CustomerService:

    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    def get_all_customers(self):
        return self.customer_repository.get_all_customers()

    def get_customer_by_id(self, customer_id: uuid.UUID) -> Customer:
        db_customer = self.customer_repository.get_customer_by_id(customer_id)
        if db_customer is None:
            raise NotFoundException('Customer Not Found')
        return db_customer

    def get_customer_by_email(self, email: str) -> Customer:
        db_customer = self.customer_repository.get_customer_by_email(email)
        if db_customer is None:
            raise NotFoundException('Customer Not found')
        return db_customer

    def create_customer(self, customer: CustomerCreate) -> Customer:
        existing_customer = self.customer_repository.create_customer(customer)
        if existing_customer is not None:
            raise BadRequestException('Customer already exists')
        return self.customer_repository.create_customer(customer)

    def update_customer(self, customer_id: uuid.UUID, customer: CustomerUpdate) -> Customer:
        existing_customer = self.customer_repository.get_customer_by_id(customer_id)
        if existing_customer is None:
            raise NotFoundException('Customer Not Found')

        user_with_email = self.customer_repository.get_customer_by_email(customer.email)

        if user_with_email is not None and user_with_email.email != customer.email:
            raise BadRequestException('Email already in use')

        return self.customer_repository.update_customer(customer_id, customer)

    def delete_customer(self, customer_id: uuid.UUID):
        if self.customer_repository.get_customer_by_id(customer_id) is None:
            raise NotFoundException('Customer Not Found')
        self.customer_repository.delete_customer(customer_id)
