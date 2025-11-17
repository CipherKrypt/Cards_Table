from __future__ import annotations

# The `Suite` class in Python represents a playing card suite with symbols and ranks.
class Suite():
    """
    Represents a playing card suite with its symbol and rank.

    This class provides a way to standardize card suites by assigning
    a human-readable name, Unicode symbol, and a numerical rank. The 
    rank can be used for sorting or comparison purposes.

    Attributes:
        suite (str): `string` representation of the suite. Must be one of ["spade", "heart", "diamond", "club"].
        symbol (str): `symbol` representation of the suite. A Unicode character symbol.
        rank (int): `rank` representation of the suite. Numerical rank as default is `Spade=1`, `Heart=2`, `Diamond=3`, `Club=4`.

    Methods:
        __str__(): Returns a string representation combining the symbol and suite name. Example: "♠SPADE" for a spade suite.

    Raises:
        Exception: If the input `suite` is not one of ["spade", "heart", "diamond", "club"].   
    """

    def __init__(self, suite:str):
        """
        Initializes a Suite object with its name, symbol, and rank.

        Args:
            suite (str): Name of the suite. Input is case-insensitive and must be one of ["spade", "heart", "diamond", "club"].

        Raises:
            Exception: If `suite` is not a valid suite name.
        """
        suite = suite.lower()
        if suite == "spade":
            self.suite = "spade"
            self.symbol = "\u2660"
            self.rank = 1
        elif suite == "heart":
            self.suite = "heart"
            self.symbol = "\u2665"
            self.rank = 2
        elif suite == "diamond":
            self.suite = "diamond"
            self.symbol = "\u2666"
            self.rank = 3
        elif suite == "club":
            self.suite = "club"
            self.symbol = "\u2663"
            self.rank = 4



        else:
            raise Exception('Suite input should be of type ["spade","heart","diamond","club"]')

    def __str__(self):
        """
        Returns a string representation of the suite.

        Returns:
            str: A string combining the suite's Unicode symbol and uppercase name.
                 Example: "♠SPADE" for a spade suite.
        """
        return f"{self.symbol}{self.suite.upper()}"

# The `Rank` class in Python represents a playing card rank with corresponding points, allowing for
# optional point overrides.
class Rank():
    """
    Represents a playing card rank with its rank and customizable point.

    This class provides a way to standardize card ranks by assigning the value representation and
    the point system assigned to the cards. 
    The point system can be customized to accomodate different common card games like `blackjack`,`poker` and `rummy`.
    
    Attributes:
        rank (str): `string` representation of the rank. Will be one of Must be one of ["A", "J", "Q", "K"] or string representation of number in range[2-10].
        point (int): `point` representation of the rank. Will be of type `int`.
    
    Methods:
        __str__(): Returns a string representation combining the rank and point assigned. Example: "Rank:'A' Point assigned:11" for 'Ace'

    Raises:
        Exception: If not a valid rank of ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

    """
    def __init__(self,rank:str|int,override_point:None|int = None):
        
        """
        Initializes an Rank object with a rank and a corresponding point value. Can override the default point value system.
        
        Args:
            rank (str|int): Takes `rank` as string of ["A", "J", "Q", "K"] or an integeror string between 2 and 10.
            override_point (int, optional): If `point` provided as a `int`, overrides the default point assignment or proceeds with the default point.
        Raises:
            Exception: If not a valid rank value.
        
        """

        rank_dict = {"A":"Ace","1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine","10":"Ten","J":"Jack","Q":"Queen","K":"King"}
        rank = str(rank)
        if rank in rank_dict.keys():
            self.rank = rank_dict[rank]
        else:
            raise Exception('rank should be of type ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]')

        if override_point == None:
           match rank:
                case "A":
                    self.point = 1
                case "J":
                    self.point = 11
                case "Q":
                    self.point = 12
                case "K":
                    self.point = 13
                case _:
                    self.point = int(rank)
        else:
            self.point = override_point

    def __str__(self):
        """Returns string representation of Rank 

        Returns:
            str: A string by combining the string rank and point assigned.
                 Example: "Rank:'A' Point assigned:11"
        """
        return f"Rank:'{self.rank}' Point assigned:{self.point}"
         
# The `Card` class represents a playing card with a suite and a rank.
class Card():
    """
    Initializes a Card object with suite and rank attributes for a playing card

    Attributes:
        suite (Suite): Will be of type `Suite` and one of 
        rank (Rank):

    Method:
        __str__(): Returns string representation of the card. Example: "♠A" for Ace of Spades
    """

    def __init__(self,suite:Suite,rank:Rank):
        """
        The function initializes an object with a suite and rank attribute.
        
        Args:
          suite (Suite): The `suite` parameter is used to specify the suite of a playing card, such as `Hearts`, `Diamonds`, `Clubs`, or `Spades` of type `Suite`.
          rank (Rank): The `rank` parameter is used to specify the rank of the card, such as `Ace`, `Jack`, `Queen`, `King` or `number values 2-10`. It is of type `Rank`.
        """
        self.suite = suite
        self.rank = rank

    def __str__(self):
        """Returns string representation of Card
        Returns:
            str: A string combination of Suite symbol and Rank name
        """
        return f"{self.suite.symbol}{self.rank.rank}"

        
class Deck():
    """Initializes a `Deck` object containing `Card` objects, representing a standard deck of playing cards.

    The Deck class provides methods to create, shuffle, cut, and deal cards from the deck.

    Attributes:
        deck (list): A list of `Card` objects representing the current deck of cards.
        sub_decks (list): A list to hold sub-decks if needed.
        pile (list): A list to hold dealt cards.

    Methods:
        _str_(): Returns string representation of the deck. Four rows containing 13 cards each.
        create_deck(): Creates a standard deck of 52 playing cards with customizable point allocation based on game type.
        shuffle(): Shuffles the deck of cards randomly.
        riffle_shuffle(): Performs a riffle shuffle on the deck.
        cut(): Cuts the deck at a specified or random position.
        deal(): Deals a card from the top of the deck and adds it to the pile.
    """
    Suites = {}
    for suite in ["spade","heart","diamond","club"]:
        Suites[suite] = Suite(suite)

    ranks = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

    def __init__(self):
        """
        The function initializes three empty lists for a deck, sub-decks, and a pile.
        """
        self.deck = []
        self.sub_decks = []
        self.pile = []

    def __str__(self):
        """Returns string representation of Deck

        Returns:
            str: A formatted string representation of the deck in 4 rows. Displays Card `Suite` and `Rank`.
        """
        def get_split(deck:list)-> int:
            """
            Takes a deck and calculates the split point for dividing a deck of cards into 4 even rows.
            
            Args:
                deck (list): Takes a list `deck` as input and returns an integer representing a split point in the deck. 
            Returns:
                Returns a 4 row formatted string representation of the deck of cards, with each card's suite symbol and rank displayed.
            """
            split = len(deck)//4
            return split

        if self.sub_decks:
            pass
        else:
            deck = ""
            split = get_split(self.deck)
            i = 1
            for card in self.deck:
                if i == split:
                    end = "\n"
                    i = 0
                else:
                    end = " "  
                symbol = card.suite.symbol
                rank = card.rank.rank
                deck += f"{symbol}{rank}{end}"
                i+=1

        return deck
        
    def create_deck(self,game:str = "blackjack", Suites:dict = Suites, ranks = ranks, include_joker = False)-> Deck:
        """Function to create a standard deck of playing cards with customizable point allocation based on game type.

        Creates a deck of cards by iterating through predefined suites and ranks, assigning point values based on the specified game type.

        Args:
            game (str, optional): String representation of a game to decide point allocation to cards. One of ["blackjack","poker","rummy"]. Defaults to "blackjack".
            Suites (dict, optional): User can enter a custom dictionary containing Suite objects. Defaults to dictionary Suites containing default Suite objects.
            ranks (list, optional): User can enter a custom list containing rank names. Defaults to ranks.
            include_joker (bool, optional): If True, includes Joker cards in the deck. Defaults to False.

        Returns:
            Deck: The Deck object itself, now populated with Card objects representing a standard deck of playing cards.
        """
        if include_joker:
            # TODO Add two Joker cards with unique point values and wildness properties.
            pass
        if game == "blackjack":
            for suite in Suites.keys():
                for rank in ranks:
                    if rank in ["J","Q","K"]:
                        point = 10
                    elif rank == "A":
                        point = (1,11)
                    else:
                        point = rank
                    card = Card(Suites[suite],Rank(rank,point))
                    self.deck.append(card)
        return self

    def shuffle(self)-> Deck:
        """Shuffles the deck of cards randomly and returns the Deck object itself.

        Returns:
            Deck: Returns the Deck object itself after shuffling the deck of cards.
        """
        from random import shuffle
        shuffle(self.deck)

        return self

    def riffle_shuffle(self) -> Deck:
        """Simulates a riffle shuffle on the deck of cards.

        Returns:
            Deck: Returns the Deck object itself after performing a riffle shuffle.
        """
        new_deck = []
        for i in range(26):
            new_deck.extend([self.deck[i],self.deck[i+26]])
        self.deck = new_deck

        return self

    def cut(self,cut_position:None|int = None)-> str:
        """Cuts the deck at a specified or random position.

        Args:
            cut_position (None | int, optional): User can provide a position to cut the Deck. Defaults to None and selects a position at random.

        Returns:
            str: Returns a message indicating the position at which the deck was cut.
        """
        from random import randint
        if cut_position is None:
            cut_position = randint(9,41)

            self.deck = self.deck[cut_position:]+self.deck[:cut_position]
            
            return f"Deck cut at position {cut_position}"

    def deal(self,add_to_pile = True)-> Card:
        """Simulates dealing a card from the top of the deck.

        Simulates dealing a card from the top of the deck by removing and returning the first card in the deck list. The dealt card is optionally added to a pile of dealt cards.

        Args:
            add_to_pile (bool, optional): User can choose whether the dealt card is burned or saved into a pile. Defaults to True.

        Returns:
            Card: Returns the dealt `Card` object.
        """
        card = self.deck.pop()
        if add_to_pile:
            self.pile.append(card)

        return card
                            




