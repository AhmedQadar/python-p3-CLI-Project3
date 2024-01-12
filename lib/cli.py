import click
from click_spinner import spinner as click_spinner
from helpers import (
    read_banner_from_file,
    display_users,
    display_accounts,
    display_passwords,
    find_user_by_id,
    find_account_by_user_name,
    find_password_by_id,
    add_user_account_password,
    delete_user,
    number_of_accounts,
    get_session,
    close_session,
    accounts_and_passwords,
    all_details_of_user,
    number_of_active_accounts,
    delete_account, 
    delete_password,
    account_owner,
    account_password,
    account_company,
    add_account_to_existing_user,
    account_for_password,
    owner,
    update_user,
    update_account,
    update_password
)

@click.group()
def main():
    pass

                                        ### DISPLAY METHODS ###


# @main.command()
# def display_all_users():
#     with click_spinner():
#         click.echo("Displaying all users...")
#         display_users()

# @main.command()
# def display_all_accounts():
#     with click_spinner():
#         click.echo("Displaying all accounts...")
#         display_accounts()

# @main.command()
# def display_all_passwords():
#     with click_spinner():
#         click.echo("Displaying all passwords...")
#         display_passwords()  

@main.command()
def display_all():
    click.echo("\n==================== Display Options ====================")
    click.echo("1. Display all users")
    click.echo("2. Display all accounts")
    click.echo("3. Display all passwords")
    click.echo("==========================================================")

    option = click.prompt("Choose what to display (1, 2, or 3):", type=int)

    with click_spinner():
        if option == 1:
            click.echo("\n👥 Displaying all users:")
            display_users()
        elif option == 2:
            click.echo("\n💼 Displaying all accounts:")
            display_accounts()
        elif option == 3:
            click.echo("\n🔐 Displaying all passwords:")
            display_passwords()
        else:
            click.echo("\n❌ Invalid option. Please choose 1, 2, or 3.")


                                        ### USER METHODS ###


# @main.command()
# def find_user_by_id_cmd():
#     click.echo("Find user by ID")
#     user_id = click.prompt("Enter user ID", type=int)
#     find_user_by_id(user_id)
    
# @main.command()
# def all_details_of_user_cmd():
#     click.echo("All details of user")
#     user_id = click.prompt("Enter user ID", type=int)
#     session = get_session()
#     all_details_of_user(user_id)
#     close_session(session)

# @main.command()
# def find_active_accounts_cmd():
#     click.echo("Find active accounts")
#     user_id = click.prompt("Enter user ID", type=int)
#     find_active_accounts(user_id)

# @main.command()
# def number_of_accounts_cmd():
#     click.echo("Number of accounts")
#     user_id = click.prompt("Enter user ID", type=int)
#     number_of_accounts(user_id)

# @main.command()
# def accounts_and_passwords_cmd():
#     click.echo("Accounts and passwords")
#     user_id = click.prompt("Enter user ID", type=int)
#     accounts_and_passwords(user_id)

@main.command()
def user_operations():
    click.echo("\n==================== User Operations ====================")
    click.echo("1. Find user by ID 🕵️‍♂️")
    click.echo("2. All details of user ℹ️")
    click.echo("3. Find active accounts 🔍")
    click.echo("4. Number of accounts 🔢")
    click.echo("5. Accounts and passwords 🔐")
    click.echo("==========================================================")

    option = click.prompt("Choose a user operation (1-5):", type=int)

    with click_spinner():
        if option == 1:
            click.echo("Find user by ID")
            user_id = click.prompt("Enter user ID", type=int)
            find_user_by_id(user_id)
        elif option == 2:
            click.echo("All details of user")
            user_id = click.prompt("Enter user ID", type=int)
            session = get_session()
            all_details_of_user(user_id)
            close_session(session)
        elif option == 3:
            click.echo("Find active accounts")
            user_id = click.prompt("Enter user ID", type=int)
            number_of_active_accounts(user_id)
        elif option == 4:
            click.echo("Number of accounts")
            user_id = click.prompt("Enter user ID", type=int)
            number_of_accounts(user_id)
        elif option == 5:
            click.echo("Accounts and passwords")
            user_id = click.prompt("Enter user ID", type=int)
            accounts_and_passwords(user_id)
        else:
            click.echo("\n❌ Invalid option. Please choose 1, 2, 3, 4, or 5.")


    
                                         ### ACCOUNT METHODS ###


# @main.command()
# def find_account_by_user_name_cmd():
#     with click_spinner():
#         click.echo("Find account by user name")
#         user_name = click.prompt("Enter user name")
#         find_account_by_user_name(user_name)

# @main.command()
# def account_owner_cmd():
#     with click_spinner():
#         click.echo("Find account owner")
#         user_name = click.prompt("Enter user name")
#         account_owner(user_name)

# @main.command()
# def account_password_cmd():
#     with click_spinner():
#         click.echo("Find account password")
#         user_name = click.prompt("Enter user name")
#         account_password(user_name)


# @main.command()
# def account_company_cmd():
#     with click_spinner():
#         click.echo("Find company for this account")
#         user_name = click.prompt("Enter user name")
#         account_company(user_name)

@main.command()
def account_operations():
    click.echo("\n==================== Account Operations ====================")
    click.echo("1. Find account by user name 🔍")
    click.echo("2. Find account owner 👤")
    click.echo("3. Find account password 🔐")
    click.echo("4. Find company for this account 🏢")
    click.echo("==========================================================")

    option = click.prompt("Choose an account operation (1-4):", type=int)

    with click_spinner():
        if option == 1:
           click.echo("Find account by user name")
           user_name = click.prompt("Enter user name")
           find_account_by_user_name(user_name) 
        elif option == 2:
            click.echo("Find account owner")
            user_name = click.prompt("Enter user name")
            account_owner(user_name)
        elif option == 3:
            click.echo("Find account password")
            user_name = click.prompt("Enter user name")
            account_password(user_name)
        elif option == 4:
            click.echo("Find company for this account")
            user_name = click.prompt("Enter user name")
            account_company(user_name)
        else:
            click.echo("\n❌ Invalid option. Please choose 1, 2, 3, or 4.")


                                          ### PASSWORD METHODS ###


# @main.command()
# def find_password_by_id_cmd():
#     with click_spinner():
#         click.echo("Find password by ID")
#         password_id = click.prompt("Enter password ID", type=int)
#         find_password_by_id(password_id)

# @main.command()
# def account_for_password_cmd():
#     with click_spinner():
#         click.echo("Find account for password")
#         password_id = click.prompt("Enter password ID", type=int)
#         account_for_password(password_id)

# @main.command()
# def owner_cmd():
#     with click_spinner():
#         click.echo("Find owner of password ")
#         password_id = click.prompt("Enter password ID", type = int)
#         owner(password_id)


@main.command()
def password_operations():
    click.echo("\n==================== Password Operations ====================")
    click.echo("1. Find password by ID 🔍")
    click.echo("2. Find account for password 👤")
    click.echo("3. Find owner of password 🕵️‍♂️")
    click.echo("==========================================================")

    option = click.prompt("Choose a password operation (1-3):", type=int)

    with click_spinner():
        if option == 1:
            click.echo("Find password by ID")
            password_id = click.prompt("Enter password ID", type=int)
            find_password_by_id(password_id) 
        elif option == 2:
            click.echo("Find account for password")
            password_id = click.prompt("Enter password ID", type=int)
            account_for_password(password_id)
        elif option == 3:
            click.echo("Find owner of password ")
            password_id = click.prompt("Enter password ID", type = int)
            owner(password_id)
        else:
            click.echo("\n❌ Invalid option. Please choose 1, 2, or 3.")


                                          ### CRUD METHODS  ###



# @main.command()
# def delete_user_cmd():
#     with click_spinner():
#         user_id = click.prompt("Enter user ID to delete", type=int)
#         delete_user(user_id)

# @main.command()
# def add_account_to_existing_user_cmd():
#     with click_spinner():
#          session = get_session()
#          user_id = click.prompt("Enter user ID to add account", type = int)
#          add_account_to_existing_user(session, user_id)
#     close_session(session)


# @main.command()
# def delete_account_cmd():
#     with click_spinner():
#         account_id = click.prompt("Enter account ID to delete", type=int)
#         delete_account(account_id)

# @main.command()
# def delete_password_cmd():
#     with click_spinner():
#         password_id = click.prompt("Enter password ID to delete", type=int)
#         delete_password(password_id)

# @main.command()
# def add_user_account_password_cmd():
#     session = get_session()
#     with click_spinner():
#         add_user_account_password(session)
#     close_session(session)

@main.command()
def delete_operations():
    click.echo("\n==================== Delete Operations ====================")
    click.echo("1. Delete User 🗑️")
    click.echo("2. Delete Account 🗑️")
    click.echo("3. Delete Password 🗑️")
    click.echo("==========================================================")

    option = click.prompt("Choose a management operation (1-3):", type=int)

    with click_spinner():
        if option == 1:
            with click_spinner():
                user_id = click.prompt("Enter user ID to delete", type=int)
                delete_user(user_id)
        elif option == 2:
            with click_spinner():
                account_id = click.prompt("Enter account ID to delete", type=int)
                delete_account(account_id)
        elif option == 3:
            with click_spinner():
                password_id = click.prompt("Enter password ID to delete", type=int)
                delete_password(password_id)
        else:
            click.echo("\n❌ Invalid option. Please choose 1, 2, 3, 4, or 5.")




                                            ### ADD METHODS ###

# @main.command()
# def add_account_to_existing_user_cmd():
#     with click_spinner():
#          session = get_session()
#          user_id = click.prompt("Enter user ID to add account", type = int)
#          add_account_to_existing_user(session, user_id)
#     close_session(session)


# @main.command()
# def add_user_account_password_cmd():
#     session = get_session()
#     with click_spinner():
#         add_user_account_password(session)
#     close_session(session)


@main.command()
def add_operations():
    click.echo("\n==================== Add Operations ====================")
    click.echo("1. Add Account to Existing User 🆕")
    click.echo("2. Add User, Account, and Password 🆕")
    click.echo("==========================================================")

    option = click.prompt("Choose a management operation (1-2):", type=int)

    with click_spinner():
        if option == 1:
            with click_spinner():
                session = get_session()
                user_id = click.prompt("Enter user ID to add account to ", type=int)
                add_account_to_existing_user(session, user_id)
            close_session(session)
        elif option == 2:
            session = get_session()
            with click_spinner():
                add_user_account_password(session)
            close_session(session)
        else:
            click.echo("\n❌ Invalid option. Please choose 1 or 2.")




                                            ### UPDATE METHODS ###



# @main.command()
# def update_user_cmd():
#     with click_spinner():
#         session = get_session()
#         user_id = click.prompt("Enter user ID to be updated", type=int)
#         update_user(session, user_id)
#     close_session(session)

# @main.command()
# def update_account_cmd():
#     with click_spinner():
#         session = get_session()
#         user_id = click.prompt("Enter user ID for account", type=int)
#         account_id = click.prompt("Enter account ID to update", type=int)
#         update_account(session, user_id, account_id)
#     close_session(session)

# @main.command()
# def update_password_cmd():
#     with click_spinner():
#         session = get_session()
#         user_id = click.prompt("Enter user ID for account", type=int)
#         account_id = click.prompt("Enter account ID for password", type=int)
#         password_id = click.prompt("Enter password ID ", type=int)
#         update_password(session, user_id, account_id, password_id)
#     close_session(session) 

@main.command()
def update_operations():
    click.echo("\n==================== Update Operations ====================")
    click.echo("1. Update User ✏️")
    click.echo("2. Update Account ✏️")
    click.echo("3. Update Password ✏️")
    click.echo("==========================================================")

    option = click.prompt("Choose a management operation (1-3):", type=int)

    with click_spinner():
        if option == 1:
            with click_spinner():
                session = get_session()
                user_id = click.prompt("Enter user ID to be updated", type=int)
                update_user(session, user_id)
            close_session(session)
        elif option == 2:
            with click_spinner():
                session = get_session()
                user_id = click.prompt("Enter user ID for account", type=int)
                account_id = click.prompt("Enter account ID to update", type=int)
                update_account(session, user_id, account_id)
            close_session(session)
        elif option == 3:
            with click_spinner():
                session = get_session()
                user_id = click.prompt("Enter user ID for account", type=int)
                account_id = click.prompt("Enter account ID for password", type=int)
                password_id = click.prompt("Enter password ID ", type=int)
                update_password(session, user_id, account_id, password_id)
            close_session(session) 
        else:
            click.echo("\n❌ Invalid option. Please choose 1, 2, or 3.")



if __name__ == "__main__":
    banner = read_banner_from_file('./banner.txt')
    if banner:
       click.echo(banner)
    main()