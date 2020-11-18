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


class WebhookCreateParameters(Model):
    """The parameters for creating a webhook.

    All required parameters must be populated in order to send to Azure.

    :param tags: The tags for the webhook.
    :type tags: dict[str, str]
    :param location: Required. The location of the webhook. This cannot be
     changed after the resource is created.
    :type location: str
    :param service_uri: Required. The service URI for the webhook to post
     notifications.
    :type service_uri: str
    :param custom_headers: Custom headers that will be added to the webhook
     notifications.
    :type custom_headers: dict[str, str]
    :param status: The status of the webhook at the time the operation was
     called. Possible values include: 'enabled', 'disabled'
    :type status: str or
     ~azure.mgmt.containerregistry.v2020_11_01_preview.models.WebhookStatus
    :param scope: The scope of repositories where the event can be triggered.
     For example, 'foo:*' means events for all tags under repository 'foo'.
     'foo:bar' means events for 'foo:bar' only. 'foo' is equivalent to
     'foo:latest'. Empty means all events.
    :type scope: str
    :param actions: Required. The list of actions that trigger the webhook to
     post notifications.
    :type actions: list[str or
     ~azure.mgmt.containerregistry.v2020_11_01_preview.models.WebhookAction]
    """

    _validation = {
        'location': {'required': True},
        'service_uri': {'required': True},
        'actions': {'required': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'service_uri': {'key': 'properties.serviceUri', 'type': 'str'},
        'custom_headers': {'key': 'properties.customHeaders', 'type': '{str}'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'actions': {'key': 'properties.actions', 'type': '[str]'},
    }

    def __init__(self, *, location: str, service_uri: str, actions, tags=None, custom_headers=None, status=None, scope: str=None, **kwargs) -> None:
        super(WebhookCreateParameters, self).__init__(**kwargs)
        self.tags = tags
        self.location = location
        self.service_uri = service_uri
        self.custom_headers = custom_headers
        self.status = status
        self.scope = scope
        self.actions = actions
