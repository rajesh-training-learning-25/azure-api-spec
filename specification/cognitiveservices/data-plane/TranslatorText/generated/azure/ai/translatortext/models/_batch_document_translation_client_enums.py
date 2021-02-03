# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ErrorCodeV2(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enums containing high level error codes.
    """

    INVALID_REQUEST = "InvalidRequest"
    INVALID_ARGUMENT = "InvalidArgument"
    INTERNAL_SERVER_ERROR = "InternalServerError"
    SERVICE_UNAVAILABLE = "ServiceUnavailable"
    RESOURCE_NOT_FOUND = "ResourceNotFound"
    UNAUTHORIZED = "Unauthorized"
    REQUEST_RATE_TOO_HIGH = "RequestRateTooHigh"

class Status(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """List of possible statuses for job or document
    """

    NOT_STARTED = "NotStarted"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    CANCELLING = "Cancelling"

class StorageInputType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Storage type of the input documents source string
    """

    FOLDER = "Folder"
    FILE = "File"
