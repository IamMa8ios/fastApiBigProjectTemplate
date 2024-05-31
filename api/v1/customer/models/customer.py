import uuid

from sqlalchemy import String, UUID, func, Column
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True,
        nullable=False
    )
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    address = Column(String(100), nullable=False)
    phone = Column(String(18))
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    def __init__(self, name, email, address, phone=None):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
