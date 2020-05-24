#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.results.test_counter
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the :py:mod:`mcbse.results.counter` module.
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
from pytest import approx

# Local modules.

# Project modules.
from mcbse.results.counter import Counter

# Globals and constants variables.


def test_is_discovered():
    """
    Test used to validate the file is included in the tests
    by the test framework.
    """
    # assert False
    assert True


def test_counter_variance():
    counter = Counter()
    counter.add_value(1)
    counter.add_value(2)
    counter.add_value(3)
    counter.add_value(4)
    counter.add_value(5)

    assert counter.counts == 5
    assert counter.min == approx(1.0, abs=0.0001)
    assert counter.max == approx(5.0, abs=0.0001)
    assert counter.mean == approx(3.0, abs=0.0001)
    assert counter.variance == approx(0.4, abs=0.0001)
    assert counter.standard_deviation == approx(0.632455532, abs=0.0001)


def test_counter_bse():
    counter = Counter()

    counter.add_value(1)
    counter.add_value(1)
    counter.add_value(0)
    counter.add_value(0)
    counter.add_value(0)
    counter.add_value(1)
    counter.add_value(1)
    counter.add_value(0)
    counter.add_value(0)
    counter.add_value(0)

    variance_ref = (0.4 * (1.0 - 0.4)) / 10.0
    assert counter.counts == 10
    assert counter.min == approx(0.0, abs=0.0001)
    assert counter.max == approx(1.0, abs=0.0001)
    assert counter.mean == approx(0.4, abs=0.0001)
    assert counter.variance == approx(variance_ref, abs=0.0001)
    assert counter.standard_deviation == approx(math.sqrt(variance_ref), abs=0.0001)
