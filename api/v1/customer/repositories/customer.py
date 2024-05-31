import uuid
from typing import Type

from sqlalchemy.orm import Session

from api.v1.customer.models.customer import Customer
from api.v1.customer.schemas.customer import CustomerCreate, CustomerUpdate


class CustomerRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all_customers(self) -> list[Type[Customer]]:
        return self.db.query(Customer).all()

    def get_customer_by_id(self, customer_id: uuid.UUID) -> Customer | None:
        return self.db.query(Customer).filter(Customer.customer_id == customer_id).first()

    # TODO: Verify email is actually filtered
    def get_customer_by_email(self, email: str) -> Customer | None:
        return self.db.query(Customer).filter_by(email=email).first()

    def create_customer(self, customer: CustomerCreate) -> Customer:
        db_customer = Customer(**customer.model_dump())
        self.db.add(db_customer)
        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer

    def update_customer(self, customer_id: uuid.UUID, customer: CustomerUpdate) -> Customer | None:
        db_customer = self.get_customer_by_id(customer_id)
        if db_customer is None:
            return None
        updated_customer = customer.model_dump(exclude_unset=True)
        for key, value in updated_customer.items():
            setattr(db_customer, key, value)
        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer

    def delete_customer(self, customer_id: uuid):
        db_customer = self.get_customer_by_id(customer_id)
        if db_customer is None:
            return None
        self.db.delete(db_customer)
        self.db.commit()
        return db_customer
