import click
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import joinedload, Session
from sqlalchemy.orm.session import make_transient
from db.models  import User, Account, Password, Session, user_account

def read_banner_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

def get_session():
    return Session()

def close_session(session):
    session.close()
                                            ### DISPLAY METHODS ###



def display_users():
    all_users = Session().query(User).all()
    for user in all_users:
        print(f"ID: {user.id} | Name: {user.first_name} {user.last_name} | Email: {user.email} | Age: {user.age}")

def display_accounts():
    all_accounts = Session().query(Account).all()
    for account in all_accounts:
        print(f"ID: {account.id} | User Name: {account.user_name} | Company: {account.company} | Active: {account.active}")

def display_passwords():
    all_passwords = Session().query(Password).all()
    for password in all_passwords:
        print(f"ID: {password.id} | Password: {password.password} | User ID: {password.user_id} | Account ID: {password.account_id}")


                                           ### USER METHODS ###
def find_user_by_id(user_id):
    user = Session().query(User).get(user_id)
    session = get_session()
    if user:
        print(f"Found user: {user.first_name} {user.last_name} | Email: {user.email} | Age: {user.age}")
    else:
        print(f"User with ID {user_id} not found.")
    
    close_session(session)


def all_details_of_user(user_id):
    user = Session().query(User).get(user_id)
    if user:
        user_details = {
            "ID": user.id,
            "Name": f"{user.first_name} {user.last_name}",
            "Email": user.email,
            "Age": user.age,
            "Accounts": [],
            "Passwords": []
        }
        
        for account in user.accounts:
            account_details = {
                "ID": account.id,
                "User Name": account.user_name,
                "Company": account.company,
                "Active": account.active
            }
            user_details["Accounts"].append(account_details)
        
        for password in user.passwords:
            password_details = {
                "ID": password.id,
                "Password": password.password,
                "User ID": password.user_id,
                "Account ID": password.account_id
            }
            user_details["Passwords"].append(password_details)
        
        for key, value in user_details.items():
            if isinstance(value, list):
                click.echo(f"{key}:")
                for item in value:
                    click.echo("\t" + "\n\t".join([f"{k}: {v}" for k, v in item.items()]))
            else:
                click.echo(f"{key}: {value}")
    else:
        click.echo(f"User with ID {user_id} not found.")


def number_of_active_accounts(user_id):
    user = Session().query(User).get(user_id)
    if user:
        active_accounts = [account for account in user.accounts if account.active]
        num_active_accounts = len(active_accounts)
        print(f"Number of active accounts for user with ID {user_id}: {num_active_accounts}")

        active_accounts_tuple = []

        if active_accounts:
            print("\nActive Accounts:")
            for account in active_accounts:
                account_data = (account.id, account.user_name, account.company, account.active)
                active_accounts_tuple.append(account_data)
                print(f"ID: {account.id} | User Name: {account.user_name} | Company: {account.company} | Active: {account.active}")

        return active_accounts_tuple
    else:
        print(f"User with ID {user_id} not found.")
        return None

def number_of_accounts(user_id):
    user = Session().query(User).get(user_id)
    if user:
        num_accounts = len(user.accounts)
        print(f"Number of accounts for user with ID {user_id}: {num_accounts}")
    else:
        print(f"User with ID {user_id} not found.")

def accounts_and_passwords(user_id):
    user = Session().query(User).get(user_id)
    if user:
        for account in user.accounts:
            print(f"Account ID: {account.id} | User Name: {account.user_name} | Company: {account.company} | Active: {account.active}")
            passwords = [password.password for password in account.passwords]
            print(f"Passwords: {passwords}")
            print("----")
    else:
        print(f"User with ID {user_id} not found.")

 


                                                 ### ACCOUNT METHODS ###
def find_account_by_user_name(user_name):
    account = Session().query(Account).filter(Account.user_name == user_name).first()
    if account:
        print(f"Found account: User Name: {account.user_name} | Company: {account.company} | Active: {account.active}")
    else:
        print(f"Account with user name '{user_name}' not found.")

def account_owner(user_name):
    account_owner = Session().query(User).join(Account).filter(Account.user_name == user_name).first()
    if account_owner:
        print(f"Account owner: {account_owner.first_name} {account_owner.last_name} | Email: {account_owner.email} | Age: {account_owner.age}")
    else:
        print(f"Account with user name '{user_name}' not found.")

def account_password(user_name):
    account_password = Session().query(Password).join(Account).filter(Account.user_name == user_name).first()
    if account_password:
        print(f"Account password: {account_password.password}")
    else:
        print(f"Account with user name '{user_name}' not found.")

def account_company(user_name):
    account_company = Session().query(Account).filter(Account.user_name == user_name).first()
    if account_company:
        print(f"Account company: {account_company.company}")
    else:
        print(f"Account with user name '{user_name}' not found.")


                                                

                                                ### PASSWORD METHODS ###
def find_password_by_id(password_id):
    password = Session().query(Password).get(password_id)
    if password:
        print(f"Found password: {password.password} | User ID: {password.user_id} | Account ID: {password.account_id}")
    else:
        print(f"Password with ID {password_id} not found.")

def account_for_password(password_id):
    account_for_password = Session().query(Account).join(Password).filter(Password.id == password_id).first()
    if account_for_password:
        print(f"Account for password: User Name: {account_for_password.user_name} | Company: {account_for_password.company} | Active: {account_for_password.active}")
    else:
        print(f"Password with password '{password}' not found.")

def owner(password_id):
    owner = Session().query(User).join(Password).filter(Password.id == password_id).first()
    if owner:
        print(f"Owner: {owner.first_name} {owner.last_name} | Email: {owner.email} | Age: {owner.age}")
    else:
        print(f"Password with password '{password}' not found.")


                                                 

                                                 ### CRUD METHODS ###

                                                 
def add_user_account_password(session):
    first_name = click.prompt("Enter first name")
    last_name = click.prompt("Enter last name")
    email = click.prompt("Enter email")
    age = click.prompt("Enter age", type=int)

    new_user = User(first_name=first_name, last_name=last_name, email=email, age=age)
    session.add(new_user)
    session.commit()


    if first_name and last_name and email and age:
        user_name = click.prompt("Enter user name for the new account")
        company = click.prompt("Enter company for the new account")
        active = click.confirm("Is the account active?")
        user_id = new_user.id

        new_account = Account(user_name=user_name, company=company, active=active, user_id=user_id)
        new_account.users.append(new_user)
        session.add(new_account)
        session.commit()

        password_value = click.prompt("Enter password for the account")

        new_password = Password(password=password_value)
        new_password.user = new_user
        new_password.account = new_account
        session.add(new_password)
        session.commit()

        print(f"User, account, and password added successfully. User ID: {new_user.id}, Account ID: {new_account.id}, Password ID: {new_password.id}")
    else:
        session.rollback()  # Rollback the transaction if the user did not provide input

def delete_user(user_id):
    session = get_session()
    user = session.query(User).get(user_id)
    if user:
        try:
            # Delete passwords associated with the user
            session.query(Password).filter(Password.user_id == user_id).delete()

            # Delete accounts associated with the user
            session.query(Account).filter(Account.users.any(id=user_id)).delete(synchronize_session=False)

            # Delete the user
            session.query(User).filter(User.id == user_id).delete()

            session.commit()
            print(f"User with ID {user_id} deleted successfully.")
        except Exception as e:
            session.rollback()
            print(f"An error occurred while deleting the user with ID {user_id}: {str(e)}")
    else:
        print(f"User with ID {user_id} not found.")
    close_session(session)


def add_account_to_existing_user(session, user_id):
    # Check if the user with the given user_id exists
    user = session.query(User).get(user_id)
    if not user:
        print(f"User with ID {user_id} not found.")
        return

    # Create a new account
    user_name = click.prompt("Enter user name for the new account")
    company = click.prompt("Enter company for the new account")
    active = click.confirm("Is the account active?")
    
    # Check if the combination of user_id and user_name already exists
    existing_account = session.query(Account).filter_by(user_id=user_id, user_name=user_name).first()
    if existing_account:
        print(f"Account with user name '{user_name}' already exists for user with ID {user_id}.")
        return

    # Add the new account to the accounts table
    new_account = Account(user_name=user_name, company=company, active=active, user_id=user_id)
    session.add(new_account)
    session.commit()

    # Associate the new account with a new password
    password_value = click.prompt("Enter password for the account")

    new_password = Password(password=password_value)
    new_password.user = user
    new_password.account = new_account
    session.add(new_password)
    session.commit()

    print(f"Account and password added successfully. Account ID: {new_account.id}, Password ID: {new_password.id}")


def update_account(session, user_id, account_id):
    # Check if the user with the given user_id exists
    user = session.query(User).get(user_id)
    if not user:
        print(f"User with ID {user_id} not found.")
        return

    # Check if the account with the given account_id exists for the user
    account = session.query(Account).filter_by(id=account_id, user_id=user_id).first()
    if not account:
        print(f"Account with ID {account_id} not found for user with ID {user_id}.")
        return

    # Gather information to update the account
    new_user_name = click.prompt("Enter new user name (leave empty to keep current):", default=account.user_name)
    new_company = click.prompt("Enter new company (leave empty to keep current):", default=account.company)
    new_active = click.confirm("Is the account active?", default=account.active)

    # Update the account object
    if new_user_name:
        account.user_name = new_user_name
    if new_company:
        account.company = new_company
    account.active = new_active

    # Commit the changes to the database
    session.commit()

    print(f"Account with ID {account_id} for user with ID {user_id} updated successfully.")


def update_password(session, user_id, account_id, password_id):
    # Check if the user with the given user_id exists
    user = session.query(User).get(user_id)
    if not user:
        print(f"User with ID {user_id} not found.")
        return

    # Check if the account with the given account_id exists for the user
    account = session.query(Account).filter_by(id=account_id, user_id=user_id).first()
    if not account:
        print(f"Account with ID {account_id} not found for user with ID {user_id}.")
        return

    # Check if the password with the given password_id exists for the user and account
    password = session.query(Password).filter_by(id=password_id, user_id=user_id, account_id=account_id).first()
    if not password:
        print(f"Password with ID {password_id} not found for user with ID {user_id} and account with ID {account_id}.")
        return

    # Gather information to update the password
    new_password_value = click.prompt("Enter new password (leave empty to keep current):", default=password.password)

    # Update the password object
    if new_password_value:
        password.password = new_password_value

    # Commit the changes to the database
    session.commit()

    print(f"Password with ID {password_id} for user with ID {user_id} and account with ID {account_id} updated successfully.")


def delete_account(account_id):
    session = get_session()
    account = session.query(Account).get(account_id)
    
    if account:
        # Expunge the account from the session, detaching it
        session.expunge(account)

        # Delete all related passwords
        passwords = session.query(Password).filter(Password.account_id == account_id).all()
        for password in passwords:
            session.delete(password)

        # Delete the account
        session.delete(account)
        session.commit()
        print(f"Account with ID {account_id} and associated passwords deleted successfully.")
    else:
        print(f"Account with ID {account_id} not found.")

    close_session(session)

def delete_password(password_id):
    session = get_session()
    password = session.query(Password).get(password_id)
    if password:
        try:
            # Expunge the password from the session, detaching it
            session.expunge(password)
        except InvalidRequestError:
            # The instance is not present in the session, which is fine
            pass

        session.delete(password)
        session.commit()
        print(f"Password with ID {password_id} deleted successfully.")
    else:
        print(f"Password with ID {password_id} not found.")

def update_user(session, user_id):
    # Check if the user with the given user_id exists
    user = session.query(User).get(user_id)
    if not user:
        print(f"User with ID {user_id} not found.")
        return

    # Gather information to update the user
    new_first_name = click.prompt("Enter new first name (leave empty to keep current):", default=user.first_name)
    new_last_name = click.prompt("Enter new last name (leave empty to keep current):", default=user.last_name)
    new_email = click.prompt("Enter new email (leave empty to keep current):", default=user.email)
    new_age = click.prompt("Enter new age (leave empty to keep current):", default=user.age, type=int)

    # Update the user object
    if new_first_name:
        user.first_name = new_first_name
    if new_last_name:
        user.last_name = new_last_name
    if new_email:
        user.email = new_email
    if new_age is not None:
        user.age = new_age

    # Commit the changes to the database
    session.commit()

    print(f"User with ID {user_id} updated successfully.")
    close_session(session)