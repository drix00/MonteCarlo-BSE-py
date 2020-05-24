#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.results.test_statistic
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the :py:mod:`mcbse.results.statistic` module.
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
import random

# Third party modules.
from pytest import approx

# Local modules.

# Project modules.
from mcbse.results.statistic import Statistic

# Globals and constants variables.


def test_is_discovered():
    """
    Test used to validate the file is included in the tests
    by the test framework.
    """
    # assert False
    assert True


def test_statistic_random_counts():
    magic_seed = 42
    random.seed(magic_seed)

    stats = Statistic()
    number_values = 20

    for i in range(number_values):
        stats.add_value(random.random())

    assert stats.counts == 20
    assert stats.min == approx(0.006498759678061017, abs=0.0001)
    assert stats.max == approx(0.8921795677048454, abs=0.0001)
    assert stats.mean == approx(0.38882570375878645, abs=0.0001)
    assert stats.variance == approx(0.08038972827674512, abs=0.0001)
    assert stats.standard_deviation == approx(0.28353082420919445, abs=0.0001)
    assert stats.mean_absolute_deviation == approx(0.0, abs=0.0001)
    assert stats.skewness == approx(0.146659708809682, abs=0.0001)
    assert stats.kurtosis == approx(0.0, abs=0.0001)


def test_statistic_skewness():
    stats = Statistic()

    stats.add_value(2)
    stats.add_value(7)
    stats.add_value(4)
    stats.add_value(9)
    stats.add_value(3)

    assert stats.counts == 5
    assert stats.min == approx(2.0, abs=0.0001)
    assert stats.max == approx(9.0, abs=0.0001)
    assert stats.mean == approx(5.0, abs=0.0001)
    assert stats.variance == approx(6.8, abs=0.0001)
    assert stats.standard_deviation == approx(2.6076809621, abs=0.0001)
    assert stats.mean_absolute_deviation == approx(0.0, abs=0.0001)
    assert stats.skewness == approx(0.406040288214, abs=1.0e-6)
    assert stats.kurtosis == approx(0.0, abs=0.0001)


def test_statistic_variance():
    stats = Statistic()

    stats.add_value(1)
    stats.add_value(2)
    stats.add_value(3)
    stats.add_value(4)
    stats.add_value(5)

    assert stats.counts == 5
    assert stats.min == approx(1.0, abs=0.0001)
    assert stats.max == approx(5.0, abs=0.0001)
    assert stats.mean == approx(3.0, abs=0.0001)
    assert stats.variance == approx(2.0, abs=0.0001)
    assert stats.standard_deviation == approx(1.4142135624, abs=0.0001)
    assert stats.mean_absolute_deviation == approx(0.0, abs=0.0001)
    assert stats.skewness == approx(0.0, abs=1.0e-6)
    assert stats.kurtosis == approx(0.0, abs=0.0001)
