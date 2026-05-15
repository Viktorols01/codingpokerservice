from quicktype.server_to_client import PokerStateDto, RequestMoveDto, PlayerMoveDto, PlayerResultDto

# Fill the following functions with your own code!

def register_move(poker_state_dto: PokerStateDto, player_move_dto: PlayerMoveDto):
    # update beliefs about players based on moves
    pass


def register_result(poker_state_dto: PokerStateDto, player_result_dto: PlayerResultDto):
    # update beliefs about players based on results
    pass


def get_move(poker_state: Poker):
    # return a move based on state
    # (below is example)
    you = poker_state.players[poker_state.youIndex]
    match = poker_state.highestBet - you.bet
    return match