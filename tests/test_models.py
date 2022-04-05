import pytest
from sqlalchemy import select

from src.models import Customer, Address, PhoneNumber


@pytest.mark.anyio
async def test_create_customer(db_session):
    customer = Customer(
        display_name="Stout",
        full_name="Stout Campos",
        doc_number="12352498301",
        doc_type="cpf",
    )

    async with db_session() as session:
        session.add(customer)
        await session.commit()

        stmt = select(Customer).where(Customer.full_name == customer.full_name)
        result = await session.scalars(stmt)

    assert result.unique().one() == customer


@pytest.mark.anyio
async def test_create_customer_with_address(db_session):
    address = Address(
        street="Rua B",
        number="s/n",
        zip_code=12345098,
        city="Belem",
        country="Brazil",
    )
    customer = Customer(
        display_name="Lindona",
        full_name="Britta Campos",
        doc_number="12352498301",
        doc_type="cpf",
        address=address,
    )

    async with db_session() as session:
        session.add(customer)
        await session.commit()

        stmt = select(Customer).where(Customer.full_name == customer.full_name)
        result = await session.scalars(stmt)
        got = result.unique().one()

    assert got == customer
    assert got.address == customer.address


@pytest.mark.anyio
async def test_create_customer_with_phone_number(db_session):
    phone_number1 = PhoneNumber(country_code=55, area_code=21, number=924453598)
    phone_number2 = PhoneNumber(country_code=49, area_code=199, number=2348602)

    customer = Customer(
        display_name="Dona Pelú",
        full_name="Dona Pelú Campos",
        doc_number="P55SDEFV1",
        doc_type="Residence Card",
        phone_numbers=[phone_number1, phone_number2],
    )

    async with db_session() as session:
        session.add(customer)
        await session.commit()

        stmt = select(Customer).where(Customer.full_name == customer.full_name)
        result = await session.scalars(stmt)
        got = result.unique().one()

    assert got == customer
    assert got.phone_numbers == [phone_number1, phone_number2]


def test_repr_customer_model():
    customer = Customer(
        display_name="Stout",
        full_name="Stout Bell",
        doc_number="12352498301",
        doc_type="cpf",
    )

    expected_repr = (
        "Customer(id=None, display_name='Stout', age=None, "
        "full_name='Stout Bell', document='12352498301', doc_type='cpf', "
        "created_at=None)"
    )

    assert customer.__repr__() == expected_repr


def test_repr_address_model():
    address = Address(
        street="Rua B",
        number="s/n",
        zip_code=12345098,
        city="Belem",
        country="Brazil",
    )

    expected_repr = (
        "Address(id=None, street='Rua B', number='s/n', complement=None, "
        "zip_code=12345098, city='Belem', country='Brazil')"
    )

    assert address.__repr__() == expected_repr


def test_repr_phone_number_model():
    phone_number = PhoneNumber(country_code=55, area_code=21, number=924453598)

    expected_repr = (
        "PhoneNumber(id=None, country_code=55, area_code=21, number=924453598)"
    )

    assert phone_number.__repr__() == expected_repr
