from pydantic import BaseModel
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Client(BaseModel):
    name: str
    skinId: str
    isHost: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Client':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        skinId = from_str(obj.get("skinId"))
        isHost = from_bool(obj.get("isHost"))
        return Client(name, skinId, isHost)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["skinId"] = from_str(self.skinId)
        result["isHost"] = from_bool(self.isHost)
        return result


class LobbyStateDto(BaseModel):
    clients: List[Client]
    youIndex: int

    @staticmethod
    def from_dict(obj: Any) -> 'LobbyStateDto':
        assert isinstance(obj, dict)
        clients = from_list(Client.from_dict, obj.get("clients"))
        youIndex = from_int(obj.get("youIndex"))
        return LobbyStateDto(clients, youIndex)

    def to_dict(self) -> dict:
        result: dict = {}
        result["clients"] = from_list(lambda x: to_class(Client, x), self.clients)
        result["youIndex"] = from_int(self.youIndex)
        return result


class MessageDto(BaseModel):
    message: str
    category: str

    @staticmethod
    def from_dict(obj: Any) -> 'MessageDto':
        assert isinstance(obj, dict)
        message = from_str(obj.get("message"))
        category = from_str(obj.get("category"))
        return MessageDto(message, category)

    def to_dict(self) -> dict:
        result: dict = {}
        result["message"] = from_str(self.message)
        result["category"] = from_str(self.category)
        return result


class RequestMoveDto(BaseModel):
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'RequestMoveDto':
        assert isinstance(obj, dict)
        return RequestMoveDto()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class PlayerContinueDto(BaseModel):
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'PlayerContinueDto':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        return PlayerContinueDto(name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        return result


class PlayerMoveDto(BaseModel):
    name: str
    action: str
    requiredBet: int
    bet: int

    @staticmethod
    def from_dict(obj: Any) -> 'PlayerMoveDto':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        action = from_str(obj.get("action"))
        requiredBet = from_int(obj.get("requiredBet"))
        bet = from_int(obj.get("bet"))
        return PlayerMoveDto(name, action, requiredBet, bet)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["action"] = from_str(self.action)
        result["requiredBet"] = from_int(self.requiredBet)
        result["bet"] = from_int(self.bet)
        return result


class Player(BaseModel):
    name: str
    markers: int
    bet: int
    cards: List[str]
    folded: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Player':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        markers = from_int(obj.get("markers"))
        bet = from_int(obj.get("bet"))
        cards = from_list(from_str, obj.get("cards"))
        folded = from_bool(obj.get("folded"))
        return Player(name, markers, bet, cards, folded)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["markers"] = from_int(self.markers)
        result["bet"] = from_int(self.bet)
        result["cards"] = from_list(from_str, self.cards)
        result["folded"] = from_bool(self.folded)
        return result


class PokerStateDto(BaseModel):
    highestBet: int
    players: List[Player]
    dealerIndex: int
    youIndex: int
    communityCards: List[str]
    bigBlind: int
    smallBlind: int

    @staticmethod
    def from_dict(obj: Any) -> 'PokerStateDto':
        assert isinstance(obj, dict)
        highestBet = from_int(obj.get("highestBet"))
        players = from_list(Player.from_dict, obj.get("players"))
        dealerIndex = from_int(obj.get("dealerIndex"))
        youIndex = from_int(obj.get("youIndex"))
        communityCards = from_list(from_str, obj.get("communityCards"))
        bigBlind = from_int(obj.get("bigBlind"))
        smallBlind = from_int(obj.get("smallBlind"))
        return PokerStateDto(highestBet, players, dealerIndex, youIndex, communityCards, bigBlind, smallBlind)

    def to_dict(self) -> dict:
        result: dict = {}
        result["highestBet"] = from_int(self.highestBet)
        result["players"] = from_list(lambda x: to_class(Player, x), self.players)
        result["dealerIndex"] = from_int(self.dealerIndex)
        result["youIndex"] = from_int(self.youIndex)
        result["communityCards"] = from_list(from_str, self.communityCards)
        result["bigBlind"] = from_int(self.bigBlind)
        result["smallBlind"] = from_int(self.smallBlind)
        return result


class PlayerMoveAndPokerStateDto(BaseModel):
    playerMove: PlayerMoveDto
    pokerState: PokerStateDto

    @staticmethod
    def from_dict(obj: Any) -> 'PlayerMoveAndPokerStateDto':
        assert isinstance(obj, dict)
        playerMove = PlayerMoveDto.from_dict(obj.get("playerMove"))
        pokerState = PokerStateDto.from_dict(obj.get("pokerState"))
        return PlayerMoveAndPokerStateDto(playerMove, pokerState)

    def to_dict(self) -> dict:
        result: dict = {}
        result["playerMove"] = to_class(PlayerMoveDto, self.playerMove)
        result["pokerState"] = to_class(PokerStateDto, self.pokerState)
        return result


class PlayerResultDto(BaseModel):
    name: str
    handDescription: str
    cards: List[str]
    markers: int

    @staticmethod
    def from_dict(obj: Any) -> 'PlayerResultDto':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        handDescription = from_str(obj.get("handDescription"))
        cards = from_list(from_str, obj.get("cards"))
        markers = from_int(obj.get("markers"))
        return PlayerResultDto(name, handDescription, cards, markers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["handDescription"] = from_str(self.handDescription)
        result["cards"] = from_list(from_str, self.cards)
        result["markers"] = from_int(self.markers)
        return result


class PlayerResultAndPokerStateDto(BaseModel):
    playerResult: PlayerResultDto
    pokerState: PokerStateDto

    @staticmethod
    def from_dict(obj: Any) -> 'PlayerResultAndPokerStateDto':
        assert isinstance(obj, dict)
        playerResult = PlayerResultDto.from_dict(obj.get("playerResult"))
        pokerState = PokerStateDto.from_dict(obj.get("pokerState"))
        return PlayerResultAndPokerStateDto(playerResult, pokerState)

    def to_dict(self) -> dict:
        result: dict = {}
        result["playerResult"] = to_class(PlayerResultDto, self.playerResult)
        result["pokerState"] = to_class(PokerStateDto, self.pokerState)
        return result


class PokerStatisticsDto(BaseModel):
    raiseSum: int
    raiseCount: int
    foldCount: int
    allInCount: int
    checkCount: int
    matchCount: int
    winCount: int
    bestHandCount: int
    lossCount: int
    handCount: int

    @staticmethod
    def from_dict(obj: Any) -> 'PokerStatisticsDto':
        assert isinstance(obj, dict)
        raiseSum = from_int(obj.get("raiseSum"))
        raiseCount = from_int(obj.get("raiseCount"))
        foldCount = from_int(obj.get("foldCount"))
        allInCount = from_int(obj.get("allInCount"))
        checkCount = from_int(obj.get("checkCount"))
        matchCount = from_int(obj.get("matchCount"))
        winCount = from_int(obj.get("winCount"))
        bestHandCount = from_int(obj.get("bestHandCount"))
        lossCount = from_int(obj.get("lossCount"))
        handCount = from_int(obj.get("handCount"))
        return PokerStatisticsDto(raiseSum, raiseCount, foldCount, allInCount, checkCount, matchCount, winCount, bestHandCount, lossCount, handCount)

    def to_dict(self) -> dict:
        result: dict = {}
        result["raiseSum"] = from_int(self.raiseSum)
        result["raiseCount"] = from_int(self.raiseCount)
        result["foldCount"] = from_int(self.foldCount)
        result["allInCount"] = from_int(self.allInCount)
        result["checkCount"] = from_int(self.checkCount)
        result["matchCount"] = from_int(self.matchCount)
        result["winCount"] = from_int(self.winCount)
        result["bestHandCount"] = from_int(self.bestHandCount)
        result["lossCount"] = from_int(self.lossCount)
        result["handCount"] = from_int(self.handCount)
        return result


class RequiredInputDto(BaseModel):
    description: str
    name: str
    remainingTime: int
    isMoveRequest: bool
    isContinueRequest: bool

    @staticmethod
    def from_dict(obj: Any) -> 'RequiredInputDto':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        name = from_str(obj.get("name"))
        remainingTime = from_int(obj.get("remainingTime"))
        isMoveRequest = from_bool(obj.get("isMoveRequest"))
        isContinueRequest = from_bool(obj.get("isContinueRequest"))
        return RequiredInputDto(description, name, remainingTime, isMoveRequest, isContinueRequest)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["name"] = from_str(self.name)
        result["remainingTime"] = from_int(self.remainingTime)
        result["isMoveRequest"] = from_bool(self.isMoveRequest)
        result["isContinueRequest"] = from_bool(self.isContinueRequest)
        return result


class SessionIDDto(BaseModel):
    sessionId: str

    @staticmethod
    def from_dict(obj: Any) -> 'SessionIDDto':
        assert isinstance(obj, dict)
        sessionId = from_str(obj.get("sessionId"))
        return SessionIDDto(sessionId)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sessionId"] = from_str(self.sessionId)
        return result


def LobbyStateDtofromdict(s: Any) -> LobbyStateDto:
    return LobbyStateDto.from_dict(s)


def LobbyStateDtotodict(x: LobbyStateDto) -> Any:
    return to_class(LobbyStateDto, x)


def MessageDtofromdict(s: Any) -> MessageDto:
    return MessageDto.from_dict(s)


def MessageDtotodict(x: MessageDto) -> Any:
    return to_class(MessageDto, x)


def NoSuchSessionIDDtofromdict(s: Any) -> RequestMoveDto:
    return RequestMoveDto.from_dict(s)


def NoSuchSessionIDDtotodict(x: RequestMoveDto) -> Any:
    return to_class(RequestMoveDto, x)


def PlayerContinueDtofromdict(s: Any) -> PlayerContinueDto:
    return PlayerContinueDto.from_dict(s)


def PlayerContinueDtotodict(x: PlayerContinueDto) -> Any:
    return to_class(PlayerContinueDto, x)


def PlayerMoveAndPokerStateDtofromdict(s: Any) -> PlayerMoveAndPokerStateDto:
    return PlayerMoveAndPokerStateDto.from_dict(s)


def PlayerMoveAndPokerStateDtotodict(x: PlayerMoveAndPokerStateDto) -> Any:
    return to_class(PlayerMoveAndPokerStateDto, x)


def PlayerMoveDtofromdict(s: Any) -> PlayerMoveDto:
    return PlayerMoveDto.from_dict(s)


def PlayerMoveDtotodict(x: PlayerMoveDto) -> Any:
    return to_class(PlayerMoveDto, x)


def PlayerResultAndPokerStateDtofromdict(s: Any) -> PlayerResultAndPokerStateDto:
    return PlayerResultAndPokerStateDto.from_dict(s)


def PlayerResultAndPokerStateDtotodict(x: PlayerResultAndPokerStateDto) -> Any:
    return to_class(PlayerResultAndPokerStateDto, x)


def PlayerResultDtofromdict(s: Any) -> PlayerResultDto:
    return PlayerResultDto.from_dict(s)


def PlayerResultDtotodict(x: PlayerResultDto) -> Any:
    return to_class(PlayerResultDto, x)


def PokerStateDtofromdict(s: Any) -> PokerStateDto:
    return PokerStateDto.from_dict(s)


def PokerStateDtotodict(x: PokerStateDto) -> Any:
    return to_class(PokerStateDto, x)


def PokerStatisticsDtofromdict(s: Any) -> PokerStatisticsDto:
    return PokerStatisticsDto.from_dict(s)


def PokerStatisticsDtotodict(x: PokerStatisticsDto) -> Any:
    return to_class(PokerStatisticsDto, x)


def RequestMoveDtofromdict(s: Any) -> RequestMoveDto:
    return RequestMoveDto.from_dict(s)


def RequestMoveDtotodict(x: RequestMoveDto) -> Any:
    return to_class(RequestMoveDto, x)


def RequiredInputDtofromdict(s: Any) -> RequiredInputDto:
    return RequiredInputDto.from_dict(s)


def RequiredInputDtotodict(x: RequiredInputDto) -> Any:
    return to_class(RequiredInputDto, x)


def SessionIDDtofromdict(s: Any) -> SessionIDDto:
    return SessionIDDto.from_dict(s)


def SessionIDDtotodict(x: SessionIDDto) -> Any:
    return to_class(SessionIDDto, x)
