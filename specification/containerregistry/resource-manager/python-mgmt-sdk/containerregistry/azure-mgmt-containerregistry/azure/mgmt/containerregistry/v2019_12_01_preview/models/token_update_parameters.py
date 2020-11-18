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


class TokenUpdateParameters(Model):
    """The parameters for updating a token.

    :param scope_map_id: The resource ID of the scope map to which the token
     will be associated with.
    :type scope_map_id: str
    :param status: The status of the token example enabled or disabled.
     Possible values include: 'enabled', 'disabled'
    :type status: str or
     ~azure.mgmt.containerregistry.v2019_12_01_preview.models.TokenStatus
    :param credentials: The credentials that can be used for authenticating
     the token.
    :type credentials:
     ~azure.mgmt.containerregistry.v2019_12_01_preview.models.TokenCredentialsProperties
    """

    _attribute_map = {
        'scope_map_id': {'key': 'properties.scopeMapId', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'credentials': {'key': 'properties.credentials', 'type': 'TokenCredentialsProperties'},
    }

    def __init__(self, **kwargs):
        super(TokenUpdateParameters, self).__init__(**kwargs)
        self.scope_map_id = kwargs.get('scope_map_id', None)
        self.status = kwargs.get('status', None)
        self.credentials = kwargs.get('credentials', None)
