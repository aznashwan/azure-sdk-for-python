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

from msrest.serialization import Model


class ProviderOperationsMetadata(Model):
    """
    Provider Operations metadata

    :param str id: Gets or sets the provider id.
    :param str name: Gets or sets the provider name
    :param str type: Gets or sets the provider type
    :param str display_name: Gets or sets the provider display name
    :param list resource_types: Gets or sets the provider resource types
    :param list operations: Gets or sets the provider operations
    """

    _required = []

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'resource_types': {'key': 'resourceTypes', 'type': '[ResourceType]'},
        'operations': {'key': 'operations', 'type': '[ProviderOperation]'},
    }

    def __init__(self, id=None, name=None, type=None, display_name=None, resource_types=None, operations=None):
        self.id = id
        self.name = name
        self.type = type
        self.display_name = display_name
        self.resource_types = resource_types
        self.operations = operations
