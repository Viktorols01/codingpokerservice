from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from PokerState import PokerState

app = FastAPI()

# add the address here!
origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://codepoker.io"
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
    return poker_state.highestBet - poker_state.you.bet 
