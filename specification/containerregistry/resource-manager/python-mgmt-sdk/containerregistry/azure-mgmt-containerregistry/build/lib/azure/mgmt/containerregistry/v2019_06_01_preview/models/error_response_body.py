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


class ErrorResponseBody(Model):
    """An error response from the Azure Container Registry service.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. error code.
    :type code: str
    :param message: Required. error message.
    :type message: str
    :param target: target of the particular error.
    :type target: str
    :param details: an array of additional nested error response info objects,
     as described by this contract.
    :type details:
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.InnerErrorDescription
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': 'InnerErrorDescription'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponseBody, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)
