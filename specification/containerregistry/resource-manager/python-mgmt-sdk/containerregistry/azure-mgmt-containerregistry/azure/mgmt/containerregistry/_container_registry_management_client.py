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

from azure.mgmt.core import ARMPipelineClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import ContainerRegistryManagementClientConfiguration

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class ContainerRegistryManagementClient(MultiApiClientMixin, _SDKClient):
    """ContainerRegistryManagementClient.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2019-05-01'
    _PROFILE_TAG = "azure.mgmt.containerregistry.ContainerRegistryManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
            'build_steps': '2018-02-01-preview',
            'build_tasks': '2018-02-01-preview',
            'builds': '2018-02-01-preview',
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        api_version=None,
        base_url=None,
        profile=KnownProfiles.default,
        **kwargs  # type: Any
    ):
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ContainerRegistryManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(ContainerRegistryManagementClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2017-03-01: :mod:`v2017_03_01.models<azure.mgmt.containerregistry.v2017_03_01.models>`
           * 2017-10-01: :mod:`v2017_10_01.models<azure.mgmt.containerregistry.v2017_10_01.models>`
           * 2018-02-01-preview: :mod:`v2018_02_01_preview.models<azure.mgmt.containerregistry.v2018_02_01_preview.models>`
           * 2018-09-01: :mod:`v2018_09_01.models<azure.mgmt.containerregistry.v2018_09_01.models>`
           * 2019-04-01: :mod:`v2019_04_01.models<azure.mgmt.containerregistry.v2019_04_01.models>`
           * 2019-05-01: :mod:`v2019_05_01.models<azure.mgmt.containerregistry.v2019_05_01.models>`
           * 2019-05-01-preview: :mod:`v2019_05_01_preview.models<azure.mgmt.containerregistry.v2019_05_01_preview.models>`
           * 2019-06-01-preview: :mod:`v2019_06_01_preview.models<azure.mgmt.containerregistry.v2019_06_01_preview.models>`
           * 2019-12-01-preview: :mod:`v2019_12_01_preview.models<azure.mgmt.containerregistry.v2019_12_01_preview.models>`
        """
        if api_version == '2017-03-01':
            from .v2017_03_01 import models
            return models
        elif api_version == '2017-10-01':
            from .v2017_10_01 import models
            return models
        elif api_version == '2018-02-01-preview':
            from .v2018_02_01_preview import models
            return models
        elif api_version == '2018-09-01':
            from .v2018_09_01 import models
            return models
        elif api_version == '2019-04-01':
            from .v2019_04_01 import models
            return models
        elif api_version == '2019-05-01':
            from .v2019_05_01 import models
            return models
        elif api_version == '2019-05-01-preview':
            from .v2019_05_01_preview import models
            return models
        elif api_version == '2019-06-01-preview':
            from .v2019_06_01_preview import models
            return models
        elif api_version == '2019-12-01-preview':
            from .v2019_12_01_preview import models
            return models
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def agent_pools(self):
        """Instance depends on the API version:

           * 2019-06-01-preview: :class:`AgentPoolsOperations<azure.mgmt.containerregistry.v2019_06_01_preview.operations.AgentPoolsOperations>`
           * 2019-12-01-preview: :class:`AgentPoolsOperations<azure.mgmt.containerregistry.v2019_12_01_preview.operations.AgentPoolsOperations>`
        """
        api_version = self._get_api_version('agent_pools')
        if api_version == '2019-06-01-preview':
            from .v2019_06_01_preview.operations import AgentPoolsOperations as OperationClass
        elif api_version == '2019-12-01-preview':
            from .v2019_12_01_preview.operations import AgentPoolsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import AgentPoolsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'agent_pools'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def build_steps(self):
        """Instance depends on the API version:

           * 2018-02-01-preview: :class:`BuildStepsOperations<azure.mgmt.containerregistry.v2018_02_01_preview.operations.BuildStepsOperations>`
        """
        api_version = self._get_api_version('build_steps')
        if api_version == '2018-02-01-preview':
            from .v2018_02_01_preview.operations import BuildStepsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'build_steps'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def build_tasks(self):
        """Instance depends on the API version:

           * 2018-02-01-preview: :class:`BuildTasksOperations<azure.mgmt.containerregistry.v2018_02_01_preview.operations.BuildTasksOperations>`
        """
        api_version = self._get_api_version('build_tasks')
        if api_version == '2018-02-01-preview':
            from .v2018_02_01_preview.operations import BuildTasksOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'build_tasks'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def builds(self):
        """Instance depends on the API version:

           * 2018-02-01-preview: :class:`BuildsOperations<azure.mgmt.containerregistry.v2018_02_01_preview.operations.BuildsOperations>`
        """
        api_version = self._get_api_version('builds')
        if api_version == '2018-02-01-preview':
            from .v2018_02_01_preview.operations import BuildsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'builds'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def export_pipelines(self):
        """Instance depends on the API version:

           * 2019-12-01-preview: :class:`ExportPipelinesOperations<azure.mgmt.containerregistry.v2019_12_01_preview.operations.ExportPipelinesOperations>`
        """
        api_version = self._get_api_version('export_pipelines')
        if api_version == '2019-12-01-preview':
            from .v2019_12_01_preview.operations import ExportPipelinesOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import ExportPipelinesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'export_pipelines'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def import_pipelines(self):
        """Instance depends on the API version:

           * 2019-12-01-preview: :class:`ImportPipelinesOperations<azure.mgmt.containerregistry.v2019_12_01_preview.operations.ImportPipelinesOperations>`
        """
        api_version = self._get_api_version('import_pipelines')
        if api_version == '2019-12-01-preview':
            from .v2019_12_01_preview.operations import ImportPipelinesOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import ImportPipelinesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'import_pipelines'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2017-03-01: :class:`Operations<azure.mgmt.containerregistry.v2017_03_01.operations.Operations>`
           * 2017-10-01: :class:`Operations<azure.mgmt.containerregistry.v2017_10_01.operations.Operations>`
           * 2018-02-01-preview: :class:`Operations<azure.mgmt.containerregistry.v2018_02_01_preview.operations.Operations>`
           * 2018-09-01: :class:`Operations<azure.mgmt.containerregistry.v2018_09_01.operations.Operations>`
           * 2019-04-01: :class:`Operations<azure.mgmt.containerregistry.v2019_04_01.operations.Operations>`
           * 2019-05-01: :class:`Operations<azure.mgmt.containerregistry.v2019_05_01.operations.Operations>`
           * 2019-05-01-preview: :class:`Operations<azure.mgmt.containerregistry.v2019_05_01_preview.operations.Operations>`
           * 2019-06-01-preview: :class:`Operations<azure.mgmt.containerregistry.v2019_06_01_preview.operations.Operations>`
           * 2019-12-01-preview: :class:`Operations<azure.mgmt.containerregistry.v2019_12_01_preview.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2017-03-01':
            from .v2017_03_01.operations import Operations as OperationClass
        elif api_version == '2017-10-01':
            from .v2017_10_01.operations import Operations as OperationClass
        elif api_version == '2018-02-01-preview':
            from .v2018_02_01_preview.operations import Operations as OperationClass
        elif api_version == '2018-09-01':
            from .v2018_09_01.operations import Operations as OperationClass
        elif api_version == '2019-04-01':
            from .v2019_04_01.operations import Operations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import Operations as OperationClass
        elif api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import Operations as OperationClass
        elif api_version == '2019-06-01-preview':
            from .v2019_06_01_preview.operations import Operations as OperationClass
        elif api_version == '2019-12-01-preview':
            from .v2019_12_01_preview.operations import Operations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def pipeline_runs(self):
        """Instance depends on the API version:

           * 2019-12-01-preview: :class:`PipelineRunsOperations<azure.mgmt.containerregistry.v2019_12_01_preview.operations.PipelineRunsOperations>`
        """
        api_version = self._get_api_version('pipeline_runs')
        if api_version == '2019-12-01-preview':
            from .v2019_12_01_preview.operations import PipelineRunsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import PipelineRunsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'pipeline_runs'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_endpoint_connections(self):
        """Instance depends on the API version:

           * 2019-12-01-preview: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.containerregistry.v2019_12_01_preview.operations.PrivateEndpointConnectionsOperations>`
        """
        api_version = self._get_api_version('private_endpoint_connections')
        if api_version == '2019-12-01-preview':
            from .v2019_12_01_preview.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import PrivateEndpointConnectionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_endpoint_connections'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def registries(self):
        """Instance depends on the API version:

           * 2017-03-01: :class:`RegistriesOperations<azure.mgmt.containerregistry.v2017_03_01.operations.RegistriesOperations>`
           * 2017-10-01: :class:`RegistriesOperations<azure.mgmt.containerregistry.v2017_10_01.operations.RegistriesOperations>`
           * 2018-02-01-preview: :class:`RegistriesOperations<azure.mgmt.containerregistry.v2018_02_01_preview.operations.RegistriesOperations>`
           * 2018-09-01: :class:`RegistriesOperations<azure.mgmt.containerregistry.v2018_09_01.operations.RegistriesOperations>`
           * 2019-04-01: :class:`RegistriesOperations<azure.mgmt.containerregistry.v2019_04_01.operations.RegistriesOperations>`
           * 2019-05-01: :class:`RegistriesOperations<azure.mgmt.containerregistry.v2019_05_01.operations.RegistriesOperations>`
           * 2019-05-01-preview: :class:`RegistriesOperations<azure.mgmt.containerregistry.v2019_05_01_preview.operations.RegistriesOperations>`
           * 2019-06-01-preview: :class:`RegistriesOperations<azure.mgmt.containerregistry.v2019_06_01_preview.operations.RegistriesOperations>`
           * 2019-12-01-preview: :class:`RegistriesOperations<azure.mgmt.containerregistry.v2019_12_01_preview.operations.RegistriesOperations>`
        """
        api_version = self._get_api_version('registries')
        if api_version == '2017-03-01':
            from .v2017_03_01.operations import RegistriesOperations as OperationClass
        elif api_version == '2017-10-01':
            from .v2017_10_01.operations import RegistriesOperations as OperationClass
        elif api_version == '2018-02-01-preview':
            from .v2018_02_01_preview.operations import RegistriesOperations as OperationClass
        elif api_version == '2018-09-01':
            from .v2018_09_01.operations import RegistriesOperations as OperationClass
        elif api_version == '2019-04-01':
            from .v2019_04_01.operations import RegistriesOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import RegistriesOperations as OperationClass
        elif api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import RegistriesOperations as OperationClass
        elif api_version == '2019-06-01-preview':
            from .v2019_06_01_preview.operations import RegistriesOperations as OperationClass
        elif api_version == '2019-12-01-preview':
            from .v2019_12_01_preview.operations import RegistriesOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import RegistriesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'registries'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def replications(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`ReplicationsOperations<azure.mgmt.containerregistry.v2017_10_01.operations.ReplicationsOperations>`
           * 2018-02-01-preview: :class:`ReplicationsOperations<azure.mgmt.containerregistry.v2018_02_01_preview.operations.ReplicationsOperations>`
           * 2018-09-01: :class:`ReplicationsOperations<azure.mgmt.containerregistry.v2018_09_01.operations.ReplicationsOperations>`
           * 2019-04-01: :class:`ReplicationsOperations<azure.mgmt.containerregistry.v2019_04_01.operations.ReplicationsOperations>`
           * 2019-05-01: :class:`ReplicationsOperations<azure.mgmt.containerregistry.v2019_05_01.operations.ReplicationsOperations>`
           * 2019-05-01-preview: :class:`ReplicationsOperations<azure.mgmt.containerregistry.v2019_05_01_preview.operations.ReplicationsOperations>`
           * 2019-06-01-preview: :class:`ReplicationsOperations<azure.mgmt.containerregistry.v2019_06_01_preview.operations.ReplicationsOperations>`
           * 2019-12-01-preview: :class:`ReplicationsOperations<azure.mgmt.containerregistry.v2019_12_01_preview.operations.ReplicationsOperations>`
        """
        api_version = self._get_api_version('replications')
        if api_version == '2017-10-01':
            from .v2017_10_01.operations import ReplicationsOperations as OperationClass
        elif api_version == '2018-02-01-preview':
            from .v2018_02_01_preview.operations import ReplicationsOperations as OperationClass
        elif api_version == '2018-09-01':
            from .v2018_09_01.operations import ReplicationsOperations as OperationClass
        elif api_version == '2019-04-01':
            from .v2019_04_01.operations import ReplicationsOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import ReplicationsOperations as OperationClass
        elif api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import ReplicationsOperations as OperationClass
        elif api_version == '2019-06-01-preview':
            from .v2019_06_01_preview.operations import ReplicationsOperations as OperationClass
        elif api_version == '2019-12-01-preview':
            from .v2019_12_01_preview.operations import ReplicationsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2019_12_01_preview.operations import ReplicationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'replications'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def runs(self):
        """Instance depends on the API version:

           * 2018-09-01: :class:`RunsOperations<azure.mgmt.containerregistry.v2018_09_01.operations.RunsOperations>`
           * 2019-04-01: :class:`RunsOperations<azure.mgmt.containerregistry.v2019_04_01.operations.RunsOperations>`
           * 2019-05-01: :class:`RunsOperations<azure.mgmt.containerregistry.v2019_05_01.operations.RunsOperations>`
           * 2019-06-01-preview: :class:`RunsOperations<azure.mgmt.containerregistry.v2019_06_01_preview.operations.RunsOperations>`
           * 2019-12-01-preview: :class:`RunsOperations<azure.mgmt.containerregistry.v2019_12_01_preview.operations.RunsOperations>`
        """
        api_version = self._get_api_version('runs')
        if api_version == '2018-09-01':
            from .v2018_09_01.operations import RunsOperations as OperationClass
        elif api_version == '2019-04-01':
            from .v2019_04_01.operations import RunsOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import RunsOperations as OperationClass
        elif api_version == '2019-06-01-preview':
            from .v2019_06_01_preview.operations import RunsOperations as OperationClass
        elif api_version == '2019-12-01-preview':
            from .v2019_12_01_preview.operations import RunsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import RunsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'runs'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def scope_maps(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`ScopeMapsOperations<azure.mgmt.containerregistry.v2019_05_01_preview.operations.ScopeMapsOperations>`
           * 2019-06-01-preview: :class:`ScopeMapsOperations<azure.mgmt.containerregistry.v2019_06_01_preview.operations.ScopeMapsOperations>`
           * 2019-12-01-preview: :class:`ScopeMapsOperations<azure.mgmt.containerregistry.v2019_12_01_preview.operations.ScopeMapsOperations>`
        """
        api_version = self._get_api_version('scope_maps')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import ScopeMapsOperations as OperationClass
        elif api_version == '2019-06-01-preview':
            from .v2019_06_01_preview.operations import ScopeMapsOperations as OperationClass
        elif api_version == '2019-12-01-preview':
            from .v2019_12_01_preview.operations import ScopeMapsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import ScopeMapsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'scope_maps'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def task_runs(self):
        """Instance depends on the API version:

           * 2019-06-01-preview: :class:`TaskRunsOperations<azure.mgmt.containerregistry.v2019_06_01_preview.operations.TaskRunsOperations>`
           * 2019-12-01-preview: :class:`TaskRunsOperations<azure.mgmt.containerregistry.v2019_12_01_preview.operations.TaskRunsOperations>`
        """
        api_version = self._get_api_version('task_runs')
        if api_version == '2019-06-01-preview':
            from .v2019_06_01_preview.operations import TaskRunsOperations as OperationClass
        elif api_version == '2019-12-01-preview':
            from .v2019_12_01_preview.operations import TaskRunsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import TaskRunsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'task_runs'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def tasks(self):
        """Instance depends on the API version:

           * 2018-09-01: :class:`TasksOperations<azure.mgmt.containerregistry.v2018_09_01.operations.TasksOperations>`
           * 2019-04-01: :class:`TasksOperations<azure.mgmt.containerregistry.v2019_04_01.operations.TasksOperations>`
           * 2019-05-01: :class:`TasksOperations<azure.mgmt.containerregistry.v2019_05_01.operations.TasksOperations>`
           * 2019-06-01-preview: :class:`TasksOperations<azure.mgmt.containerregistry.v2019_06_01_preview.operations.TasksOperations>`
           * 2019-12-01-preview: :class:`TasksOperations<azure.mgmt.containerregistry.v2019_12_01_preview.operations.TasksOperations>`
        """
        api_version = self._get_api_version('tasks')
        if api_version == '2018-09-01':
            from .v2018_09_01.operations import TasksOperations as OperationClass
        elif api_version == '2019-04-01':
            from .v2019_04_01.operations import TasksOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import TasksOperations as OperationClass
        elif api_version == '2019-06-01-preview':
            from .v2019_06_01_preview.operations import TasksOperations as OperationClass
        elif api_version == '2019-12-01-preview':
            from .v2019_12_01_preview.operations import TasksOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import TasksOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'tasks'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def tokens(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`TokensOperations<azure.mgmt.containerregistry.v2019_05_01_preview.operations.TokensOperations>`
           * 2019-06-01-preview: :class:`TokensOperations<azure.mgmt.containerregistry.v2019_06_01_preview.operations.TokensOperations>`
           * 2019-12-01-preview: :class:`TokensOperations<azure.mgmt.containerregistry.v2019_12_01_preview.operations.TokensOperations>`
        """
        api_version = self._get_api_version('tokens')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import TokensOperations as OperationClass
        elif api_version == '2019-06-01-preview':
            from .v2019_06_01_preview.operations import TokensOperations as OperationClass
        elif api_version == '2019-12-01-preview':
            from .v2019_12_01_preview.operations import TokensOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import TokensOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'tokens'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def webhooks(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`WebhooksOperations<azure.mgmt.containerregistry.v2017_10_01.operations.WebhooksOperations>`
           * 2018-02-01-preview: :class:`WebhooksOperations<azure.mgmt.containerregistry.v2018_02_01_preview.operations.WebhooksOperations>`
           * 2018-09-01: :class:`WebhooksOperations<azure.mgmt.containerregistry.v2018_09_01.operations.WebhooksOperations>`
           * 2019-04-01: :class:`WebhooksOperations<azure.mgmt.containerregistry.v2019_04_01.operations.WebhooksOperations>`
           * 2019-05-01: :class:`WebhooksOperations<azure.mgmt.containerregistry.v2019_05_01.operations.WebhooksOperations>`
           * 2019-05-01-preview: :class:`WebhooksOperations<azure.mgmt.containerregistry.v2019_05_01_preview.operations.WebhooksOperations>`
           * 2019-06-01-preview: :class:`WebhooksOperations<azure.mgmt.containerregistry.v2019_06_01_preview.operations.WebhooksOperations>`
           * 2019-12-01-preview: :class:`WebhooksOperations<azure.mgmt.containerregistry.v2019_12_01_preview.operations.WebhooksOperations>`
        """
        api_version = self._get_api_version('webhooks')
        if api_version == '2017-10-01':
            from .v2017_10_01.operations import WebhooksOperations as OperationClass
        elif api_version == '2018-02-01-preview':
            from .v2018_02_01_preview.operations import WebhooksOperations as OperationClass
        elif api_version == '2018-09-01':
            from .v2018_09_01.operations import WebhooksOperations as OperationClass
        elif api_version == '2019-04-01':
            from .v2019_04_01.operations import WebhooksOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import WebhooksOperations as OperationClass
        elif api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import WebhooksOperations as OperationClass
        elif api_version == '2019-06-01-preview':
            from .v2019_06_01_preview.operations import WebhooksOperations as OperationClass
        elif api_version == '2019-12-01-preview':
            from .v2019_12_01_preview.operations import WebhooksOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import WebhooksOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'webhooks'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)