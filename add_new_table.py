from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from model import start

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):  # optional
        return f'Product {self.name}'


engine, session = start()

print('Available tables before creation:', engine.table_names())
Product.__table__.create(engine)
print('Available tables after creation:', engine.table_names())
