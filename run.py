#!/usr/bin/env python3.6

import random
from user import User
from credentials import Credentials

# Functions to add credentials


def create_new_credential(account_name, account_password):
    """Function to create a new account and its credentials"""
    new_credential = Credentials(account_name, account_password)
    return new_credential


def save_new_credential(credentials):
    """Function to save the newly created account and password"""
    credentials.save_credentials()


def find_credential(account_name):
    """Function that finds credentials based on account_name given"""
    return Credentials.find_by_name(account_name)


def check_existing_credentials(name):
    """Method that checks whether a partinular account and its credentials exist based on searched account_name"""
    return Credentials.find_by_name(name)


def display_credentials():
    """Function which displays all saved credentials"""
    return Credentials.display_credentials()


def copy_credentials():
    '''
    Function to copy a credentials details to the clipboard
    '''
    return Credentials.copy_credentials()


def delete_credential(credentials):
    """
    Method that deletes credentials
    """
    return Credentials.delete_credential(credentials)


def main():

    while True:
        print("Welcome to PassKeeper.")
        print('\n')
        print("Use these short codes to select an option: Create New User use 'nu': Sign in to your account use 'si' or 'ex' to exit password locker")
        short_code = input().lower()
        print('\n')

        if short_code == 'nu':
            print("Create a UserName")
            created_user_name = input()

            print("Enter a Password")
            created_user_password = input()

            print("Confirm Your Password")
            confirm_password = input()

            while confirm_password != created_user_password:
                print("Sorry passwords Missmatch!")
                print("Enter a password")
                created_user_password = input()
                print("Confirm Your Password")
                confirm_password = input()
            else:
                print(
                    f"Congratulations {created_user_name}! Your account was successfully created")
                print('\n')
                print("Kindly Sign In to your Account")
                print("Username")
                entered_userName = input()
                print("Your Password")
                entered_password = input()

                while entered_userName != created_user_name or entered_password != created_user_password:
                    print("You entered a wrong username or password")
                    print("Username")
                    entered_userName = input()
                    print("Your Password")
                    entered_password = input()
                else:
                    print(f"Welcome: {entered_userName} to your Account")
                    print('\n')

                    print(
                        "Select an option below to continue: Enter vs, nc, rc, sc or so")
                    print('\n')

                while True:
                    print("vs: View Your saved credentials")
                    print("nc: Add new credentials")
                    print("rc: Remove credentials")
                    print("sc: Search credentials")
                    print("so: Sign Out")
                    option = input()

                    if option == 'nc':
                        while True:
                            print("Continue to add? y/n")

                            choice = input().lower()
                            if choice == 'y':
                                print("Enter Account Name")
                                account_name = input()
                                print("Enter a password")
                                print(
                                    "To generate random password enter keyword 'gp' or 'n' to create your own password")
                                keyword = input().lower()
                                if keyword == 'gp':
                                    account_password = random.randint(
                                        111111, 1111111)
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')
                                elif keyword == 'n':
                                    print("Create your password")
                                    account_password = input()
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')

                                else:
                                    print("Please enter a valid Code")

                                save_new_credential(create_new_credential(
                                    account_name, account_password))
                            elif choice == 'n':
                                break
                            else:
                                print("Please use 'y' for yes or 'n' for no!")
                    elif option == 'vs':
                        while True:
                            print("Here are  all your credentials")
                            if display_credentials():

                                for credential in display_credentials():
                                    print(
                                        f"ACCOUNT NAME:{credential.account_name}")
                                    print(
                                        f"PASSWORD:{credential.account_password}")

                            else:
                                print('\n')
                                print("You don't seem to have any contacts yet")
                                print('\n')

                            print("Back to Menu? y/n")

                            back = input().lower()
                            if back == 'y':
                                break
                            elif back == 'n':
                                continue
                            else:
                                print("Please Enter a valid code")
                                continue

                    elif option == 'so':
                        print(
                            "WARNING! You will loose all your credentials if you log out. Are you sure? y/n")
                        logout = input().lower()

                        if logout == 'y':
                            print("You have Successfully signed out")
                            break
                        elif logout == 'n':
                            continue
                    elif option == 'rc':
                        while True:
                            print("Search for credential to delete")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(
                                    search_name)
                                print(
                                    f"ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                                print("Delete? y/n")
                                sure = input().lower()
                                if sure == 'y':
                                    delete_credential(search_credential)
                                    print("Account SUCCESSFULLY deleted")
                                    break
                                elif sure == 'n':
                                    continue

                            else:
                                print("That Contact Does not exist")
                                break

                    elif option == 'sc':
                        while True:
                            print("Continue? y/n")
                            option2 = input().lower()
                            if option2 == 'y':
                                print("Enter an account name to find credentials")

                                search_name = input()

                                if check_existing_credentials(search_name):
                                    search_credential = find_credential(
                                        search_name)
                                    print(
                                        f"ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                                else:
                                    print("That Contact Does not exist")
                            elif option2 == 'n':
                                break
                            else:
                                print("Please enter a valid code")

                    else:
                        print("Please enter a valid code")
                        continue

        elif short_code == 'si':
            print("WELCOME")
            print("Enter UserName")
            default_user_name = input()

            print("Enter Your password")
            default_user_password = input()
            print('\n')

            while default_user_name != 'testuser' or default_user_password != '1234echo':
                print(
                    "Wrong userName or password. Username 'testuser' and password '1234echo'")
                print("Enter UserName")
                default_user_name = input()

                print("Enter Your password")
                default_user_password = input()

                print('\n')

            if default_user_name == 'testuser' and default_user_password == '1234echo':
                print("YOU HAVE SUCCESSFULLY LOGGED IN!")
                print('\n')
                print("Select an option below to continue: Enter vs, nc, rc, sc or so")
                print('\n')

            while True:
                print("vs: View Your saved credentials")
                print("nc: Add new credentials")
                print("rc: Remove credentials")
                print("sc: Search credentials")
                print("so: Log Out")
                option = input()

                if option == 'nc':
                    while True:
                        print("Continue to add? y/n")

                        choice = input().lower()
                        if choice == 'y':
                            print("Enter The Account Name")
                            account_name = input()
                            print("Enter a password")
                            print(
                                "To generate random password enter keyword 'gp' or 'n' to create your own password")
                            keyword = input().lower()
                            if keyword == 'gp':
                                account_password = random.randint(
                                    111111, 1111111)
                                print(f"Account: {account_name}")
                                print(f"Password: {account_password}")
                                print('\n')
                            elif keyword == 'n':
                                print("Create your password")
                                account_password = input()
                                print(f"Account: {account_name}")
                                print(f"Password: {account_password}")
                                print('\n')

                            else:
                                print("Please enter a valid Code")

                            save_new_credential(create_new_credential(
                                account_name, account_password))
                        elif choice == 'n':
                            break
                        else:
                            print("Please use 'y' for yes or 'n' for no!")
                elif option == 'vs':
                    while True:
                        print("Below is a list of all your credentials")
                        if display_credentials():

                            for credential in display_credentials():
                                print(
                                    f"ACCOUNT NAME:{credential.account_name}")
                                print(
                                    f"PASSWORD:{credential.account_password}")

                        else:
                            print('\n')
                            print("You don't seem to have any contacts yet")
                            print('\n')

                        print("Back to Menu? y/n")

                        back = input().lower()
                        if back == 'y':
                            break
                        elif back == 'n':
                            continue
                        else:
                            print("Please Enter a valid code")
                        # elif choice1 == 'n':
                        #     break
                        # else:
                        #     print("Please use y or n")
                elif option == 'so':
                    print(
                        "Kindly Note thar files are saved as per session and will be lost if you sign out. Are you sure? y/n")
                    logout = input().lower()

                    if logout == 'y':
                        print("You have Successfully logged out")
                        break
                    elif logout == 'n':
                        continue

                elif option == 'rc':
                    while True:
                        print("Search for credential to delete")

                        search_name = input()

                        if check_existing_credentials(search_name):
                            search_credential = find_credential(search_name)
                            print(
                                f"ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                            print("Delete? y/n")
                            sure = input().lower()
                            if sure == 'y':
                                delete_credential(search_credential)
                                print("Account SUCCESSFULLY deleted")
                                break
                            elif sure == 'n':
                                continue

                        else:
                            print("That Contact Does not exist")
                            break

                elif option == 'sc':
                    while True:
                        print("Continue? y/n")
                        option2 = input().lower()
                        if option2 == 'y':
                            print("Enter an account name to find credentials")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(
                                    search_name)
                                print(
                                    f"ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                            else:
                                print("That Contact Does not exist")
                        elif option2 == 'n':
                            break
                        else:
                            print("Please enter a valid code")

                elif option == 'sc':
                    while True:
                        print("Continue? y/n")
                        option2 = input().lower()
                        if option2 == 'y':
                            print("Enter an account name to find credentials")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(
                                    search_name)
                                print(
                                    f"ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                            else:
                                print("That Contact Does not exist")
                        elif option2 == 'n':
                            break
                        else:
                            print("Please enter a valid code")
                else:
                    print("Please enter a valid code")
        elif short_code == 'ex':
            break
        else:
            print("Please Enter a valid code to continue")


if __name__ == '__main__':
    main()
