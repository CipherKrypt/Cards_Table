from Deck import Card

class Player:
    """
    Represents a player in a card game, capable of holding cards and
    performing actions like raise, call, and fold.

    Attributes:
        name (str): The name of the player.
        hand (list): A list of Card objects held by the player.
        chips (int): Amount of chips the player has for betting.

    Raises:
        Exception: If chips is not a positive non-zero integer.
        Exception: If the player tries to bet more chips than they have.
    """

    def __init__(self, name: str, chips: int = 100):
        self.name = name
        self.hand = []
        if chips > 0 :
            self.chips = chips 
        else:
            raise Exception("Chips must be a positive non-zero integer.")

    def receive_card(self, card: Card):
        """
        Receives a card and adds it to the player's hand.

        Args:
            card (Card): The card to add to the player's hand.
        """
        self.hand.append(card)

    def show_hand(self)-> list:
        """
        Returns a list of the player's current hand containing `Card` objects.
        """
        return self.hand

    def print_hand(self)-> str:
        """
        Returns a string representation of the player's hand.

        Returns:
            str: Returns a comma-separated string of cards in hand.
        """
        return ', '.join(str(card) for card in self.hand)

    def bet(self, amount: int):
        """
        Bets a specified amount of chips.

        Args:
            amount (int): The amount to bet.
        
        Raises:
            Exception: If the amount exceeds available chips.
        """
        if amount > self.chips:
            raise Exception(f"{self.name} does not have enough chips to bet {amount}.")
        self.chips -= amount
        return amount

    def call(self, previous_bet: int):
        """
        Calls the previous bet by matching the amount.

        Args:
            previous_bet (int): The amount to match.
        """
        return self.bet(previous_bet)

    def raise_bet(self, amount: int = 1, all_in: bool = False):
        """
        Raises the bet by a specified amount.

        Args:
            amount (int): The additional amount to raise.
        """
        return self.bet(self.chips if all_in else amount)

    def fold(self)-> list:
        """
        Folds the player's hand, removing them from the current round.
        Returns:
            list: The player's current hand before folding.
        """
        hand = self.hand
        self.hand = []
        return hand