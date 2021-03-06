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


class Site(Resource):
    """
    Represents a web app

    :param str id: Resource Id
    :param str name: Resource Name
    :param str location: Resource Location
    :param str type: Resource type
    :param dict tags: Resource tags
    :param str site_name: Name of web app
    :param str state: State of the web app
    :param list host_names: Hostnames associated with web app
    :param str repository_site_name: Name of repository site
    :param str usage_state: State indicating whether web app has exceeded its
     quota usage. Possible values include: 'Normal', 'Exceeded'
    :param bool enabled: True if the site is enabled; otherwise, false.
     Setting this  value to false disables the site (takes the site off line).
    :param list enabled_host_names: Hostnames for the web app that are
     enabled. Hostnames need to be assigned and enabled. If some hostnames
     are assigned but not enabled
     the app is not served on those hostnames
    :param str availability_state: Management information availability state
     for the web app. Possible values are Normal or Limited.
     Normal means that the site is running correctly and that
     management information for the site is available.
     Limited means that only partial management information for
     the site is available and that detailed site information is unavailable.
     Possible values include: 'Normal', 'Limited', 'DisasterRecoveryMode'
    :param list host_name_ssl_states: Hostname SSL states are  used to manage
     the SSL bindings for site's hostnames.
    :param str server_farm_id:
    :param datetime last_modified_time_utc: Last time web app was modified in
     UTC
    :param SiteConfig site_config: Configuration of web app
    :param list traffic_manager_host_names: Read-only list of Azure Traffic
     manager hostnames associated with web app
    :param bool premium_app_deployed: If set indicates whether web app is
     deployed as a premium app
    :param bool scm_site_also_stopped: If set indicates whether to stop SCM
     (KUDU) site when the web app is stopped. Default is false.
    :param str target_swap_slot: Read-only property that specifies which slot
     this app will swap into
    :param HostingEnvironmentProfile hosting_environment_profile:
     Specification for the hosting environment (App Service Environment) to
     use for the web app
    :param str micro_service:
    :param str gateway_site_name: Name of gateway app associated with web app
    :param bool client_affinity_enabled: Specifies if the client affinity is
     enabled when load balancing http request for multiple instances of the
     web app
    :param bool client_cert_enabled: Specifies if the client certificate is
     enabled for the web app
    :param bool host_names_disabled: Specifies if the public hostnames are
     disabled the web app.
     If set to true the app is only accessible via API Management
     process
    :param str outbound_ip_addresses: List of comma separated IP addresses
     that this web app uses for outbound connections. Those can be used when
     configuring firewall rules for databases accessed by this web app.
    :param CloningInfo cloning_info: This is only valid for web app creation.
     If specified, web app is cloned from
     a source web app
    """

    _required = []

    _attribute_map = {
        'site_name': {'key': 'properties.name', 'type': 'str', 'flatten': True},
        'state': {'key': 'properties.state', 'type': 'str', 'flatten': True},
        'host_names': {'key': 'properties.hostNames', 'type': '[str]', 'flatten': True},
        'repository_site_name': {'key': 'properties.repositorySiteName', 'type': 'str', 'flatten': True},
        'usage_state': {'key': 'properties.usageState', 'type': 'UsageState', 'flatten': True},
        'enabled': {'key': 'properties.enabled', 'type': 'bool', 'flatten': True},
        'enabled_host_names': {'key': 'properties.enabledHostNames', 'type': '[str]', 'flatten': True},
        'availability_state': {'key': 'properties.availabilityState', 'type': 'SiteAvailabilityState', 'flatten': True},
        'host_name_ssl_states': {'key': 'properties.hostNameSslStates', 'type': '[HostNameSslState]', 'flatten': True},
        'server_farm_id': {'key': 'properties.serverFarmId', 'type': 'str', 'flatten': True},
        'last_modified_time_utc': {'key': 'properties.lastModifiedTimeUtc', 'type': 'iso-8601', 'flatten': True},
        'site_config': {'key': 'properties.siteConfig', 'type': 'SiteConfig', 'flatten': True},
        'traffic_manager_host_names': {'key': 'properties.trafficManagerHostNames', 'type': '[str]', 'flatten': True},
        'premium_app_deployed': {'key': 'properties.premiumAppDeployed', 'type': 'bool', 'flatten': True},
        'scm_site_also_stopped': {'key': 'properties.scmSiteAlsoStopped', 'type': 'bool', 'flatten': True},
        'target_swap_slot': {'key': 'properties.targetSwapSlot', 'type': 'str', 'flatten': True},
        'hosting_environment_profile': {'key': 'properties.hostingEnvironmentProfile', 'type': 'HostingEnvironmentProfile', 'flatten': True},
        'micro_service': {'key': 'properties.microService', 'type': 'str', 'flatten': True},
        'gateway_site_name': {'key': 'properties.gatewaySiteName', 'type': 'str', 'flatten': True},
        'client_affinity_enabled': {'key': 'properties.clientAffinityEnabled', 'type': 'bool', 'flatten': True},
        'client_cert_enabled': {'key': 'properties.clientCertEnabled', 'type': 'bool', 'flatten': True},
        'host_names_disabled': {'key': 'properties.hostNamesDisabled', 'type': 'bool', 'flatten': True},
        'outbound_ip_addresses': {'key': 'properties.outboundIpAddresses', 'type': 'str', 'flatten': True},
        'cloning_info': {'key': 'properties.cloningInfo', 'type': 'CloningInfo', 'flatten': True},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, site_name=None, state=None, host_names=None, repository_site_name=None, usage_state=None, enabled=None, enabled_host_names=None, availability_state=None, host_name_ssl_states=None, server_farm_id=None, last_modified_time_utc=None, site_config=None, traffic_manager_host_names=None, premium_app_deployed=None, scm_site_also_stopped=None, target_swap_slot=None, hosting_environment_profile=None, micro_service=None, gateway_site_name=None, client_affinity_enabled=None, client_cert_enabled=None, host_names_disabled=None, outbound_ip_addresses=None, cloning_info=None):
        super(Site, self).__init__(id=id, name=name, location=location, type=type, tags=tags)
        self.site_name = site_name
        self.state = state
        self.host_names = host_names
        self.repository_site_name = repository_site_name
        self.usage_state = usage_state
        self.enabled = enabled
        self.enabled_host_names = enabled_host_names
        self.availability_state = availability_state
        self.host_name_ssl_states = host_name_ssl_states
        self.server_farm_id = server_farm_id
        self.last_modified_time_utc = last_modified_time_utc
        self.site_config = site_config
        self.traffic_manager_host_names = traffic_manager_host_names
        self.premium_app_deployed = premium_app_deployed
        self.scm_site_also_stopped = scm_site_also_stopped
        self.target_swap_slot = target_swap_slot
        self.hosting_environment_profile = hosting_environment_profile
        self.micro_service = micro_service
        self.gateway_site_name = gateway_site_name
        self.client_affinity_enabled = client_affinity_enabled
        self.client_cert_enabled = client_cert_enabled
        self.host_names_disabled = host_names_disabled
        self.outbound_ip_addresses = outbound_ip_addresses
        self.cloning_info = cloning_info
