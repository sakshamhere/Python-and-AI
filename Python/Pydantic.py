# Pydantic is the most widely used data validation library for Python.

from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional

class User(BaseModel):
    id: int
    name: str
    is_active: bool

# Correct
input_data1 = {'id': 101, 'name': 'saksham', 'is_active': True}

# Incorrect
input_data2 = {'id': 101, 'name': 'saksham', 'is_active': 23}

# Default conversion
input_data3 = {'id': '101', 'name': 'saksham', 'is_active': True}

user = User(**input_data3)

# print(user)


# Mixing Pydantic with Typing

class User2(BaseModel):
    id: int
    name: str
    items: List[str]
    quantities: Dict[str, int]
    middleName: Optional[str]

input_data4 = {'id': '101', 'name': 'saksham', 'items': ['a','b'], 'quantities': {'a':2, 'b':3}, 'middleName': None}

input_data5 = {'id': '101', 'name': 'saksham', 'items': 2 , 'quantities': {'a':2, 'b':3}, 'middleName': None}

user2 = User2(**input_data4)

# print(user2)


# Using Feild

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=10,
        description='name',
        examples='saksham'
    )
    salary: int = Field(
        ...,
        ge=50000,
        le=90000
    )

input_data5 = {'id':1, 'name': 'test', 'salary': 60000}

input_data6 = {'id':1, 'name': 'test', 'salary': 10000}

employee = Employee(**input_data5)

# print(employee)

# FeildValidator  - same as Feild mostly

class User3(BaseModel):
    username: str

    @field_validator('username')
    def username_lenght(cls, v):
        if len(v) < 4:
            raise ValueError('error')
        
        return v

input_data7 = {'username': 'abcds'}
input_data8 = {'username': 'ab'}

user = User3(**input_data7)

# print(user)

# ModelValidator - this can access all the valus as the same time

class User4(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('error')
        
        return values
    
input_data9 = {'password': 'test', 'confirm_password': 'test'}

input_data10 = {'password': 'test', 'confirm_password': 'tes'}

user4 = User4(**input_data9)

# print(user4)

# Computed_felid and use of property (we can access property like a method from an object)

class Booking(BaseModel):
    roomno: int
    price: int
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    
booking = Booking(roomno=101, price=1000, quantity=2)

# print(booking.total_price)                              # we used property directly


# Multi Model

class Address(BaseModel):
    street: str
    city: str

class NewUser(BaseModel):
    id: int
    name: str
    address: Address

ob1 = Address(street='one', city='indore')

ob2 = NewUser(id=1, name='saksham', address=ob1)

print(ob2)