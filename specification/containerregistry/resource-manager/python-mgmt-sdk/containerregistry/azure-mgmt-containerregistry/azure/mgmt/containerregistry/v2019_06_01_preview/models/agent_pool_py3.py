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

from .resource_py3 import Resource


class AgentPool(Resource):
    """The agentpool that has the ARM resource and properties.
    The agentpool will have all information to create an agent pool.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: Required. The location of the resource. This cannot be
     changed after the resource is created.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :ivar system_data: Metadata pertaining to creation and last modification
     of the resource.
    :vartype system_data:
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.SystemData
    :param count: The count of agent machine
    :type count: int
    :param tier: The Tier of agent machine
    :type tier: str
    :param os: The OS of agent machine. Possible values include: 'Windows',
     'Linux'
    :type os: str or
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.OS
    :param virtual_network_subnet_resource_id: The Virtual Network Subnet
     Resource Id of the agent machine
    :type virtual_network_subnet_resource_id: str
    :ivar provisioning_state: The provisioning state of this agent pool.
     Possible values include: 'Creating', 'Updating', 'Deleting', 'Succeeded',
     'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'system_data': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'count': {'key': 'properties.count', 'type': 'int'},
        'tier': {'key': 'properties.tier', 'type': 'str'},
        'os': {'key': 'properties.os', 'type': 'str'},
        'virtual_network_subnet_resource_id': {'key': 'properties.virtualNetworkSubnetResourceId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, count: int=None, tier: str=None, os=None, virtual_network_subnet_resource_id: str=None, **kwargs) -> None:
        super(AgentPool, self).__init__(location=location, tags=tags, **kwargs)
        self.count = count
        self.tier = tier
        self.os = os
        self.virtual_network_subnet_resource_id = virtual_network_subnet_resource_id
        self.provisioning_state = None
