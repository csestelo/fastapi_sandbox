from datetime import datetime
from typing import Any

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    SmallInteger,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship, declarative_base

Base: Any = declarative_base()


class Customer(Base):
    __tablename__ = "customer"
    __table_args__ = (
        UniqueConstraint(
            "doc_number",
            "doc_type",
            name="indent_doc",
        ),
    )

    id = Column(Integer, primary_key=True)
    display_name = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    doc_number = Column(String, nullable=False)
    doc_type = Column(String, nullable=False)
    age = Column(SmallInteger)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    address = relationship(
        "Address",
        cascade="all, delete",
        passive_deletes=True,
        uselist=False,
        lazy="joined",
    )
    phone_numbers = relationship(
        "PhoneNumber",
        cascade="all, delete",
        passive_deletes=True,
        lazy="joined",
    )

    def __repr__(self):
        return (
            f"Customer(id={self.id!r}, display_name={self.display_name!r}, "
            f"age={self.age!r}, full_name={self.full_name!r}, "
            f"document={self.doc_number!r}, doc_type={self.doc_type!r}, "
            f"created_at={self.created_at!r})"
        )


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    street = Column(String, nullable=False)
    number = Column(String, nullable=False)
    complement = Column(String)
    zip_code = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)

    customer_id = Column(Integer, ForeignKey("customer.id", ondelete="CASCADE"))

    def __repr__(self):
        return (
            f"Address(id={self.id!r}, street={self.street!r}, "
            f"number={self.number!r}, complement={self.complement!r}, "
            f"zip_code={self.zip_code!r}, city={self.city!r}, "
            f"country={self.country!r})"
        )


class PhoneNumber(Base):
    __tablename__ = "phone_number"

    id = Column(Integer, primary_key=True)
    country_code = Column(SmallInteger, nullable=False)
    area_code = Column(SmallInteger)
    number = Column(Integer, nullable=False)

    customer_id = Column(Integer, ForeignKey("customer.id", ondelete="CASCADE"))

    def __repr__(self):
        return (
            f"PhoneNumber(id={self.id!r}, country_code={self.country_code!r}, "
            f"area_code={self.area_code!r}, number={self.number!r})"
        )
