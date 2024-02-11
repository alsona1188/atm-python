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

#user_data = SHEET.worksheet('data-user')

# Prints a list of users by row
#list_of_users = user_data.get_all_values()[1:]
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


def validate_card():
    """
    Validating the card inserted by the user. If it is correct will break
    otherwise it will continue to ask for card number.
    """
    list_of_users = SHEET.worksheet("data-user").get_all_values()[1:]
    while True:
        inserted_card = input("\n Please insert your CARD:  ")
        if not inserted_card:
            print("\n Please insert your card number.")
            continue
            
        user = [holder_card for holder_card in list_of_users if 
                inserted_card == holder_card[2]]
        if user:
            time.sleep(0.3)
            print("\n [green] Your card is correct[/]\n")
            break
        else:
            print("\n [red] Your card number doesn't exist![/]")

def validate_pin(userData):
    



def main():
    welcome_message()
    display_menu()
    validate_card()
    

main()