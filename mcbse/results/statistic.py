#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcbse.results.statistic
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Statistic of a series of values for a quantity X.
"""

###############################################################################
# Copyright 2020 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License")
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
import math

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.


class Statistic:
    def __init__(self):
        self.counts = 0

        self.sum_x = 0.0
        self.sum_xx = 0.0
        self.sum_xxx = 0.0
        self.sum_xxxx = 0.0

        self.min = 1.0e9
        self.max = -1.0e9

    def add_value(self, value_):
        self.counts += 1

        self.sum_x += value_
        self.sum_xx += value_ * value_
        self.sum_xxx += value_ * value_ * value_
        self.sum_xxxx += value_ * value_ * value_ * value_

        self.min = min(self.min, value_)
        self.max = max(self.max, value_)

    @property
    def mean(self):
        value = self.sum_x / self.counts
        return value

    @property
    def variance(self):
        value = self.sum_xx / self.counts - self.mean * self.mean
        return value

    @property
    def standard_deviation(self):
        value = math.sqrt(self.variance)
        return value

    @property
    def mean_absolute_deviation(self):
        return 0.0

    @property
    def skewness(self):
        term1 = self.sum_xxx / self.counts
        term2 = 3.0 * self.mean * self.standard_deviation * self.standard_deviation
        term3 = self.mean * self.mean * self.mean
        nominator = term1 - term2 - term3
        denominator = self.standard_deviation * self.standard_deviation * self.standard_deviation
        value = nominator / denominator

        return value

    @property
    def kurtosis(self):
        return 0.0
