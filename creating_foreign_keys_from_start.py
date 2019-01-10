'''
Tutorial link: https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
Sqlalchemy version: 1.2.15
Python version: 3.7
'''

from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')

    def __repr__(self):  # optional
        return f'Product {self.name}'


class User(Base):
    __tablename__ = 'user'  # if you use base it is obligatory

    id = Column(Integer, primary_key=True)  # obligatory
    name = Column(String)
    password = Column(String)
    products = relationship(Product, backref="users")

    def __repr__(self):  # optional
        return f'User {self.name}'


def start():
    engine = create_engine('sqlite:///:memory:')

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    return engine, session
