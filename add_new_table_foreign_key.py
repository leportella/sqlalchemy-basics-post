from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from model import start, User, Base

engine, session = start()


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def __repr__(self):  # optional
        return f'Product {self.name} - User {self.user_id}'

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter_by(name='wolf').first()


User.products = relationship(Product, backref='users')
Product.__table__.create(engine)

user = User(name='John')
product = Product(name='wolf', user=user)

session.add(user)
session.add(product)
session.flush()

print(user.products)
print(product.user)
