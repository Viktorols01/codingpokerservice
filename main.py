from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from quicktype.server_to_client import PokerStateDto, RequestMoveDto, PlayerMoveDto, PlayerResultDto

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
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

poker_state = None

@app.post("/POKER_STATE")
def register_poker_state(new_poker_state: PokerStateDto):
    global poker_state
    poker_state = new_poker_state

@app.post("/PLAYER_MOVE")
def register_move(player_move_dto: PlayerMoveDto):
    pass

@app.post("/PLAYER_RESULT")
def register_result(player_result_dto: PlayerResultDto):
    pass

@app.get("/REQUEST_MOVE")
def get_move():
    global poker_state
    # implement your own solution
    you = poker_state.players[poker_state.youIndex]
    match = poker_state.highestBet - you.bet 
    return match