from generated.poker_rest import PokerState, PlayerMove, PlayerResult

# Fill the following functions with your own code!

def register_move(poker_state: PokerState, player_move: PlayerMove):
    # update beliefs about players based on moves
    pass


def register_result(poker_state: PokerState, player_result: PlayerResult):
    # update beliefs about players based on results
    pass


def get_move(poker_state: PokerState):
    # return a move based on state
    # (below is example)
    you = poker_state.players[poker_state.you_index]
    match = poker_state.highest_bet - you.bet
    return match
