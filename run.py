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
        cardNumber = int(input("\n Please insert your card number:  "))
        list_of_cardNumbers = user_data.col_values(3)
        list_of_cardNumbers.pop(0)
        list_of_cardNumbers = [int(x) for x in list_of_cardNumbers]
        if cardNumber in list_of_cardNumbers:
            print('\n      [green]Your card number is correct!!![/]')
            return str(cardNumber)
    except ValueError:
        print('   [cyan]Please enter numbers for your account number![/]')
    print("       [red]Your account number doesn't exist![/]")
    return False

def validate_pin(userData, cardNumber):
    """" 
    Verifying if the pin entered by the user is 
    corresponding to our spreadsheet and also 
    to the card number that the user entered
    """
    cardNumber_row = user_data.find(cardNumber).row
    cardNumber_col = user_data.find(cardNumber).col
    user_pin = user_data.cell(cardNumber_row, cardNumber_col+1).value
    inserted_pin = int(input("\n Please insert your Pin:  "))
    
              
def main():

    welcome_message()
    display_menu()
    validate_card(userData)
    
if __name__ == '__main__':
    main()
 