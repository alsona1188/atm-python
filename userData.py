class userData ():
    """
    userData class contains 5 attributes
    """
    def __init__(self, firstname, lastname, card_number, pin, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.card_number = card_number
        self.pin = pin
        self.balance = balance


def print_user_data(self):
    """ This function will print out all the details for this object """
    print("The data are:")
    print("**-------------------------------------------------**")
    print("Firstname: ", self.firstname)
    print("Lastname: ", self.lastname)
    print("Card number: ", self.card_number)
    print("Pin: ", self.pin)
    print("Balance: ", self.balance)

