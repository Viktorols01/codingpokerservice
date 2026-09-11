from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from generated.poker_rest import PokerState, PlayerMoveAndPokerState, PlayerResultAndPokerState

import custom_code

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

poker_state = None

@app.post("/PLAYER_MOVE")
def register_move(payload: PlayerMoveAndPokerState):
    custom_code.register_move(payload.poker_state, payload.player_move)


@app.post("/PLAYER_RESULT")
def register_result(payload: PlayerResultAndPokerState):
    custom_code.register_result(payload.poker_state, payload.player_result)


@app.post("/REQUEST_MOVE")
def get_move(poker_state: PokerState):
    return custom_code.get_move(poker_state)