# -*- coding: utf-8 -*-
#
# Copyright 2016 BigML
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


"""Options for BigMLer analyze

"""
from __future__ import absolute_import


import os

def get_whizzml_options(defaults=None):
    """Adding arguments for the whizzml subcommand

    """


    if defaults is None:
        defaults = {}

    options = {
        # directory for the package
        '--package-dir': {
            "action": 'store',
            "dest": 'package_dir',
            "default": defaults.get('package_dir', None),
            "help": "Directory for the package."}}

    return options
