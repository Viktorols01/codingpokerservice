from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from quicktype.server_to_client import PokerStateDto, PlayerMoveAndPokerStateDto, PlayerResultAndPokerStateDto

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

poker_state_dto = None

@app.post("/PLAYER_MOVE")
def register_move(dto: PlayerMoveAndPokerStateDto):
    custom_code.register_move(dto.pokerState, dto.playerMove)


@app.post("/PLAYER_RESULT")
def register_result(dto: PlayerResultAndPokerStateDto):
    custom_code.register_result(dto.pokerState, dto.playerResult)


@app.post("/REQUEST_MOVE")
def get_move(poker_state_dto: PokerStateDto):
    return custom_code.get_move(poker_state_dto)