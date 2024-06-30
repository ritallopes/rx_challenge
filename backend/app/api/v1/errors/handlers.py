from fastapi import HTTPException

from .codes.py import ERROR_MESSAGES, ErrorCode


def raise_error(error_code: ErrorCode, status_code: int, details: str = None):
    error_message = ERROR_MESSAGES[error_code]
    raise HTTPException(
        status_code=status_code,
        detail={
            'status': 'error',
            'error_code': error_code.value,
            'message': error_message,
            'details': details or error_message,
        },
    )
