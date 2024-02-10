import gspread
from google.oauth2.service_account import Credentials
from userData import userData
from rich import print
import time
import datetime
import os

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

# user_data = SHEET.worksheet('data-user')
# users = user_data.get_all_values()
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

def deposit(userData):
    """ Get deposit as an input from the user """
    try:
        deposit = float(input("[yellow]How much money would you like to deposit?[/]"))
        userData.set_balance(userData.get_balance() + deposit)
        balance = str(userData.get_balance())
        print(f"\n [green] Thank you for your deposit. Your new balance is: {balance}[/]")
    
    except:
        print("    [red]Invalid input[/]")


def withdraw(userData):
    """ Get withdraw as an input from the user """
    try:
        withdraw = float(input ("[blue]How much money would you like to withdraw[/]"))
       #Check if user has enaugh balance
        if(userData.get_balance() < withdraw):
            print ("     [red]Sorry! There is not enough balance[/]")
            
        else:
            userData.set_balance(userData.get_balance() - withdraw)
            print("      [green]Your withdraw was completed!![/]")
    
    except:
        print("         [red]Invalid input[/]")


def check_balance():
    print ("[green]Your current balance is: ", userData.get_balance())

