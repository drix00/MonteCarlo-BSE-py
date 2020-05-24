#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.models.test_random_number
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the :py:mod:`mcbse.models.random_number` module.
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

# Third party modules.
from pytest import approx

# Local modules.

# Project modules.
from mcbse.results.statistic import Statistic
from mcbse.models.random_number import RandomNumber
from tests import slow_test

# Globals and constants variables.


def test_is_discovered():
    """
    Test used to validate the file is included in the tests
    by the test framework.
    """
    # assert False
    assert True


def test_random_number_magic_seed():
    random_number = RandomNumber(RandomNumber.magic_seed)

    assert random_number() == approx(0.6394267984578837, abs=0.0001)
    assert random_number() == approx(0.025010755222666936, abs=0.0001)
    assert random_number() == approx(0.27502931836911926, abs=0.0001)
    assert random_number() == approx(0.22321073814882275, abs=0.0001)
    assert random_number() == approx(0.7364712141640124, abs=0.0001)
    assert random_number() == approx(0.6766994874229113, abs=0.0001)
    assert random_number() == approx(0.8921795677048454, abs=0.0001)
    assert random_number() == approx(0.08693883262941615, abs=0.0001)
    assert random_number() == approx(0.4219218196852704, abs=0.0001)
    assert random_number() == approx(0.029797219438070344, abs=0.0001)


@slow_test
def test_random_number_statistic_1M():  # pragma: no cover
    random_number = RandomNumber(RandomNumber.magic_seed)

    stats = Statistic()
    number_values = 1000000

    for i in range(number_values):
        stats.add_value(random_number())

    assert stats.counts == number_values
    assert stats.min == approx(0.0000008088, abs=0.0001)
    assert stats.max == approx(0.9999985263, abs=0.0001)
    assert stats.mean == approx(0.5000145439034656, abs=0.0001)
    assert stats.variance == approx(0.0832747386, abs=0.0001)
    assert stats.standard_deviation == approx(0.2885736278, abs=0.0001)
    assert stats.mean_absolute_deviation == approx(0.0, abs=0.0001)
    assert stats.skewness == approx(-0.0007863836102638839, abs=0.0001)
    assert stats.kurtosis == approx(0.0, abs=0.0001)
