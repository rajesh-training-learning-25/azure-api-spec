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

from .task_step_properties import TaskStepProperties


class EncodedTaskStep(TaskStepProperties):
    """The properties of a encoded task step.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar base_image_dependencies: List of base image dependencies for a step.
    :vartype base_image_dependencies:
     list[~azure.mgmt.containerregistry.v2018_09_01.models.BaseImageDependency]
    :param context_path: The URL(absolute or relative) of the source context
     for the task step.
    :type context_path: str
    :param context_access_token: The token (git PAT or SAS token of storage
     account blob) associated with the context for a step.
    :type context_access_token: str
    :param type: Required. Constant filled by server.
    :type type: str
    :param encoded_task_content: Required. Base64 encoded value of the
     template/definition file content.
    :type encoded_task_content: str
    :param encoded_values_content: Base64 encoded value of the
     parameters/values file content.
    :type encoded_values_content: str
    :param values: The collection of overridable values that can be passed
     when running a task.
    :type values:
     list[~azure.mgmt.containerregistry.v2018_09_01.models.SetValue]
    """

    _validation = {
        'base_image_dependencies': {'readonly': True},
        'type': {'required': True},
        'encoded_task_content': {'required': True},
    }

    _attribute_map = {
        'base_image_dependencies': {'key': 'baseImageDependencies', 'type': '[BaseImageDependency]'},
        'context_path': {'key': 'contextPath', 'type': 'str'},
        'context_access_token': {'key': 'contextAccessToken', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'encoded_task_content': {'key': 'encodedTaskContent', 'type': 'str'},
        'encoded_values_content': {'key': 'encodedValuesContent', 'type': 'str'},
        'values': {'key': 'values', 'type': '[SetValue]'},
    }

    def __init__(self, **kwargs):
        super(EncodedTaskStep, self).__init__(**kwargs)
        self.encoded_task_content = kwargs.get('encoded_task_content', None)
        self.encoded_values_content = kwargs.get('encoded_values_content', None)
        self.values = kwargs.get('values', None)
        self.type = 'EncodedTask'
