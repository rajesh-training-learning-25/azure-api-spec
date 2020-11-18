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


class RetentionPolicy(Model):
    """The retention policy for a container registry.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param days: The number of days to retain an untagged manifest after which
     it gets purged. Default value: 7 .
    :type days: int
    :ivar last_updated_time: The timestamp when the policy was last updated.
    :vartype last_updated_time: datetime
    :param status: The value that indicates whether the policy is enabled or
     not. Possible values include: 'enabled', 'disabled'. Default value:
     "disabled" .
    :type status: str or
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.PolicyStatus
    """

    _validation = {
        'last_updated_time': {'readonly': True},
    }

    _attribute_map = {
        'days': {'key': 'days', 'type': 'int'},
        'last_updated_time': {'key': 'lastUpdatedTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RetentionPolicy, self).__init__(**kwargs)
        self.days = kwargs.get('days', 7)
        self.last_updated_time = None
        self.status = kwargs.get('status', "disabled")
