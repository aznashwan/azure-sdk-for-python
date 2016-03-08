# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class SiteConfig(Resource):
    """
    Configuration of Azure web site

    :param str id: Resource Id
    :param str name: Resource Name
    :param str location: Resource Location
    :param str type: Resource type
    :param dict tags: Resource tags
    :param int number_of_workers: Number of workers
    :param list default_documents: Default documents
    :param str net_framework_version: Net Framework Version
    :param str php_version: Version of PHP
    :param str python_version: Version of Python
    :param bool request_tracing_enabled: Enable request tracing
    :param datetime request_tracing_expiration_time: Request tracing
     expiration time
    :param bool remote_debugging_enabled: Remote Debugging Enabled
    :param str remote_debugging_version: Remote Debugging Version
    :param bool http_logging_enabled: HTTP logging Enabled
    :param int logs_directory_size_limit: HTTP Logs Directory size limit
    :param bool detailed_error_logging_enabled: Detailed error logging enabled
    :param str publishing_username: Publishing user name
    :param str publishing_password: Publishing password
    :param list app_settings: Application Settings
    :param list metadata: Site Metadata
    :param list connection_strings: Connection strings
    :param list handler_mappings: Handler mappings
    :param str document_root: Document root
    :param str scm_type: SCM type
    :param bool use32_bit_worker_process: Use 32 bit worker process
    :param bool web_sockets_enabled: Web socket enabled.
    :param bool always_on: Always On
    :param str java_version: Java version
    :param str java_container: Java container
    :param str java_container_version: Java container version
    :param str managed_pipeline_mode: Managed pipeline mode. Possible values
     include: 'Integrated', 'Classic'
    :param list virtual_applications: Virtual applications
    :param str load_balancing: Site load balancing. Possible values include:
     'WeightedRoundRobin', 'LeastRequests', 'LeastResponseTime',
     'WeightedTotalTraffic', 'RequestHash'
    :param Experiments experiments: This is work around for polymophic types
    :param SiteLimits limits: Site limits
    :param bool auto_heal_enabled: Auto heal enabled
    :param AutoHealRules auto_heal_rules: Auto heal rules
    :param str tracing_options: Tracing options
    :param str vnet_name: Vnet name
    :param CorsSettings cors: Cross-Origin Resource Sharing (CORS) settings.
    :param ApiDefinitionInfo api_definition: Information about the formal API
     definition for the web app.
    :param str auto_swap_slot_name: Auto swap slot name
    :param bool local_my_sql_enabled: Local mysql enabled
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'number_of_workers': {'key': 'properties.numberOfWorkers', 'type': 'int'},
        'default_documents': {'key': 'properties.defaultDocuments', 'type': '[str]'},
        'net_framework_version': {'key': 'properties.netFrameworkVersion', 'type': 'str'},
        'php_version': {'key': 'properties.phpVersion', 'type': 'str'},
        'python_version': {'key': 'properties.pythonVersion', 'type': 'str'},
        'request_tracing_enabled': {'key': 'properties.requestTracingEnabled', 'type': 'bool'},
        'request_tracing_expiration_time': {'key': 'properties.requestTracingExpirationTime', 'type': 'iso-8601'},
        'remote_debugging_enabled': {'key': 'properties.remoteDebuggingEnabled', 'type': 'bool'},
        'remote_debugging_version': {'key': 'properties.remoteDebuggingVersion', 'type': 'str'},
        'http_logging_enabled': {'key': 'properties.httpLoggingEnabled', 'type': 'bool'},
        'logs_directory_size_limit': {'key': 'properties.logsDirectorySizeLimit', 'type': 'int'},
        'detailed_error_logging_enabled': {'key': 'properties.detailedErrorLoggingEnabled', 'type': 'bool'},
        'publishing_username': {'key': 'properties.publishingUsername', 'type': 'str'},
        'publishing_password': {'key': 'properties.publishingPassword', 'type': 'str'},
        'app_settings': {'key': 'properties.appSettings', 'type': '[NameValuePair]'},
        'metadata': {'key': 'properties.metadata', 'type': '[NameValuePair]'},
        'connection_strings': {'key': 'properties.connectionStrings', 'type': '[ConnStringInfo]'},
        'handler_mappings': {'key': 'properties.handlerMappings', 'type': '[HandlerMapping]'},
        'document_root': {'key': 'properties.documentRoot', 'type': 'str'},
        'scm_type': {'key': 'properties.scmType', 'type': 'str'},
        'use32_bit_worker_process': {'key': 'properties.use32BitWorkerProcess', 'type': 'bool'},
        'web_sockets_enabled': {'key': 'properties.webSocketsEnabled', 'type': 'bool'},
        'always_on': {'key': 'properties.alwaysOn', 'type': 'bool'},
        'java_version': {'key': 'properties.javaVersion', 'type': 'str'},
        'java_container': {'key': 'properties.javaContainer', 'type': 'str'},
        'java_container_version': {'key': 'properties.javaContainerVersion', 'type': 'str'},
        'managed_pipeline_mode': {'key': 'properties.managedPipelineMode', 'type': 'ManagedPipelineMode'},
        'virtual_applications': {'key': 'properties.virtualApplications', 'type': '[VirtualApplication]'},
        'load_balancing': {'key': 'properties.loadBalancing', 'type': 'SiteLoadBalancing'},
        'experiments': {'key': 'properties.experiments', 'type': 'Experiments'},
        'limits': {'key': 'properties.limits', 'type': 'SiteLimits'},
        'auto_heal_enabled': {'key': 'properties.autoHealEnabled', 'type': 'bool'},
        'auto_heal_rules': {'key': 'properties.autoHealRules', 'type': 'AutoHealRules'},
        'tracing_options': {'key': 'properties.tracingOptions', 'type': 'str'},
        'vnet_name': {'key': 'properties.vnetName', 'type': 'str'},
        'cors': {'key': 'properties.cors', 'type': 'CorsSettings'},
        'api_definition': {'key': 'properties.apiDefinition', 'type': 'ApiDefinitionInfo'},
        'auto_swap_slot_name': {'key': 'properties.autoSwapSlotName', 'type': 'str'},
        'local_my_sql_enabled': {'key': 'properties.localMySqlEnabled', 'type': 'bool'},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, number_of_workers=None, default_documents=None, net_framework_version=None, php_version=None, python_version=None, request_tracing_enabled=None, request_tracing_expiration_time=None, remote_debugging_enabled=None, remote_debugging_version=None, http_logging_enabled=None, logs_directory_size_limit=None, detailed_error_logging_enabled=None, publishing_username=None, publishing_password=None, app_settings=None, metadata=None, connection_strings=None, handler_mappings=None, document_root=None, scm_type=None, use32_bit_worker_process=None, web_sockets_enabled=None, always_on=None, java_version=None, java_container=None, java_container_version=None, managed_pipeline_mode=None, virtual_applications=None, load_balancing=None, experiments=None, limits=None, auto_heal_enabled=None, auto_heal_rules=None, tracing_options=None, vnet_name=None, cors=None, api_definition=None, auto_swap_slot_name=None, local_my_sql_enabled=None, **kwargs):
        super(SiteConfig, self).__init__(id=id, name=name, location=location, type=type, tags=tags, **kwargs)
        self.number_of_workers = number_of_workers
        self.default_documents = default_documents
        self.net_framework_version = net_framework_version
        self.php_version = php_version
        self.python_version = python_version
        self.request_tracing_enabled = request_tracing_enabled
        self.request_tracing_expiration_time = request_tracing_expiration_time
        self.remote_debugging_enabled = remote_debugging_enabled
        self.remote_debugging_version = remote_debugging_version
        self.http_logging_enabled = http_logging_enabled
        self.logs_directory_size_limit = logs_directory_size_limit
        self.detailed_error_logging_enabled = detailed_error_logging_enabled
        self.publishing_username = publishing_username
        self.publishing_password = publishing_password
        self.app_settings = app_settings
        self.metadata = metadata
        self.connection_strings = connection_strings
        self.handler_mappings = handler_mappings
        self.document_root = document_root
        self.scm_type = scm_type
        self.use32_bit_worker_process = use32_bit_worker_process
        self.web_sockets_enabled = web_sockets_enabled
        self.always_on = always_on
        self.java_version = java_version
        self.java_container = java_container
        self.java_container_version = java_container_version
        self.managed_pipeline_mode = managed_pipeline_mode
        self.virtual_applications = virtual_applications
        self.load_balancing = load_balancing
        self.experiments = experiments
        self.limits = limits
        self.auto_heal_enabled = auto_heal_enabled
        self.auto_heal_rules = auto_heal_rules
        self.tracing_options = tracing_options
        self.vnet_name = vnet_name
        self.cors = cors
        self.api_definition = api_definition
        self.auto_swap_slot_name = auto_swap_slot_name
        self.local_my_sql_enabled = local_my_sql_enabled