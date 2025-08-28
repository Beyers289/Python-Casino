import sys
import os

# Get the absolute path to the parent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Now import
from game_logic.gambler import Gambler
from game_logic.slots_logic import SlotsLogic
from database import db

def choice_login():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    if db.validate_user(username, password):
        balance, name, user_id = db.get_gambler(username)
        return balance, name, user_id
    else:
        print("Invalid Credientals please try again")
        return choice_login()


def choice_create():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if db.create_user(username, password):
        balance, name, user_id = db.get_gambler(username)
        balance += deposit_method(user_id, balance)
        return balance, name, user_id
    else:
        print("Username is already taken please try and create a new account again")
        return choice_create()


def get_user_choice():
    choice = input("Please choose Login or Create: ").capitalize()
    if choice == "Login":
        return choice_login()
    elif choice == "Create":
        return choice_create()
    else:
        print("Invalid Choice please try again")
        return get_user_choice()


def deposit_method(gamblerID, gambler_balance):
    deposit = int(input("How much would you like to deposit: "))
    while deposit < 1:
        print("Minimum deposit is $1")
        deposit = int(input("How much would you like to deposit: "))
    db.update_gambler_balance(gamblerID, new_balance=(deposit + gambler_balance))
    return deposit


def display_slots_result(random_symbols):
    print("************")
    print(" | ".join(random_symbols))
    print("************")


def slots_start(gambler):
    end_string = "Y"

    while end_string == "Y":
        # Starting layout of slot
        print("*************************")
        print("Welcome Python Slots")
        print(SlotsLogic.get_display_info())
        print("*************************")
        print(f"Current Balance: ${gambler.get_balance():.2f}")

        # Getting the bet amount
        bet_amount = input("Place your bet amount: ")
        # While loop for making sure the bet amount is not greater than balance
        while not bet_amount.isdigit() or int(bet_amount) > gambler.get_balance():
            print("Bet Amount is invaild")
            bet_amount = input("Place a new bet amount: ")
        print("Spinning...\n")

        # Assigning new random symbols
        random_symbols = SlotsLogic.spin()
        display_slots_result(random_symbols)

        ## Checking to see if the symbols match and then updating the payout and getting the message
        payout = SlotsLogic.get_payout(int(bet_amount), random_symbols, gambler)
        print(payout["message"])
        if payout["type"] == "loss":
            gambler.sub_money(int(bet_amount))
        else:
            gambler.add_money(payout["payout"])
        db.update_gambler_balance(gambler.userID, gambler.get_balance())

        if gambler.get_balance() < 1:
            print("You ran out of money idiot goodbye\n")
            break

        print(f"Current Balance: ${gambler.get_balance():.2f}")
        end_string = input("Do you want to play again? (Y/N): ").upper()

        if end_string != "Y":
            break
    db.update_gambler_balance(gambler.userID, gambler.get_balance())
    return gambler


def main():
    # Program Starts here

    print("Welcome to 💎PYTHON CASINO💎")
    balance, name, user_ID = get_user_choice()
    user_gambler = Gambler(balance, name, user_ID)
    end_string = "Y"

    while end_string == "Y":
        if balance < 1:
            print("Please deposit as your balance is less than minimum bet amount")
            user_gambler.add_money(
                deposit_method(user_gambler.userID, user_gambler.balance)
            )
        print(f"Your playable balance is ${user_gambler.get_balance():.2f}\n")
        print("Please select a game from our selection 1-5\n")
        print("Option 1: Slots")
        print("Option 2: Blackjack COMING SOON")
        print("Option 3: Baccarat COMING SOON")
        print("Option 4: Coin Flip COMING SOON")
        print("Option 5: Leave Casino\n")

        user_choice = int(input("Please enter a number 1-5: "))
        if user_choice == 1:
            user_gambler = slots_start(user_gambler)
        elif user_choice == 5:
            break

        if user_gambler.get_balance() < 1:
            print(f"You have run out of money {user_gambler.get_name()}")
            end_string = input("Would you like to deposit and keep playing (Y/N): ").upper()
            if end_string == "Y":
                deposit = int(input("Please enter how much you would like to deposit: "))
                user_gambler.add_money(deposit)
            else:
                break

    print(f"\nThank you for playing at Python Casino {user_gambler.get_name()}\nPlease come again💎")


if __name__ == "__main__":
    main()
