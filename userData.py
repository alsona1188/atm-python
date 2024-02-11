class userData():
    """
    userData class contains 5 attributes
    """
    def __init__(self, firstname, lastname, card_number, pin, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.card_number = card_number
        self.pin = pin
        self.balance = balance


# Getter methods

def get_firstname(self):
    return self.firstname

def get_lastname(self):
    return self.lastname

def get_card_number(self):
    return self.card_number

def get_pin(self):
    return self.pin

def get_balance(self):
    return self.balance

# Setter methods

def set_firstname(self, newValue):
    self.firstname = newValue

def set_lastname(self, newValue):
    self.lastname = newValue

def set_card_number(self, newValue):
    self.card_number = newValue

def set_pin(self, newvalue):
    self.pin = newvalue

def set_balance(self, newValue):
    self.balance = newValue


def print_user_data(self):
    """ This function will print out all the details for this object """
    print("The data are:")
    print("**-------------------------------------------------**")
    print("Firstname: ", self.firstname)
    print("Lastname: ", self.lastname)
    print("Card number: ", self.card_number)
    print("Pin: ", self.pin)
    print("Balance: ", self.balance)

