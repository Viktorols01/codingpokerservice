from pydantic import BaseModel
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class CreatedLobbyDto(BaseModel):
    isCreated: bool
    lobbyId: str

    @staticmethod
    def from_dict(obj: Any) -> 'CreatedLobbyDto':
        assert isinstance(obj, dict)
        isCreated = from_bool(obj.get("isCreated"))
        lobbyId = from_str(obj.get("lobbyId"))
        return CreatedLobbyDto(isCreated, lobbyId)

    def to_dict(self) -> dict:
        result: dict = {}
        result["isCreated"] = from_bool(self.isCreated)
        result["lobbyId"] = from_str(self.lobbyId)
        return result


class LobbyConfigurationDto(BaseModel):
    anyoneCanContinue: bool
    enableStatistics: bool
    isPrivate: bool
    allowMoves: bool
    rabbitHunting: bool
    moveTimeout: int
    afterMoveTimeout: int
    afterGameTimeout: int
    bigBlind: int
    smallBlind: int
    startMarkers: int

    @staticmethod
    def from_dict(obj: Any) -> 'LobbyConfigurationDto':
        assert isinstance(obj, dict)
        anyoneCanContinue = from_bool(obj.get("anyoneCanContinue"))
        enableStatistics = from_bool(obj.get("enableStatistics"))
        isPrivate = from_bool(obj.get("isPrivate"))
        allowMoves = from_bool(obj.get("allowMoves"))
        rabbitHunting = from_bool(obj.get("rabbitHunting"))
        moveTimeout = from_int(obj.get("moveTimeout"))
        afterMoveTimeout = from_int(obj.get("afterMoveTimeout"))
        afterGameTimeout = from_int(obj.get("afterGameTimeout"))
        bigBlind = from_int(obj.get("bigBlind"))
        smallBlind = from_int(obj.get("smallBlind"))
        startMarkers = from_int(obj.get("startMarkers"))
        return LobbyConfigurationDto(anyoneCanContinue, enableStatistics, isPrivate, allowMoves, rabbitHunting, moveTimeout, afterMoveTimeout, afterGameTimeout, bigBlind, smallBlind, startMarkers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["anyoneCanContinue"] = from_bool(self.anyoneCanContinue)
        result["enableStatistics"] = from_bool(self.enableStatistics)
        result["isPrivate"] = from_bool(self.isPrivate)
        result["allowMoves"] = from_bool(self.allowMoves)
        result["rabbitHunting"] = from_bool(self.rabbitHunting)
        result["moveTimeout"] = from_int(self.moveTimeout)
        result["afterMoveTimeout"] = from_int(self.afterMoveTimeout)
        result["afterGameTimeout"] = from_int(self.afterGameTimeout)
        result["bigBlind"] = from_int(self.bigBlind)
        result["smallBlind"] = from_int(self.smallBlind)
        result["startMarkers"] = from_int(self.startMarkers)
        return result


class LobbyContainerStatusDto(BaseModel):
    lobbyContainerId: str
    lobbyCount: int
    channelCount: int

    @staticmethod
    def from_dict(obj: Any) -> 'LobbyContainerStatusDto':
        assert isinstance(obj, dict)
        lobbyContainerId = from_str(obj.get("lobbyContainerId"))
        lobbyCount = from_int(obj.get("lobbyCount"))
        channelCount = from_int(obj.get("channelCount"))
        return LobbyContainerStatusDto(lobbyContainerId, lobbyCount, channelCount)

    def to_dict(self) -> dict:
        result: dict = {}
        result["lobbyContainerId"] = from_str(self.lobbyContainerId)
        result["lobbyCount"] = from_int(self.lobbyCount)
        result["channelCount"] = from_int(self.channelCount)
        return result


class LobbySearchResultDto(BaseModel):
    found: bool
    lobbyId: str

    @staticmethod
    def from_dict(obj: Any) -> 'LobbySearchResultDto':
        assert isinstance(obj, dict)
        found = from_bool(obj.get("found"))
        lobbyId = from_str(obj.get("lobbyId"))
        return LobbySearchResultDto(found, lobbyId)

    def to_dict(self) -> dict:
        result: dict = {}
        result["found"] = from_bool(self.found)
        result["lobbyId"] = from_str(self.lobbyId)
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


def CreatedLobbyDtofromdict(s: Any) -> CreatedLobbyDto:
    return CreatedLobbyDto.from_dict(s)


def CreatedLobbyDtotodict(x: CreatedLobbyDto) -> Any:
    return to_class(CreatedLobbyDto, x)


def LobbyConfigurationDtofromdict(s: Any) -> LobbyConfigurationDto:
    return LobbyConfigurationDto.from_dict(s)


def LobbyConfigurationDtotodict(x: LobbyConfigurationDto) -> Any:
    return to_class(LobbyConfigurationDto, x)


def LobbyContainerStatusDtofromdict(s: Any) -> LobbyContainerStatusDto:
    return LobbyContainerStatusDto.from_dict(s)


def LobbyContainerStatusDtotodict(x: LobbyContainerStatusDto) -> Any:
    return to_class(LobbyContainerStatusDto, x)


def LobbySearchResultDtofromdict(s: Any) -> LobbySearchResultDto:
    return LobbySearchResultDto.from_dict(s)


def LobbySearchResultDtotodict(x: LobbySearchResultDto) -> Any:
    return to_class(LobbySearchResultDto, x)


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
