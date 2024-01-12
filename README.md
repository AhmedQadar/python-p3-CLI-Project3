## MODELS 

    1-    user_account Table Definition:

            user_account = Table('user_account', Base.metadata, Column('user_id', ForeignKey('users.id'), primary_key=True), Column('account_id', ForeignKey('accounts.id'), primary_key=True), extend_existing=True)
            Defines a table named user_account with columns user_id and account_id, serving as a many-to-many association table between users and accounts.


    2-    User Class Definition:

            accounts = relationship('Account', secondary=user_account, back_populates='users')
            Establishes a many-to-many relationship between User and Account through the user_account association table.


    3-    Account Class Definition:

            users = relationship('User', secondary=user_account, back_populates='accounts')
            Establishes a many-to-many relationship between Account and User through the user_account association table.


    4-    Password Class Definition:

            account_id = Column(Integer(), ForeignKey('accounts.id'))

            Creates a foreign key relationship between the Password table and the accounts table using the account_id column.

            user_id = Column(Integer(), ForeignKey('users.id'))

            Creates a foreign key relationship between the Password table and the users table using the user_id column.


## METHODS 

                                   ### DISPLAY METHODS ###


    1-    display_users Function:

            all_users = Session().query(User).all()

            Retrieves all user records from the User table using the SQLAlchemy session.
            for user in all_users:

            Iterates through each user record in all_users.
            print(f"ID: {user.id} | Name: {user.first_name} {user.last_name} | Email: {user.email} | Age: {user.age}")

            Prints formatted information for each user, including ID, name, email, and age.
            display_accounts Function:

    2-    all_accounts = Session().query(Account).all()

            Retrieves all account records from the Account table using the SQLAlchemy session.
            for account in all_accounts:

            Iterates through each account record in all_accounts.
            print(f"ID: {account.id} | User Name: {account.user_name} | Company: {account.company} | Active: {account.active}")

            Prints formatted information for each account, including ID, user name, company, and active status.
            display_passwords Function:

    3-    all_passwords = Session().query(Password).all()

            Retrieves all password records from the Password table using the SQLAlchemy session.
            for password in all_passwords:

            Iterates through each password record in all_passwords.
            print(f"ID: {password.id} | Password: {password.password} | User ID: {password.user_id} | Account ID: {password.account_id}")

            Prints formatted information for each password, including ID, password value, user ID, and account ID.


                                   ### USER METHODS ###


    1-    find_user_by_id Function:

            Retrieves a user with a given user_id from the User table.
            Prints user details if found, otherwise, prints a message that the user was not found.

    2-    all_details_of_user Function:

            Retrieves a user with a given user_id from the User table.
            Constructs a dictionary (user_details) containing various details about the user, accounts, and passwords.
            Prints the details of the user, accounts, and passwords in a structured format.

    3-    number_of_active_accounts Function:

            Retrieves a user with a given user_id from the User table.
            Counts the number of active accounts and prints the count.
            Constructs a list of tuples (active_accounts_tuple) containing details of each active account.
            Prints details of each active account and returns the list of tuples.

    4-    number_of_accounts Function:

            Retrieves a user with a given user_id from the User table.
            Counts the total number of accounts for the user and prints the count.

    5-    accounts_and_passwords Function:

            Retrieves a user with a given user_id from the User table.
            Prints details of each account for the user, including account ID, user name, company, and active status.
            Prints the passwords associated with each account.


                                    ### ACCOUNT METHODS ###


    1-    find_account_by_user_name Function:

            Queries the Account table to find an account based on the provided user_name.
            Prints details of the found account if it exists; otherwise, prints a message that the account was not found.


    2-    account_owner Function:

            Joins the User table with the Account table to find the user who owns an account with the given user_name.
            Prints details of the found user (account owner) if it exists; otherwise, prints a message that the account was not found.


    3-    account_password Function:

            Joins the Password table with the Account table to find the password associated with an account based on the provided user_name.
            Prints the password of the found account if it exists; otherwise, prints a message that the account was not found.


    4-    account_company Function:

            Queries the Account table to find details of an account based on the provided user_name.
            Prints the company associated with the found account if it exists; otherwise, prints a message that the account was not found.


                                     ###  PASSWORD METHODS ###


    1-    find_password_by_id Function:

            Queries the Password table to find a password based on the provided password_id.
            Prints details of the found password if it exists; otherwise, prints a message that the password was not found.


    2-    account_for_password Function:

            Joins the Account table with the Password table to find the account associated with a password based on the provided password_id.
            Prints details of the found account for the password if it exists; otherwise, prints a message that the password was not found.


    3-    owner Function:

            Joins the User table with the Password table to find the owner (user) associated with a password based on the provided password_id.
            Prints details of the found user (owner) for the password if it exists; otherwise, prints a message that the password was not found.


                                ### CRUD METHODS ###


    1-    add_user_account_password Function:

            Adds a new user, account, and password to the database.
            Collects user information (first name, last name, email, and age) through prompts.
            Creates a new user, adds it to the session, and commits the transaction.
            Collects account information (user name, company, and active status) through prompts.
            Creates a new account associated with the user, adds it to the session, and commits the transaction.
            Collects password information through prompts, creates a new password associated with the user and account, adds it to the session, and commits the transaction.
            Prints a success message with the IDs of the newly added user, account, and password.


    2-    delete_user Function:

            Deletes a user and all associated accounts and passwords based on the provided user_id.
            Rolls back the transaction in case of an error during deletion.
            Prints success or error messages based on the outcome.


    3-    add_account_to_existing_user Function:

            Adds a new account to an existing user in the database.
            Collects account information (user name, company, and active status) through prompts.
            Checks if the combination of user_id and user_name already exists; if so, prints an error message and returns.
            Creates a new account associated with the user, adds it to the session, and commits the transaction.
            Collects password information through prompts, creates a new password associated with the user and account, adds it to the session, and commits the transaction.
            Prints a success message with the IDs of the newly added account and password.


    4-    update_account Function:

            Updates an existing account's information based on the provided user_id and account_id.
            Gathers information for updating the account (new user name, new company, and new active status) through prompts.
            Updates the account object with the new information and commits the transaction.
            Prints a success message.


    5-    update_password Function:

            Updates an existing password's information based on the provided user_id, account_id, and password_id.
            Gathers information for updating the password (new password value) through prompts.
            Updates the password object with the new information and commits the transaction.
            Prints a success message.


    6-    delete_account Function:

            Deletes an account and all associated passwords based on the provided account_id.
            Expunges the account from the session and deletes all related passwords.
            Commits the transaction and prints a success message.


    7-    delete_password Function:

            Deletes a password based on the provided password_id.
            Expunges the password from the session and commits the transaction.
            Prints a success message.


    8-    update_user Function:

            Updates an existing user's information based on the provided user_id.
            Gathers information for updating the user (new first name, new last name, new email, and new age) through prompts.
            Updates the user object with the new information and commits the transaction.
            Prints a success message.


