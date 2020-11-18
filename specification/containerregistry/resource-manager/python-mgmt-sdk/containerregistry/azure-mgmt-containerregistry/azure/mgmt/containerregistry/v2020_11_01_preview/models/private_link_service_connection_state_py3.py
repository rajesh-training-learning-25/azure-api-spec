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


class PrivateLinkServiceConnectionState(Model):
    """The state of a private link service connection.

    :param status: The private link service connection status. Possible values
     include: 'Approved', 'Pending', 'Rejected', 'Disconnected'
    :type status: str or
     ~azure.mgmt.containerregistry.v2020_11_01_preview.models.ConnectionStatus
    :param description: The description for connection status. For example if
     connection is rejected it can indicate reason for rejection.
    :type description: str
    :param actions_required: A message indicating if changes on the service
     provider require any updates on the consumer. Possible values include:
     'None', 'Recreate'
    :type actions_required: str or
     ~azure.mgmt.containerregistry.v2020_11_01_preview.models.ActionsRequired
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'actions_required': {'key': 'actionsRequired', 'type': 'str'},
    }

    def __init__(self, *, status=None, description: str=None, actions_required=None, **kwargs) -> None:
        super(PrivateLinkServiceConnectionState, self).__init__(**kwargs)
        self.status = status
        self.description = description
        self.actions_required = actions_required
