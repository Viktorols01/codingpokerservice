from enum import Enum
from typing import List
from pydantic import BaseModel

class PokerStateSuit(int, Enum):
    HEARTS = 0
    DIAMONDS = 1
    CLUBS = 2
    SPADES = 3

class PokerStateCard(BaseModel):
    suit: PokerStateSuit
    rank: int

class PokerStatePlayer(BaseModel):
    name: str
    markers: int
    bet: int
    cards: List[PokerStateCard]
    folded: bool

class PokerState(BaseModel):
    highestBet: int
    players: List[PokerStatePlayer]
    dealerIndex: int
    youIndex: int
    communityCards: List[PokerStateCard]
    bigBlind: int
    smallBlind: int
