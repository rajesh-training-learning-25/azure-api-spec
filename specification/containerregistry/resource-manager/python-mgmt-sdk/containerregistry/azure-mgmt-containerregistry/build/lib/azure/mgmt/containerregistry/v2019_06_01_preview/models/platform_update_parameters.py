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


class PlatformUpdateParameters(Model):
    """The properties for updating the platform configuration.

    :param os: The operating system type required for the run. Possible values
     include: 'Windows', 'Linux'
    :type os: str or
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.OS
    :param architecture: The OS architecture. Possible values include:
     'amd64', 'x86', '386', 'arm', 'arm64'
    :type architecture: str or
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.Architecture
    :param variant: Variant of the CPU. Possible values include: 'v6', 'v7',
     'v8'
    :type variant: str or
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.Variant
    """

    _attribute_map = {
        'os': {'key': 'os', 'type': 'str'},
        'architecture': {'key': 'architecture', 'type': 'str'},
        'variant': {'key': 'variant', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PlatformUpdateParameters, self).__init__(**kwargs)
        self.os = kwargs.get('os', None)
        self.architecture = kwargs.get('architecture', None)
        self.variant = kwargs.get('variant', None)
