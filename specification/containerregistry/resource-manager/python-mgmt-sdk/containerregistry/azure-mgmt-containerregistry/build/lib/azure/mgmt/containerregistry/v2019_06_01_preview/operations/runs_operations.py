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

import uuid
from msrest.pipeline import ClientRawResponse
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling

from .. import models


class RunsOperations(object):
    """RunsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The client API version. Constant value: "2019-06-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2019-06-01-preview"

        self.config = config

    def list(
            self, resource_group_name, registry_name, filter=None, top=None, custom_headers=None, raw=False, **operation_config):
        """Gets all the runs for a registry.

        :param resource_group_name: The name of the resource group to which
         the container registry belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param filter: The runs filter to apply on the operation. Arithmetic
         operators are not supported. The allowed string function is
         'contains'. All logical operators except 'Not', 'Has', 'All' are
         allowed.
        :type filter: str
        :param top: $top is supported for get list of runs, which limits the
         maximum number of runs to return.
        :type top: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Run
        :rtype:
         ~azure.mgmt.containerregistry.v2019_06_01_preview.models.RunPaged[~azure.mgmt.containerregistry.v2019_06_01_preview.models.Run]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.containerregistry.v2019_06_01_preview.models.ErrorResponseException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=1),
                    'registryName': self._serialize.url("registry_name", registry_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9]*$')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.RunPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.RunPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/runs'}

    def get(
            self, resource_group_name, registry_name, run_id, custom_headers=None, raw=False, **operation_config):
        """Gets the detailed information for a given run.

        :param resource_group_name: The name of the resource group to which
         the container registry belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param run_id: The run ID.
        :type run_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Run or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.containerregistry.v2019_06_01_preview.models.Run
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.containerregistry.v2019_06_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=1),
            'registryName': self._serialize.url("registry_name", registry_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9]*$'),
            'runId': self._serialize.url("run_id", run_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Run', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/runs/{runId}'}


    def _update_initial(
            self, resource_group_name, registry_name, run_id, is_archive_enabled=None, custom_headers=None, raw=False, **operation_config):
        run_update_parameters = models.RunUpdateParameters(is_archive_enabled=is_archive_enabled)

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=1),
            'registryName': self._serialize.url("registry_name", registry_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9]*$'),
            'runId': self._serialize.url("run_id", run_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(run_update_parameters, 'RunUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Run', response)
        if response.status_code == 201:
            deserialized = self._deserialize('Run', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def update(
            self, resource_group_name, registry_name, run_id, is_archive_enabled=None, custom_headers=None, raw=False, polling=True, **operation_config):
        """Patch the run properties.

        :param resource_group_name: The name of the resource group to which
         the container registry belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param run_id: The run ID.
        :type run_id: str
        :param is_archive_enabled: The value that indicates whether archiving
         is enabled or not.
        :type is_archive_enabled: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns Run or
         ClientRawResponse<Run> if raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~azure.mgmt.containerregistry.v2019_06_01_preview.models.Run]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~azure.mgmt.containerregistry.v2019_06_01_preview.models.Run]]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.containerregistry.v2019_06_01_preview.models.ErrorResponseException>`
        """
        raw_result = self._update_initial(
            resource_group_name=resource_group_name,
            registry_name=registry_name,
            run_id=run_id,
            is_archive_enabled=is_archive_enabled,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('Run', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/runs/{runId}'}

    def get_log_sas_url(
            self, resource_group_name, registry_name, run_id, custom_headers=None, raw=False, **operation_config):
        """Gets a link to download the run logs.

        :param resource_group_name: The name of the resource group to which
         the container registry belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param run_id: The run ID.
        :type run_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RunGetLogResult or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.containerregistry.v2019_06_01_preview.models.RunGetLogResult
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.containerregistry.v2019_06_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_log_sas_url.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=1),
            'registryName': self._serialize.url("registry_name", registry_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9]*$'),
            'runId': self._serialize.url("run_id", run_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('RunGetLogResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_log_sas_url.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/runs/{runId}/listLogSasUrl'}


    def _cancel_initial(
            self, resource_group_name, registry_name, run_id, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.cancel.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=1),
            'registryName': self._serialize.url("registry_name", registry_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9]*$'),
            'runId': self._serialize.url("run_id", run_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def cancel(
            self, resource_group_name, registry_name, run_id, custom_headers=None, raw=False, polling=True, **operation_config):
        """Cancel an existing run.

        :param resource_group_name: The name of the resource group to which
         the container registry belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param run_id: The run ID.
        :type run_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None or
         ClientRawResponse<None> if raw==True
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None] or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[None]]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.containerregistry.v2019_06_01_preview.models.ErrorResponseException>`
        """
        raw_result = self._cancel_initial(
            resource_group_name=resource_group_name,
            registry_name=registry_name,
            run_id=run_id,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    cancel.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/runs/{runId}/cancel'}
