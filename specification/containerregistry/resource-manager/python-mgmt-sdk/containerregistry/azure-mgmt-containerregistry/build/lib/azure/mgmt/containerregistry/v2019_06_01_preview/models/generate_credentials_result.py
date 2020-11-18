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


class GenerateCredentialsResult(Model):
    """The response from the GenerateCredentials operation.

    :param username: The username for a container registry.
    :type username: str
    :param passwords: The list of passwords for a container registry.
    :type passwords:
     list[~azure.mgmt.containerregistry.v2019_06_01_preview.models.TokenPassword]
    """

    _attribute_map = {
        'username': {'key': 'username', 'type': 'str'},
        'passwords': {'key': 'passwords', 'type': '[TokenPassword]'},
    }

    def __init__(self, **kwargs):
        super(GenerateCredentialsResult, self).__init__(**kwargs)
        self.username = kwargs.get('username', None)
        self.passwords = kwargs.get('passwords', None)
