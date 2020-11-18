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


class SecretObject(Model):
    """Describes the properties of a secret object value.

    :param value: The value of the secret. The format of this value will be
     determined
     based on the type of the secret object. If the type is Opaque, the value
     will be
     used as is without any modification.
    :type value: str
    :param type: The type of the secret object which determines how the value
     of the secret object has to be
     interpreted. Possible values include: 'Opaque', 'Vaultsecret'
    :type type: str or
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.SecretObjectType
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SecretObject, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.type = kwargs.get('type', None)
