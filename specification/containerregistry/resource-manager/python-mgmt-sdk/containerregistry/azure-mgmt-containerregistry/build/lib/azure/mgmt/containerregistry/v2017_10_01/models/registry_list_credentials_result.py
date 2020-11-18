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


class RegistryListCredentialsResult(Model):
    """The response from the ListCredentials operation.

    :param username: The username for a container registry.
    :type username: str
    :param passwords: The list of passwords for a container registry.
    :type passwords:
     list[~azure.mgmt.containerregistry.v2017_10_01.models.RegistryPassword]
    """

    _attribute_map = {
        'username': {'key': 'username', 'type': 'str'},
        'passwords': {'key': 'passwords', 'type': '[RegistryPassword]'},
    }

    def __init__(self, **kwargs):
        super(RegistryListCredentialsResult, self).__init__(**kwargs)
        self.username = kwargs.get('username', None)
        self.passwords = kwargs.get('passwords', None)
