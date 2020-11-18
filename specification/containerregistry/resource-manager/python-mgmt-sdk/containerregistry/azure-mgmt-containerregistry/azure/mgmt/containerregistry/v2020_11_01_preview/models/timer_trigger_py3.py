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


class TimerTrigger(Model):
    """The properties of a timer trigger.

    All required parameters must be populated in order to send to Azure.

    :param schedule: Required. The CRON expression for the task schedule
    :type schedule: str
    :param status: The current status of trigger. Possible values include:
     'Enabled', 'Disabled'. Default value: "Enabled" .
    :type status: str or
     ~azure.mgmt.containerregistry.v2020_11_01_preview.models.TriggerStatus
    :param name: Required. The name of the trigger.
    :type name: str
    """

    _validation = {
        'schedule': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'schedule': {'key': 'schedule', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, schedule: str, name: str, status="Enabled", **kwargs) -> None:
        super(TimerTrigger, self).__init__(**kwargs)
        self.schedule = schedule
        self.status = status
        self.name = name
