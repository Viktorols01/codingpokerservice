from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from PokerState import PokerState

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "https://codingpoker.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/")
def read_root(poker_state: PokerState):
    # implement your own solution
    you = poker_state.players[poker_state.youIndex]
    match = poker_state.highestBet - you.bet 
    return match
