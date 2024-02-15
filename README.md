# **ATM Commerz Bank**

## Project Overview

ATM-python is a convenient banking application provided by Commerz bank, enabling clients with debit, credit, or ec cards to access various banking functionalities. This user-friendly app mirrors the traditional ATM experience, offering a range of options including balance inquiry, deposits, withdrawals, PIN changes, PIN display, and exit. Its intuitive design ensures seamless navigation and ease of use for all users.

![screenshot of amiresponsive](document/amiresponsive.png)

You can acess the application [ATM Commerz bank](https://atm-python-58b3ab8a62e4.herokuapp.com/)

### My GitHub Repository

You can visit the GitHub Repository [here](https://github.com/alsona1188/atm-python)

## CONTENTS

- [**ATM Commerz Bank**](#atm-python)
  - [CONTENTS](#contents)
  - [User Experience](#user-experience)
  - [Flowchart](#flowchart)  
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
  - [Data Model](#data-model)  
  - [Testing](#testing)
  - [Bugs](#bugs)
    - [Resolved Bugs](#resolved-bugs)
    - [Remaining Bugs](#remaining-bugs)
  - [Technologies Used](#technologies-used)
  - [Imported Libraries and Packages Used](#imported-libraries-and-packages-used) 
  - [Heroku Deployment](#heroku-deployment)
  - [Clone the Repository Code Locally](#clone-the-repository-code-locally)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

  ## User experience
__Target Audience__

  - Commerz Bank Customers: Individual card holders.

  The target users of an ATM commerz Bank project are all the clients who rely on ATMs for their daily banking needs, whether it be for routine transactions,like deposit or withdraws, checking their balance or changin the pin.The project aims to serve these users efficiently and securely, enhancing their overall banking experience.

__User Stories__

As a customer approaching an Automated Teller Machine (ATM), the experience is designed to be user-centric, efficient, and secure. 

The user experience at the ATM is designed to be efficient, secure, and hassle-free.The ATM is user-friendly interface and thoughtful design aim to provide you with a seamless and satisfying banking experience.

## Flowchart
A well-designed flowchart for an ATM software project helps developers, testers, and stakeholders understand the system's functionality, interactions, and decision points, ensuring the smooth operation of the ATM and a positive user experience. The flowchart is given below.

![Flowchart](document/atm_flowchart.png)

## Features

### Existing Features

### Welcome Screen
- In this ATM machine software project, there is a welcome screen that greets the customer and provides the time and the dat. The welcome screen typically displays a welcoming message and offers the option to insert the card number.

![Welcome Screen/Page](document/welcome_screen.png)

### Validation of Card number and PIN
- If the user enters a wrong card number, than an error message will come informing that the card number is not correct.

![Wrong card number](document/card_number_wrong.png)

- If the user enters a wrong pin, than an error message will come, same as with the card number

![Wrong PIN](document/wrong_pin.png)

- If the user enter 3 times wrong card or pin number than the system will log out and the user will be exiting the atm. 

![Exceeded limit](document/exceeded_limit.png)

- If the user enters the correct card number and PIN than a menu will display wit all the functionalities that the ATM is offering. A welcoming message will apear with the name of the customer. 

![Menu](document/menu.png)

### Option 1: Balance
 - If the user choose the option 1, than he will be able to see his current balance displayed on the screen.

 - Menu will be displayed after that.

![Balance](document/balance.png) 

### Option 2: Deposit

- if the user is choosing the option 2, deposit, the screen will be cleared and the customer will be asked how much money the user likes to deposit.

 - Here there there are some errors that will display to the user. 
  1. The user must enter a value
  2. The amount should be greater than 0
  3. The value should be numeric. 

![Error deposit](document/error_deposit.png)

- if the user enters a valid amount for deposit, Than it will show the progress bar and also the message that the deposit was successfully updated. When we enter a deposit value than automatically the balance will be updated. 

![Deposit successfully](document/valid_amount_deposit.png)

## Option 3: Withdraw

- if the user is choosing the option 3, withdraw, the screen will be cleared and the customer will be asked how much money the user likes to withdraw.

 - Here there there are some errors that will display to the user. 
  1. The user must enter a value
  2. The amount should be greater than 0
  3. The value should be numeric. 
  4. The amount should be less or equal to the balance

![Errors withdraw](document/errors_withdraw.png)

- if the user enters a valid amount for withdraw, Than it will show the progress bar and also the message that the withdraw was successfully updated. When we enter a withdraw value than automatically the balance will be updated. 

![Deposit successfully](document/valid_amount_withdraw.png)

## Option 4: Change PIN

- If the want to change the PIN number that he has to enter number 4. There is one condition that the pin should be 4 digit, else error will appear on the screen. 

![Not valid Pin](document/4-digit_pin.png)

- When the user enters a valid PIN thank a message will appear that the pin was successfully changed.

![Valid Pin](document/valid_new_pin.png)

## Option 5: Show PIN

- When the user enters number 4, than automatically on the screen will appear the current PIN. 

![Show Pin](document/show_pin.png)

## Option 6: Exit

- When the user wants to exit the ATM he can just enter option 6. 

![Exit](document/exit.png)

### Future Features

- A future feature for this app, is to keep track and save all the deposit and Withdraw of the customer.
- Creating more sheets on the spreadsheet, like withdraw and deposit. 
- Developing the APP not only as an ATM but can go further to Online Banking.

## Data Model

1.Google Sheets:

Google Sheets is used as a data storage and management tool. It allows for organized data storage and retrieval of the user details, like firstname, lastname, Card Number, Pin and Balance.

Here is the link of the spreadsheet:
[atm-python](https://docs.google.com/spreadsheets/d/1LVCX2QFLkQlBhcHl-c_47eY1clq3Ybq8vf8vXKG5wV8/edit?usp=sharing)

## Testing

 - Python Validation

I validated my file using [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) and was met with no errors. There are only notification about the long code more than 79 charachters. 

The Result is given below.

![Python Linter Test Result](document/python_linter.png)

- I have manually tested the project by giving invalid inputs, such as strings when numbers are expected, or giving input withdraw greater than the balance. Pin was tested as well, when you enter a new pin, should be 4 digit. 
- Tested in my local terminal and on my personal heroku terminal. 

## Bugs

- Solved Bugs
  
  1. When I wrote the project I noticed that i did not add the condition that the withdraw amount should be less than the balance amount. Fixed it by adding the right code.

  2. Another problem that I faced during writing of the code was that I was not able to update the balance after doing a withdraw or deposit. I fixed that by adding the user_data and the list_of_users inside the show_balance function.

  3. I had also a bug where i had to convert the input_deposit and input_withdraw to float. 

  4. When I was deploying the App I had also problems with the libraries. I found out that i had to update the rich library to the last version. 

  5. During deployment a secon error happened with the sleep used on the progress bar,I fixed that by changing sleep(0.02) to time.sleep(0.02)

- Unsolved Bugs: I can mention only the code longer than 79 characters appearing at the CI python linter.

## Technologies Used

The following is a list of the technologies I used on this project.

1. Python: is the primary programming language used to develop the ATM software. It is a versatile language known for its simplicity and readability.

2. Google Cloud: provides the necessary APIs for various functions within the project.

3. GitHub

4. Gitpod and CodeAnywhere: Integrated development environment (IDE) for coding and managing the project. It offers a range of developer tools and extensions to aid in code writing and debugging.

5. Flowchart was made using Lucidchart website. 

Each of these technologies plays a specific role in the project's development and execution, contributing to the successful operation of the ATM software system.


## Imported Libraries and Packages Used

- [rich](https://pypi.org/project/rich/#description) The Rich API makes it easy to add color and style to terminal output.
- [os](https://docs.python.org/3/library/os.html)  library is utilized to implement a clear_screen function. This function enhances the user experience by clearing the terminal screen, reducing clutter, and making interactions more straightforward.
- [sys](https://docs.python.org/3/library/sys.html) is used to control the output behavior of the program. Specifically, it is used to print text letter by letter, creating a typewriter-like effect that can enhance user engagement.
- [gspread](https://docs.gspread.org/en/v5.7.0/) facilitates the connection between the program and Google Sheets. It enables reading and updating data on a Google Sheets document, making it an effective tool for managing and syncing data.
- [datetime](https://docs.python.org/3/library/datetime.html#module-datetime) The datetime module supplies classes for manipulating dates and times.
- [time](https://docs.python.org/3/library/time.h) This module provides various time-related functions


## Heroku Deployment

Deployment steps are as follows, after account setup:

- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Also we have to add the credentials file to *Reveal Config Vars* and set the key to CREDS and the value to the credentials file. 
- Further down, to support dependencies, select *Add Buildpack*.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)
- Link the `Heroku app` to `Repository` 
- Click on `Deploy`. 

## Clone the Repository Code Locally
- Navigate to the GitHub Repository you want to clone to use locally:
  - Click on the code drop down button
  - Click on HTTPS
  - Copy the repository link to the clipboard
  - Open your IDE of choice
  - Type git clone copied-git-url into the IDE terminal
  - The project will now be cloned on your local machine for use.

## Credits 

Here we credit everywhere we have got content for the website and any code that was taken from other sources.

### Code 

- The code for clearing the terminal was got from [stack overflow](https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python)
- The code for progress bar effect was got from [freeCodeCamp](https://www.freecodecamp.org/news/use-the-rich-library-in-python/)
- The code for connecting to google sheets was got from [Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/071036790a5642f9a6f004f9888b6a45/)
- [Youtube tutorial](https://www.youtube.com/watch?v=PkfhcduvAOE)
- Code Institute for the deployment material. 
- [Gspread: Automate Google sheet with Python](https://medium.com/hacktive-devs/gspread-automate-google-sheet-with-python-dc1fa7c65c21)














































     
   
