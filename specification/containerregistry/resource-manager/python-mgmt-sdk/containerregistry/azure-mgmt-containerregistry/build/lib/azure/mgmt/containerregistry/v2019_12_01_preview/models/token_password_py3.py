# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TokenPassword(Model):
    """The password that will be used for authenticating the token of a container
    registry.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param creation_time: The creation datetime of the password.
    :type creation_time: datetime
    :param expiry: The expiry datetime of the password.
    :type expiry: datetime
    :param name: The password name "password1" or "password2". Possible values
     include: 'password1', 'password2'
    :type name: str or
     ~azure.mgmt.containerregistry.v2019_12_01_preview.models.TokenPasswordName
    :ivar value: The password value.
    :vartype value: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'expiry': {'key': 'expiry', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, *, creation_time=None, expiry=None, name=None, **kwargs) -> None:
        super(TokenPassword, self).__init__(**kwargs)
        self.creation_time = creation_time
        self.expiry = expiry
        self.name = name
        self.value = None
