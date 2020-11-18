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


class ExportPipeline(ProxyResource):
    """An object that represents an export pipeline for a container registry.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

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
    :param location: The location of the export pipeline.
    :type location: str
    :param identity: The identity of the export pipeline.
    :type identity:
     ~azure.mgmt.containerregistry.v2020_11_01_preview.models.IdentityProperties
    :param target: Required. The target properties of the export pipeline.
    :type target:
     ~azure.mgmt.containerregistry.v2020_11_01_preview.models.ExportPipelineTargetProperties
    :param options: The list of all options configured for the pipeline.
    :type options: list[str or
     ~azure.mgmt.containerregistry.v2020_11_01_preview.models.PipelineOptions]
    :ivar provisioning_state: The provisioning state of the pipeline at the
     time the operation was called. Possible values include: 'Creating',
     'Updating', 'Deleting', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.containerregistry.v2020_11_01_preview.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
        'target': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'IdentityProperties'},
        'target': {'key': 'properties.target', 'type': 'ExportPipelineTargetProperties'},
        'options': {'key': 'properties.options', 'type': '[str]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExportPipeline, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.identity = kwargs.get('identity', None)
        self.target = kwargs.get('target', None)
        self.options = kwargs.get('options', None)
        self.provisioning_state = None
