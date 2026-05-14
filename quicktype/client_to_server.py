from pydantic import BaseModel
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class JoinLobbyDto(BaseModel):
    name: str
    skinId: str

    @staticmethod
    def from_dict(obj: Any) -> 'JoinLobbyDto':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        skinId = from_str(obj.get("skinId"))
        return JoinLobbyDto(name, skinId)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["skinId"] = from_str(self.skinId)
        return result


class RejoinLobbyDto(BaseModel):
    sessionId: str

    @staticmethod
    def from_dict(obj: Any) -> 'RejoinLobbyDto':
        assert isinstance(obj, dict)
        sessionId = from_str(obj.get("sessionId"))
        return RejoinLobbyDto(sessionId)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sessionId"] = from_str(self.sessionId)
        return result


class RequestShutdownDto(BaseModel):
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'RequestShutdownDto':
        assert isinstance(obj, dict)
        return RequestShutdownDto()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class SendMoveDto(BaseModel):
    move: int

    @staticmethod
    def from_dict(obj: Any) -> 'SendMoveDto':
        assert isinstance(obj, dict)
        move = from_int(obj.get("move"))
        return SendMoveDto(move)

    def to_dict(self) -> dict:
        result: dict = {}
        result["move"] = from_int(self.move)
        return result


class ShowCardsDto(BaseModel):
    showCards: bool

    @staticmethod
    def from_dict(obj: Any) -> 'ShowCardsDto':
        assert isinstance(obj, dict)
        showCards = from_bool(obj.get("showCards"))
        return ShowCardsDto(showCards)

    def to_dict(self) -> dict:
        result: dict = {}
        result["showCards"] = from_bool(self.showCards)
        return result


class VotekickDto(BaseModel):
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'VotekickDto':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        return VotekickDto(name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        return result


def JoinLobbyDtofromdict(s: Any) -> JoinLobbyDto:
    return JoinLobbyDto.from_dict(s)


def JoinLobbyDtotodict(x: JoinLobbyDto) -> Any:
    return to_class(JoinLobbyDto, x)


def RejoinLobbyDtofromdict(s: Any) -> RejoinLobbyDto:
    return RejoinLobbyDto.from_dict(s)


def RejoinLobbyDtotodict(x: RejoinLobbyDto) -> Any:
    return to_class(RejoinLobbyDto, x)


def RequestDisconnectDtofromdict(s: Any) -> RequestShutdownDto:
    return RequestShutdownDto.from_dict(s)


def RequestDisconnectDtotodict(x: RequestShutdownDto) -> Any:
    return to_class(RequestShutdownDto, x)


def RequestPokerStatisticsDtofromdict(s: Any) -> RequestShutdownDto:
    return RequestShutdownDto.from_dict(s)


def RequestPokerStatisticsDtotodict(x: RequestShutdownDto) -> Any:
    return to_class(RequestShutdownDto, x)


def RequestShutdownDtofromdict(s: Any) -> RequestShutdownDto:
    return RequestShutdownDto.from_dict(s)


def RequestShutdownDtotodict(x: RequestShutdownDto) -> Any:
    return to_class(RequestShutdownDto, x)


def SendMoveDtofromdict(s: Any) -> SendMoveDto:
    return SendMoveDto.from_dict(s)


def SendMoveDtotodict(x: SendMoveDto) -> Any:
    return to_class(SendMoveDto, x)


def ShowCardsDtofromdict(s: Any) -> ShowCardsDto:
    return ShowCardsDto.from_dict(s)


def ShowCardsDtotodict(x: ShowCardsDto) -> Any:
    return to_class(ShowCardsDto, x)


def VotekickDtofromdict(s: Any) -> VotekickDto:
    return VotekickDto.from_dict(s)


def VotekickDtotodict(x: VotekickDto) -> Any:
    return to_class(VotekickDto, x)
