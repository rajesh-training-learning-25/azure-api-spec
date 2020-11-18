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


class Credentials(Model):
    """The parameters that describes a set of credentials that will be used when a
    run is invoked.

    :param source_registry: Describes the credential parameters for accessing
     the source registry.
    :type source_registry:
     ~azure.mgmt.containerregistry.v2019_12_01_preview.models.SourceRegistryCredentials
    :param custom_registries: Describes the credential parameters for
     accessing other custom registries. The key
     for the dictionary item will be the registry login server
     (myregistry.azurecr.io) and
     the value of the item will be the registry credentials for accessing the
     registry.
    :type custom_registries: dict[str,
     ~azure.mgmt.containerregistry.v2019_12_01_preview.models.CustomRegistryCredentials]
    """

    _attribute_map = {
        'source_registry': {'key': 'sourceRegistry', 'type': 'SourceRegistryCredentials'},
        'custom_registries': {'key': 'customRegistries', 'type': '{CustomRegistryCredentials}'},
    }

    def __init__(self, *, source_registry=None, custom_registries=None, **kwargs) -> None:
        super(Credentials, self).__init__(**kwargs)
        self.source_registry = source_registry
        self.custom_registries = custom_registries
