from game_logic.gambler import Gambler


gambler2 = Gambler(200.676767676, 'Nate', 1)
gambler2.sub_money(50)
print(gambler2.get_balance())