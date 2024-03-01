from __future__ import annotations

from enum import IntEnum


class ErrorCode(IntEnum):
    SUGGESTION_MESSAGE_DELETED = 1
    MISSING_PERMISSIONS = 2
    MISSING_SUGGESTIONS_CHANNEL = 3
    MISSING_LOG_CHANNEL = 4
    SUGGESTION_NOT_FOUND = 5
    OWNER_ONLY = 6
    SUGGESTION_CONTENT_TOO_LONG = 7
    INVALID_GUILD_CONFIG_CHOICE = 8
    COMMAND_ON_COOLDOWN = 9
    GENERIC_FORBIDDEN = 10
    UNHANDLED_ERROR = 11
    GENERIC_NOT_FOUND = 12
    CONFIGURED_CHANNEL_NO_LONGER_EXISTS = 13
    MISSING_FETCH_PERMISSIONS_IN_SUGGESTIONS_CHANNEL = 14
    MISSING_FETCH_PERMISSIONS_IN_LOGS_CHANNEL = 15
    MISSING_TRANSLATION = 16
    SUGGESTION_RESOLUTION_ERROR = 17
    MISSING_SEND_PERMISSIONS_IN_SUGGESTION_CHANNEL = 18
    MISSING_THREAD_CREATE_PERMISSIONS = 19
    QUEUE_IMBALANCE = 20
    MISSING_QUEUE_CHANNEL = 21
    BLOCKLISTED_USER = 22
    INVALID_FILE_TYPE = 23

    @classmethod
    def from_value(cls, value: int) -> ErrorCode:
        return ErrorCode(value)
