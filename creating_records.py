'''
Tutorial link: https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
Sqlalchemy version: 1.2.15
Python version: 3.7
'''

from model import create_session, User

session = create_session()

user = User(name='John Snow', password='johnspassword')

session.add(user)
db_user = session.query(User).filter_by(name='John Snow').first()
