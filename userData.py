class UserData():
    """
    UserData class contains 5 attributes
    """
    def __init__(self, firstname, lastname, cardNumber, pin, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.cardNumber = cardNumber
        self.pin = pin
        self.balance = balance
    
    def __str__(self):
        return f"cardHolder({self.firstname}, {self.lastname}, {self.card_number}, {self.pin}, {self.balance})"
 
    # Getter methods

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_cardNumber(self):
        return self.cardNumber

    def get_pin(self):
        return self.pin

    def get_balance(self):
        return self.balance

# Setter methods

    def set_firstname(self, newValue):
        self.firstname = newValue

    def set_lastname(self, newValue):
        self.lastname = newValue

    def set_cardNumber(self, newValue):
        self.cardNumber = newValue

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

