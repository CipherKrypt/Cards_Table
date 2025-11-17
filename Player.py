from Deck import *

class Player():
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
        """Initialize the Player class.

        Args:
            name (str): Name of the player.
            chips (int, optional): User defined amount chips. Defaults to 100.

        Raises:
            Exception: If chips is not a positive non-zero integer.
        """
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

    def show_hand(self)-> list[Card]:
        """
        Returns a list of the player's current hand containing `Card` objects.

        Returns:
            list: Returns the player's current hand as a list of `Card` objects.
        """
        return self.hand

    def print_hand(self)-> str:
        """
        Prints a string representation of the player's hand.

        """
        print(', '.join(str(card) for card in self.hand)) if len(self.hand) > 0 else print(f"{self.name} has no cards in hand.")

    def bet(self, amount: int = 0, all_in: bool = False)-> int:
        """
        Bets a specified amount of chips. Can be used for calling or raising.

        Args:
            amount (int): The amount to bet.
        
        Raises:
            Exception: If the amount exceeds available chips.
        """
        if all_in:
            amount = self.chips
        if amount > self.chips:
            raise Exception(f"{self.name} does not have enough chips to bet {amount}.")
        self.chips -= amount
        return amount

    def fold(self)-> list[Card]:
        """
        Folds the player's hand, removing them from the current round.
        Returns:
            list: The player's current hand before folding.
        """
        hand = self.hand
        self.hand = []
        return hand