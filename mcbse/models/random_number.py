#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcbse.models.random_number
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Random number model.
"""

###############################################################################
# Copyright 2020 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.
import random

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.


class RandomNumber:
    magic_seed = 42

    def __init__(self, seed):
        random.seed(seed)

    def __call__(self):
        value = random.random()
        return value
