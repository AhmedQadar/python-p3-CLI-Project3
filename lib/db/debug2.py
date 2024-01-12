from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Account, Password

if __name__ == '__main__':
    engine = create_engine('sqlite:///database.sqlite', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()
    