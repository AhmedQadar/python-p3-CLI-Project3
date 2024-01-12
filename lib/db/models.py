from sqlalchemy import create_engine, func, and_
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData, Boolean
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///manager.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()  

user_account = Table(
    'user_account',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('account_id', ForeignKey('accounts.id'), primary_key=True),
    extend_existing=True
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    email = Column(String())
    age = Column(Integer())

    accounts = relationship('Account', secondary=user_account, back_populates='users')
    passwords = relationship('Password', backref=backref('user'))

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'
class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer(), primary_key=True)
    user_name = Column(String())
    company = Column(String())
    active = Column(Boolean())
    user_id = Column(Integer(), ForeignKey('users.id'))
    
    users = relationship('User', secondary=user_account, back_populates='accounts')
    passwords = relationship('Password', backref=backref('account'))
    
    def __repr__(self):
        return f'<Account {self.user_name}>'
    
class Password(Base):
    __tablename__ = 'passwords'

    id = Column(Integer(), primary_key=True)
    password = Column(String(), nullable=False)
    account_id = Column(Integer(), ForeignKey('accounts.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))
    
    def __repr__(self):
        return f'<Password {self.password}>'
