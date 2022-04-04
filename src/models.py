from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    SmallInteger,
)
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    family_name = Column(String)
    doc_number = Column(String, nullable=False)
    doc_type = Column(String, nullable=False)
    age = Column(SmallInteger)
    # TODO: use UTC to guarantee timezone
    created_at = Column(DateTime, nullable=False, default=datetime.now)

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
            f"Customer(id={self.id!r}, name={self.name!r}, age={self.age!r}, "
            f"family_name={self.family_name!r}, document={self.doc_number!r}, "
            f"doc_type={self.doc_type!r}, created_at={self.created_at!r})"
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
