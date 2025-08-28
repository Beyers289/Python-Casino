"""
Slots game logic

"""

import random
from collections import Counter

SYMBOLS = ["🍒", "🍉", "🎄", "💎", "🌹"]
WEIGHTS = [40, 25, 18, 12, 5]
THREE_PAYS = {"🍒": 5, "🍉": 12, "🎄": 25, "💎": 60, "🌹": 250}
TWO_PAYS = {"🍒": 0.10, "🍉": 0.25, "🎄": 0.50, "💎": 1.20, "🌹": 3.50}

class SlotsLogic:
    # Holds the symbols and returns 3 randoms
    def spin():
        return random.choices(SYMBOLS, weights=WEIGHTS, k=3)

    def get_display_info():
            return f"Symbols: {' '.join(SYMBOLS)}"

    # Gets the payout and uses a dictonary to assign values based on the probability of them getting selected
    def get_payout(bet_amount, symbols, user):
        counts = Counter(symbols)  # e.g. symbols = ["🍒", "🍒", "💎"] -> {'🍒': 2, '💎': 1}

        # If the length of symbols in a set(no dupes) equals 1 thats 3 of a kind
        if len(set(symbols)) == 1:
            payout = bet_amount * THREE_PAYS[symbols[0]]
            return {
                'type': 'three_of_a_kind',
                'payout': payout,
                'message': f"Congrats you won ${payout:.2f}"
            }
        elif 2 in counts.values():
            # uses the max function to go over counts {'🍒': 2, '💎': 1} and then use the key to get the value of each key in the dictonary
            two_symbols = max(counts, key=counts.get)
            payout = bet_amount * TWO_PAYS[two_symbols]

            return {
                'type': 'two_of_a_kind',
                'payout': payout,
                'message': f"Congrats you won ${payout:.2f}"
            }
        else:
            return {
                'type': 'loss',
                'payout': 0,
                'message': f"You lost ${bet_amount} LOSER"
            }

