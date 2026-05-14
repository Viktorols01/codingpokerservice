from pydantic import BaseModel
from typing import Any, TypeVar, Type, cast


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
