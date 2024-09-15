from http import HTTPStatus

from fastapi import HTTPException


class AppException(HTTPException):
    def __init__(
        self, status_code: int, details: str, headers: dict[str, str] | None = None
    ):
        super().__init__(status_code, details, headers)


class EntityNotFoundException(AppException):
    def __init__(self, details: str):
        super().__init__(HTTPStatus.NOT_FOUND, details)


class EntityAlreadyExistsException(AppException):
    def __init__(self, details: str):
        super().__init__(HTTPStatus.CONFLICT, details)


class UnauthorizedException(AppException):
    def __init__(self, details: str | None):
        super().__init__(
            HTTPStatus.UNAUTHORIZED,
            "Unauthorized" if details is None else details,
            {"WWW-Authenticate": "Basic"},
        )


class ForbiddenException(AppException):
    def __init__(self, details: str | None):
        super().__init__(
            HTTPStatus.FORBIDDEN, "Access is denied" if details is None else details
        )


class ValidationException(AppException):
    def __init__(self, details: str):
        super().__init__(HTTPStatus.BAD_REQUEST, details)


class InvalidFormatException(AppException):
    def __init__(self, details: str):
        super().__init__(HTTPStatus.BAD_REQUEST, details)
