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

from .proxy_resource import ProxyResource


class PrivateEndpointConnection(ProxyResource):
    """An object that represents a private endpoint connection for a container
    registry.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar system_data: Metadata pertaining to creation and last modification
     of the resource.
    :vartype system_data:
     ~azure.mgmt.containerregistry.v2020_11_01_preview.models.SystemData
    :param private_endpoint: The resource of private endpoint.
    :type private_endpoint:
     ~azure.mgmt.containerregistry.v2020_11_01_preview.models.PrivateEndpoint
    :param private_link_service_connection_state: A collection of information
     about the state of the connection between service consumer and provider.
    :type private_link_service_connection_state:
     ~azure.mgmt.containerregistry.v2020_11_01_preview.models.PrivateLinkServiceConnectionState
    :ivar provisioning_state: The provisioning state of private endpoint
     connection resource. Possible values include: 'Creating', 'Updating',
     'Deleting', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.containerregistry.v2020_11_01_preview.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'private_endpoint': {'key': 'properties.privateEndpoint', 'type': 'PrivateEndpoint'},
        'private_link_service_connection_state': {'key': 'properties.privateLinkServiceConnectionState', 'type': 'PrivateLinkServiceConnectionState'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PrivateEndpointConnection, self).__init__(**kwargs)
        self.private_endpoint = kwargs.get('private_endpoint', None)
        self.private_link_service_connection_state = kwargs.get('private_link_service_connection_state', None)
        self.provisioning_state = None
