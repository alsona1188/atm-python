import gspread
from google.oauth2.service_account import Credentials
from userData import userData
from rich import print
import time
import datetime
import os
import sys

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
users = user_data.get_all_values()
# print(users)

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
    print("\n      [green]**__[/] [bright_magenta]MENU[/] [green]__**[/]")
    time.sleep(0.2)
    print("\n      [green]1. BALANCE[/]")
    time.sleep(0.2)
    print("      [yellow]2. DEPOSIT[/]")
    time.sleep(0.2)
    print("      [blue]3. WITHDRAW[/]")
    time.sleep(0.2)
    print("      [red]4. EXIT[/]")
    time.sleep(0.2)
    print()
    print("[green]==================================================[/]")
    time.sleep(0.2)

def validate_card(userData):
    """ 
    Checking if the card number belongs to the list of card numbers that we 
    have on spreadsheet.
    """
    try:
        card_number = int(input("\n Please insert your card number:  "))
        list_of_cardNumbers = user_data.col_values(3)
        list_of_cardNumbers.pop(0)
        list_of_cardNumbers = [int(x) for x in list_of_cardNumbers]
        if card_number in list_of_cardNumbers:

            print('\n      [green]Your card number is correct!!![/]')

            return str(card_number)

    except ValueError:
        print('   [cyan]Please enter numbers for your account number![/]')
    print("       [red]Your account number doesn't exist![/]")
    return False

def validate_pin(userData, card_number):
    """" 
    Verifying if the pin entered by the user is 
    corresponding to our spreadsheet and also 
    to the card number that the user entered
    """
    card_number_row = user_data.find(card_number).row
    card_number_col = user_data.find(card_number).col
    user_pin = user_data.cell(card_number_row, card_number_col+1).value
    
    attempts_left = 3
    while attempts_left > 0:
        inserted_pin = int(input("\n Please insert your PIN:  "))

        if user_pin == inserted_pin:
            print("Your PIN is correct!")
            return True
        else:
            attempts_left -= 1
            print(f"Incorrect PIN! {attempts_left} attempts left.")
            if attempts_left == 0:
                print("Your account has been blocked! Please contact us.")
                return False

    
    
def main():

    welcome_message()
    display_menu()
    validate_card(userData)
   
    

if __name__ == '__main__':
    main()