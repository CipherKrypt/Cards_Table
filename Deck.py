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

        




