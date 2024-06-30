from enum import Enum


class ErrorCode(Enum):
    AUTH_INVALID_TOKEN = 'AUTH_INVALID_TOKEN'
    RESOURCE_NOT_FOUND = 'RESOURCE_NOT_FOUND'
    CONFLICT = 'CONFLICT'
    VALIDATION_FAILED = 'VALIDATION_FAILED'
    PERMISSION_DENIED = 'PERMISSION_DENIED'


ERROR_MESSAGES = {
    ErrorCode.AUTH_INVALID_TOKEN: 'The provided token is invalid.',
    ErrorCode.RESOURCE_NOT_FOUND: 'Requested resource was not found.',
    ErrorCode.CONFLICT: 'The request could not be completed due to a conflict.',
    ErrorCode.VALIDATION_FAILED: 'One or more fields are invalid.',
    ErrorCode.PERMISSION_DENIED: 'You do not have permission to access this resource.',
}
