from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Account, Password

if __name__ == '__main__':
    engine = create_engine('sqlite:///manager.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


    session.query(User).delete()
    session.query(Account).delete()
    session.query(Password).delete()

    fake = Faker()

    users = []
    for _ in range(50):
        user = User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            age=random.randint(18, 80)
        )
        session.add(user)
        session.commit()
        users.append(user)

        num_accounts = random.randint(1, 5)
        for _ in range(num_accounts):
            account = Account(
                user_name=fake.user_name(),
                company=fake.company(),
                active=random.choice([True, False]),
                user_id=user.id
            )
            account.users.append(user)
            session.add(account)
            session.commit()


    passwords = []
    for user in users:
        accounts = session.query(Account).filter(Account.user_id == user.id).all()
        for account in accounts:
            password = Password(
                password=fake.password(),
                account_id=account.id,
                user_id=user.id
            )
            passwords.append(password)



    session.bulk_save_objects(passwords)
    session.commit()
    session.close()