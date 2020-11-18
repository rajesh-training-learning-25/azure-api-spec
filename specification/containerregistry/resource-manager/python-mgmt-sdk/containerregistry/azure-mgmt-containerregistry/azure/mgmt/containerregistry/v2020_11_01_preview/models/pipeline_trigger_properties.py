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


class PipelineTriggerProperties(Model):
    """PipelineTriggerProperties.

    :param source_trigger: The source trigger properties of the pipeline.
    :type source_trigger:
     ~azure.mgmt.containerregistry.v2020_11_01_preview.models.PipelineSourceTriggerProperties
    """

    _attribute_map = {
        'source_trigger': {'key': 'sourceTrigger', 'type': 'PipelineSourceTriggerProperties'},
    }

    def __init__(self, **kwargs):
        super(PipelineTriggerProperties, self).__init__(**kwargs)
        self.source_trigger = kwargs.get('source_trigger', None)
