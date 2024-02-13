import gspread
from google.oauth2.service_account import Credentials
from userData import UserData
from rich import print
import time
import datetime
import os
import sys
from rich.progress import track
from time import sleep

# This code is taken from Love Sandwiches Project
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('atm_python')

user_data = SHEET.worksheet('data-user')
#Prints a list of users by row
list_of_users = user_data.get_all_values()[1:] # Creating a list of lists


def clear():
    """This function will clear the terminal screen based on the operating system. 
       It checks the operating system and then executes the appropriate command
       (cls for Windows and clear for Linux/Mac) using os.system()."""

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def welcome_message():
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
    print("      [red]5. EXIT[/]")
    time.sleep(0.2)
    print()
    print("[green]==================================================[/]")
    time.sleep(0.2)


def validate_card_and_pin(userData):
    """Validate the card and PIN entered by the user."""
    attempts = 0
    while attempts < 3:
        time.sleep(0.2)
        inserted_card = input("\nPlease insert your CARD: ")
        if not inserted_card:
            print("\nPlease insert your card number.")
            continue

        user = [holder_card for holder_card in list_of_users if inserted_card == holder_card[2]]
        if user:
            time.sleep(0.3)
            break
        else:
            print("\n[red]Your card number doesn't exist![/]")
            attempts += 1

    if attempts == 3:
        clear()
        print("\n[red]Sorry you've exceeded your trial limit[/]\n")
        sys.exit()
        return False

    attempts = 0
    while attempts < 3:
        time.sleep(0.2)
        inserted_pin = input("\nPlease enter PIN: ")
        if not inserted_pin:
            print("\n[cyan]Please enter PIN.[/]\n")
            attempts += 1
            continue

        elif not inserted_pin.isnumeric():
            clear()
            print("\n[cyan]Only numbers allowed. Insert your card and try again.[/]\n")
            sys.exit()
            return False

        elif inserted_pin == user[0][3]:
            clear()
            time.sleep(0.2)
            print("\n[green]Access allowed!![/]\n")
            return True

        else:
            print("\n[red]Incorrect PIN, try again.[/]\n")
            attempts += 1
    clear()
    print("\n[red]Sorry you've exceeded your trial limit[/]\n")
    
    sys.exit()
    return False

# This code was taken from https://www.freecodecamp.org/news/use-the-rich-library-in-python/
# How to display a progress bar using rich
def proccess_data():
    sleep(0.02)

   


def show_balance(userData):

    """Check balance function
    """
    userData = UserData
    user = [
        holder_card
        for holder_card in list_of_users
        if UserData.get_cardNumber == holder_card[2]
    ] 
    return list_of_users[0][4]   

def show_user(userData):
    """ Show the user name when this function is called """
    userData = UserData
    user = [
        holder_card
        for holder_card in list_of_users
        if UserData.get_cardNumber == holder_card[2]
    ] 
    return list_of_users[0][0] 

def deposit(userData):
    """ 
      - Creating a function for the Deposit proccess
      - Validation of numeric
      - Updating the balance at the database 
    """
    userData = UserData
    user = [
        holder_card
        for holder_card in list_of_users
        if UserData.get_cardNumber == holder_card[2]
    ] 
    while True:
        time.sleep(0.2)
        input_deposit = input("\nHow much would you like to Deposit: € ")
        if not input_deposit:
            print("\n  [cyan]Please enter an amount to Deposit, try again.[/]\n")
        else:
            try:
                input_deposit = float(input_deposit)
                if input_deposit <= 0:
                    time.sleep(0.2)
                    print("\n[cyan]Deposit amount should be greater than 0.[/]")
                else:
                    balance = show_balance(userData)  # Get the current balance
                    if balance is not None:
                        # Convert balance to float
                        balance = float(balance)
                        new_balance = input_deposit + balance
                        current_user = user_data.find(list_of_users[0][2])
                        user_data.update_cell(current_user.row, 5, new_balance)
                        for _ in track(range(100), description='[green]Processing data'):
                            proccess_data()
                        print("\n[green]Successfully deposited [blue]€ {:.2f}[/] to your account.[/]\n".format(input_deposit))
                        return True
                    else:
                        print("\n[cyan]User not found[/]\n")
                        return False
            except ValueError:
                print("\n [cyan]Enter only numeric values for the deposit amount.[/]\n")

def withdraw(userData):
    """
      - Creating the withdraw function 
      - Validation of numeric
      - Checking if the user has sufficient data
      - Updating the balance  
     """
    userData = UserData
    user = [
        holder_card
        for holder_card in list_of_users
        if UserData.get_cardNumber == holder_card[2]
    ] 
    while True:
        time.sleep(0.2)
        input_withdraw = input("\nHow much would you like to Withdraw: € ")
        if not input_withdraw:
            print("\n [cyan]Please enter an amount to withdraw, try again.[/]\n")
        else:
            try:
                input_withdraw = float(input_withdraw)
                if input_withdraw <= 0:
                    print("\n[cyan]Withdraw amount should be greater than 0.[/]")
                else:
                    balance = show_balance(userData)  # Get the current balance
                    if balance is not None:
                        # Convert balance to float
                        balance = float(balance)
                        new_balance = balance - input_withdraw
                        current_user = user_data.find(list_of_users[0][2])
                        user_data.update_cell(current_user.row, 5, new_balance)
                        for _ in track(range(100), description='[green]Processing data'):
                            proccess_data()
                        print("\n[green]Successfully withdrawed [blue]€ {:.2f}[/] from your account.[/]\n".format(input_withdraw))
                        return True
                    else:
                        print("\n[cyan]User not found.[/]\n")
                        return False
            except ValueError:
                print("\n [cyan]Enter only numeric values for the withdraw amount.[/]\n")


def change_pin(userData):
    """
      - Creating the pin function 
      - Validation of numeric
      - Updating pin on spreadsheet  
     """
    userData = UserData
    user = [
        holder_card
        for holder_card in list_of_users
        if UserData.get_cardNumber == holder_card[2]
    ] 
    while True:
        time.sleep(0.2)
        new_pin = input("\nEnter a new 4-digit PIN: ")
        if new_pin.isdigit() and len(new_pin) == 4:
            current_user = user_data.find(list_of_users[0][2])
            user_data.update_cell(current_user.row, 4, new_pin)
            for _ in track(range(100), description='[green]Processing data'):
                proccess_data()
            print("\n[green]PIN successfully changed.[/]\n")
            break
        else:
            print("\n[red]Please enter a valid 4-digit PIN containing only digits.[/]\n")
            

def main():
    """
    A function that runs all the program functions
    """
    welcome_message()
    current_user = validate_card_and_pin(list_of_users)
    print("\nWelcome ", show_user(current_user), " :)\n")
    option = 0
    while True:
        # calling the menu function 
        display_menu()
        try:
            option = int(input("Enter here your option:  "))
            time.sleep(0.2)
            print("[green]==================================================[/]")
        except ValueError:
            time.sleep(0.2)
            print("\n    [red]Invalid input. Please try again.[/]\n")
            continue  # Restart the loop if invalid input is given
        if option == 1:
            clear()
            show_balance(current_user)
            for _ in track(range(100), description='[green]Processing data'):
                proccess_data()
            print("\n [cyan]Your current balance is: € [/]", show_balance(current_user))
            print("[green]==================================================[/]")
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
            time.sleep(0.2)
            clear()
            time.sleep(0.2)
            print("[green]==================================================[/]")
            time.sleep(0.2)
            print("[red]You exit the ATM!![/]\n")
            time.sleep(0.2)
            print("[green]Have a nice day!![/]\n")
            time.sleep(0.2)
            print("[green]==================================================[/]")
            time.sleep(0.2)
            break     
        else: 
            print("\n [red]Invalid option. Please try again.[/]\n")
        
main()  

