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


class SyncProperties(Model):
    """The sync properties of the connected registry with its parent.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param token_id: Required. The resource ID of the ACR token used to
     authenticate the connected registry to its parent during sync.
    :type token_id: str
    :param schedule: The cron expression indicating the schedule that the
     connected registry will sync with its parent.
    :type schedule: str
    :param sync_window: The time window during which sync is enabled for each
     schedule occurrence. Specify the duration using the format
     P[n]Y[n]M[n]DT[n]H[n]M[n]S as per ISO8601.
    :type sync_window: timedelta
    :param message_ttl: Required. The period of time for which a message is
     available to sync before it is expired. Specify the duration using the
     format P[n]Y[n]M[n]DT[n]H[n]M[n]S as per ISO8601.
    :type message_ttl: timedelta
    :ivar last_sync_time: The last time a sync occurred between the connected
     registry and its parent.
    :vartype last_sync_time: datetime
    :ivar gateway_endpoint: The gateway endpoint used by the connected
     registry to communicate with its parent.
    :vartype gateway_endpoint: str
    """

    _validation = {
        'token_id': {'required': True},
        'message_ttl': {'required': True},
        'last_sync_time': {'readonly': True},
        'gateway_endpoint': {'readonly': True},
    }

    _attribute_map = {
        'token_id': {'key': 'tokenId', 'type': 'str'},
        'schedule': {'key': 'schedule', 'type': 'str'},
        'sync_window': {'key': 'syncWindow', 'type': 'duration'},
        'message_ttl': {'key': 'messageTtl', 'type': 'duration'},
        'last_sync_time': {'key': 'lastSyncTime', 'type': 'iso-8601'},
        'gateway_endpoint': {'key': 'gatewayEndpoint', 'type': 'str'},
    }

    def __init__(self, *, token_id: str, message_ttl, schedule: str=None, sync_window=None, **kwargs) -> None:
        super(SyncProperties, self).__init__(**kwargs)
        self.token_id = token_id
        self.schedule = schedule
        self.sync_window = sync_window
        self.message_ttl = message_ttl
        self.last_sync_time = None
        self.gateway_endpoint = None
