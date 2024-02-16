import gspread
from google.oauth2.service_account import Credentials
from cardUser import cardUser
from rich import print
import time
import datetime
import os
import sys
from rich.progress import track

# This code is taken from Love Sandwiches Project
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("user_database")

def clear():
    """ This function will clear the terminal screen
      based on the operating system."""
# This code was taken from stack overflow
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def welcome_message():
    """ Print welcome message at the begining"""
    clear()
    now = datetime.datetime.now()
    print(now.strftime("      [cyan]%A       %Y-%m-%d  %H:%M:%S[/]"))
    time.sleep(0.2)
    print("[green]==================================================[/]")
    time.sleep(0.2)
    print("      [cyan]Welcome to[/]   [bright_magenta]Commerz Bank[/]")
    time.sleep(0.2)
    print("[green]==================================================[/]")
    time.sleep(0.2)


def display_menu():
    """ Print options to the user """
    print("[cyan]Select one of the options to proceed.[/]\n")
    print("\n      [green]**__[/] [bright_magenta]MENU[/] [green]__**[/]")
    time.sleep(0.2)
    print("\n      [green]1. BALANCE[/]")
    time.sleep(0.2)
    print("      [yellow]2. DEPOSIT[/]")
    time.sleep(0.2)
    print("      [blue]3. WITHDRAW[/]")
    time.sleep(0.2)
    print("      [bright_magenta]4. Change PIN[/]")
    time.sleep(0.2)
    print("      [bright_magenta]5. Show PIN[/]")
    time.sleep(0.2)
    print("      [red]6. EXIT[/]")
    time.sleep(0.2)
    print()
    print("[green]==================================================[/]")
    time.sleep(0.2)


def validate_card():
    """Card number validation of the user, showing errors if the card is not inserted or not valid
    """
    list_of_users = SHEET.worksheet("user").get_all_values()[1:]
    while True:
        time.sleep(0.2)
        inserted_card = input("\nPlease insert your CARD: ")
        user = [holder for holder in list_of_users if inserted_card == holder[0]]
        if inserted_card and len(user) > 0:
            break
        elif not inserted_card:
            time.sleep(0.2)
            print("\nPlease insert your card number.")
        else:
            time.sleep(0.2)
            print("\n[red]Your card number doesn't exist![/]")
    return cardUser(user[0][0], user[0][1], user[0][2], user[0][3], user[0][4])


def proccess_data():
    """ This code was taken from
        https://www.freecodecamp.org/news/use-the-rich-library-in-python/
        How to display a progress bar using rich"""
    time.sleep(0.02)


def validate_user(cardUser):
    # Pin code number validation
    list_of_users = SHEET.worksheet("user").get_all_values()[1:]
    user = [
        holder
        for holder in list_of_users
        if cardUser.get_cardNum() == holder[0]
    ]
    attempts = 0
    while attempts < 3:
        attempts += 1
        time.sleep(0.2)
        inserted_pin = input("\nPlease enter PIN: ")
        if not inserted_pin:
            print("\n[cyan]Please enter PIN.[/]\n")
            status = False
        elif not inserted_pin.isnumeric():
            clear()
            print("\n[cyan]Only numbers allowed.Try again.[/]\n")
            sys.exit()
        elif inserted_pin.isnumeric() and inserted_pin == user[0][1]:
            status = True
            break
        elif attempts == 3:
            time.sleep(0.2)
            clear()
            print("\n[red]Sorry you've exceeded your trial limit[/]\n")
            status = False
            sys.exit()
        else:
            print("\n[red]Incorrect PIN, try again.[/]\n")
            status = False
    return status

def show_balance(cardUser):
    """Check balance function
    """
    list_of_users = SHEET.worksheet("user").get_all_values()[1:]
    user = [
        holder
        for holder in list_of_users
        if cardUser.get_cardNum() == holder[0]
    ]
    return user[0][4]

def show_user_name(cardUser):
    list_of_users= SHEET.worksheet("user").get_all_values()[1:]
    user = [
        holder
        for holder in list_of_users
        if cardUser.get_cardNum() == holder[0]
    ]
    return user[0][2]

def show_pin(cardUser):
    list_of_users= SHEET.worksheet("user").get_all_values()[1:]
    user = [
        holder
        for holder in list_of_users
        if cardUser.get_cardNum() == holder[0]
    ]
    return user[0][1]

def change_pin(cardUser):
    """ - Creating the pin function, Validation of numeric
      - Updating pin on spreadsheet """
    list_of_users= SHEET.worksheet("user").get_all_values()[1:]
    user = [
        holder
        for holder in list_of_users
        if cardUser.get_cardNum() == holder[0]
    ]
    while True:
        time.sleep(0.2)
        new_pin = input("\nEnter a new 4-digit PIN: ")
        if new_pin.isdigit() and len(new_pin) == 4:
            status = True
            cardUser.set_pin(new_pin)
            current_user = SHEET.worksheet("user").find(user[0][0])
            SHEET.worksheet("user").update_cell(current_user.row, 2, new_pin)
            for _ in track(range(100), description='[green]Processing data'):
                proccess_data()
            print("\n[green]PIN successfully changed.[/]\n")
            break
        else:
            print("\n[red]Please enter a valid 4-digit PIN.[/]\n")
    return True

def deposit(cardUser):
    # Deposit menu function and validation of numeric
    list_of_users = SHEET.worksheet("user").get_all_values()[1:]
    user = [
        holder
        for holder in list_of_users
        if cardUser.get_cardNum() == holder[0]
    ]
    while True:
        input_deposit = input("\nHow much would you like to deposit: € ")
        if not input_deposit:
            print("\n[cyan]Please enter an amount, try again.[/]")
            status = False
        elif not input_deposit.isnumeric():
            print("\n[cyan]Enter only amount in figures.[/]")
            status = False
        else:
            status = True
            new_balance = float(cardUser.get_balance()) + float(input_deposit)
            cardUser.set_balance(new_balance)
            cur_user = SHEET.worksheet("user").find(user[0][0])
            SHEET.worksheet("user").update_cell(cur_user.row, 5, new_balance)
            print("\n[green]Successfully deposited to your account.[/]")
            break
    return True

def withdraw(cardUser):
    """ - Creating a function for the Deposit proccess
      - Validation of numeric
      - Updating the balance at the database """

    list_of_users = SHEET.worksheet("user").get_all_values()[1:]
    user = [
        holder
        for holder in list_of_users
        if cardUser.get_cardNum() == holder[0]
    ]
    while True:
        time.sleep(0.2)
        input_withdraw = input("\nHow much would you like to withdraw: € ")
        if not input_withdraw:
            print("\n [cyan]Please enter an amount to withdraw.[/]\n")
            status = False
        elif not input_withdraw.isnumeric():
            print("\nEnter only amount in figures.")
            status = False
        elif float(cardUser.get_balance()) < float(input_withdraw):
            print("\n[red]Insufficient balance. Try again.[/]")
            status = False
        else:
            status = True
            new_balance = float(cardUser.get_balance()) - float(input_withdraw)
            cardUser.set_balance(new_balance)
            current_user = SHEET.worksheet("user").find(user[0][0])
            SHEET.worksheet("user").update_cell(current_user.row, 5, new_balance)
            print("\n[green]Successfully withdraw![/]\n")
            break
    return True


def main():
    """
    A function that runs all the program functions
    """
    welcome_message()
    current_user = validate_card()
    validate_user(current_user)
    clear()
    for _ in track(range(100), description='[green]Processing data'):
                proccess_data()
    print("\nWelcome ", show_user_name(current_user), " :)\n")
    option = 0
    while True:
        display_menu()
        try:
            option = int(input("Enter here your option:  "))
            time.sleep(0.2)
            print("[green]===================================+=====[/]")
        except ValueError:
            time.sleep(0.2)
            print("\n    [red]Invalid input. Please try again.[/]\n")
            continue  # Restart the loop if invalid input is given
        if option == 1:
            clear()
            show_balance(current_user)
            for _ in track(range(100), description='[green]Processing data'):
                proccess_data()
            print("\n [cyan]Your balance is: € [/]", show_balance(current_user))
            print("[green]===========================================[/]")
        elif option == 2:
            time.sleep(0.2)
            clear()
            deposit(current_user)
        elif option == 3:
            time.sleep(0.2)
            clear()
            withdraw(current_user)
        elif option == 4:
            time.sleep(0.2)
            clear()
            change_pin(current_user)
        elif option == 5:
            clear()
            show_pin(current_user)
            for _ in track(range(100), description='[green]Processing data'):
                proccess_data()
            print("\n [cyan]Your PIN is: € [/]", show_pin(current_user))
            print("[green]===========================================[/]")
        elif option == 6:
            time.sleep(0.2)
            clear()
            time.sleep(0.2)
            print("[green]=============================================[/]")
            time.sleep(0.2)
            print("[red]You exit the ATM!![/]\n")
            time.sleep(0.2)
            print("[green]Have a nice day!![/]\n")
            time.sleep(0.2)
            print("[green]==============================================[/]")
            time.sleep(0.2)
            break
        else:
            print("\n [red]Invalid option. Please try again.[/]\n")


main()