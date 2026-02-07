"""Functions to help play and score a game of blackjack.

How to play blackjack: https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.
    
    :param card: str - given card.
    :return: int - value of a given card. See below for values.
    
    1. 'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2. 'A' (ace card) = 1
    3. '2' - '10' = numerical value.
    """
    face_cards: dict[str, int] = {'J': 10, 'Q': 10, 'K': 10}
    
    if card in face_cards:
        return face_cards[card]
    return 1 if card == 'A' else int(card)

print(value_of_card('K'))
print(value_of_card('4'))
print(value_of_card('A'))

def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    """Determine which card has a higher value in the hand.
    
    :param card_one: str - first card dealt in hand.
    :param card_two: str - second card dealt in hand.
    :return: str or tuple - card with higher value or tuple if equal.
    
    1. 'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2. 'A' (ace card) = 1
    3. '2' - '10' = numerical value.
    """
    value_one: int = value_of_card(card_one)
    value_two: int = value_of_card(card_two)
    
    if value_one == value_two:
        return card_one, card_two
    return card_one if value_one > value_two else card_two

print(higher_card('K', '10'))
print(higher_card('4', '6'))
print(higher_card('K', 'A'))

def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.
    
    :param card_one: str - first card dealt.
    :param card_two: str - second card dealt.
    :return: int - either 1 or 11 value of the upcoming ace card.
    
    1. 'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2. 'A' (ace card) = 11 (if already in hand)
    3. '2' - '10' = numerical value.
    """   
    ace_value: int = 11
    
    total: int = sum(
        ace_value if card == 'A' else
        10 if card in ['J', 'Q', 'K'] else
        int(card)
        for card in [card_one, card_two]
    )
    
    return 11 if total + 11 <= 21 else 1
print(value_of_ace('6', 'K'))
print(value_of_ace('7', '3'))

def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.
    
    :param card_one: str - first card dealt.
    :param card_two: str - second card dealt.
    :return: bool - is the hand a blackjack (two cards worth 21).
    
    1. 'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2. 'A' (ace card) = 11 (if already in hand)
    3. '2' - '10' = numerical value.
    """
    ace_value: int = 11
    blackjack_target: int = 21
    
    total: int = sum(
        ace_value if card == 'A' else
        10 if card in ['J', 'Q', 'K'] else
        int(card)
        for card in [card_one, card_two]
    )
    
    return total == blackjack_target
print(is_blackjack('A', 'K'))
print(is_blackjack('10', '9'))

def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.
    
    :param card_one: str - first card dealt.
    :param card_two: str - second card dealt.
    :return: bool - can the hand be split into two pairs?
    """
    return value_of_card(card_one) == value_of_card(card_two)
print(can_split_pairs('Q', 'K'))
print(can_split_pairs('10', 'A'))

def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.
    
    :param card_one: str - first card in hand.
    :param card_two: str - second card in hand.
    :return: bool - can the hand be doubled down? (totals 9, 10 or 11).
    """

    #value_one :int = value_of_card(card_one)
    #value_two :int = value_of_card(card_two)
    ace_value: int = value_of_ace(card_one,card_two)
    valid_totals: set[int] = {9, 10, 11}
    
    total: int = sum(
        ace_value if card == 'A' else
        10 if card in ['J', 'Q', 'K'] else
        int(card)
        for card in [card_one, card_two]
    )
    
    return total in valid_totals

print(can_double_down('A', '9'))
print(can_double_down('10', '2'))
