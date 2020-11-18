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


class PipelineRunSourceProperties(Model):
    """PipelineRunSourceProperties.

    :param type: The type of the source. Possible values include:
     'AzureStorageBlob'. Default value: "AzureStorageBlob" .
    :type type: str or
     ~azure.mgmt.containerregistry.v2019_12_01_preview.models.PipelineRunSourceType
    :param name: The name of the source.
    :type name: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PipelineRunSourceProperties, self).__init__(**kwargs)
        self.type = kwargs.get('type', "AzureStorageBlob")
        self.name = kwargs.get('name', None)
