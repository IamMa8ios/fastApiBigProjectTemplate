from fastapi import HTTPException, status


class NotFoundException(HTTPException):
    def __init__(self, message: str | None = None):
        self.message = message or "Not found"
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=self.message,
        )


class BadRequestException(HTTPException):
    def __init__(self, message: str | None = None):
        self.message = message or "Bad request"
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=self.message,
        )


class ValidationException(HTTPException):
    def __init__(self, message: str | None = None):
        self.message = message or "Validation error"
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=self.message,
        )


class FileUploadException(HTTPException):
    def __init__(self):
        self.message = "Failed to upload file"
        super().__init__(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=self.message,
        )


class FileParsingException(HTTPException):
    def __init__(self, detail: str | dict[str, any] | list[str] | list[dict[str, any]]):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
