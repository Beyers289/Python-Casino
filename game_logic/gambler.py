class Gambler:
    #Creating the Gambler giving them the name and Balance
    def __init__(self, balance, name, userID):
        self.balance = balance
        self.name = name
        self.userID = userID
    
    #Adding money onto the gamblers balance
    def add_money(self, payment):
        self.balance += payment
    
    #Subtracting money from the gamblers balance
    def sub_money(self, payment):
        self.balance -= payment
    
    #If a whole change is needed to the balance ex. if balance is 100 but due to error it should be 50 or 200 you use this method to completely change the balance
    def change_balance(self, balance):
        self.balance = balance
    
    #Returns the gamblers balance
    def get_balance(self):
        return self.balance
    
    #Returns the gamblers name 
    def get_name(self):
        return self.name