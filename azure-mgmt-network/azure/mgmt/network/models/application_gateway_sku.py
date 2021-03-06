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


class ApplicationGatewaySku(Model):
    """
    SKU of application gateway

    :param str name: Gets or sets name of application gateway SKU. Possible
     values include: 'Standard_Small', 'Standard_Medium', 'Standard_Large'
    :param str tier: Gets or sets tier of application gateway. Possible
     values include: 'Standard'
    :param int capacity: Gets or sets capacity (instance count) of
     application gateway
    """

    _required = []

    _attribute_map = {
        'name': {'key': 'name', 'type': 'ApplicationGatewaySkuName'},
        'tier': {'key': 'tier', 'type': 'ApplicationGatewayTier'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(self, name=None, tier=None, capacity=None):
        self.name = name
        self.tier = tier
        self.capacity = capacity
