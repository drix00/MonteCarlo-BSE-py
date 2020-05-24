#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.models.test_direction_cosine
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the :py:mod:`mcbse.models.direction_cosine` module.
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
from mcbse.models.direction_cosine import DirectionCosine

# Globals and constants variables.


def test_is_discovered():
    """
    Test used to validate the file is included in the tests
    by the test framework.
    """
    # assert False
    assert True


def test_compute():
    tolerance = 1.0e-6

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(0.0, 0.0)
    assert model.ca == approx(0.0, abs=tolerance)
    assert model.cb == approx(0.0, abs=tolerance)
    assert model.cc == approx(1.0, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(math.pi / 4.0, 0.0)
    assert model.ca == approx(0.70710678118654757, abs=tolerance)
    assert model.cb == approx(0.0, abs=tolerance)
    assert model.cc == approx(0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(-math.pi / 4.0, 0.0)
    assert model.ca == approx(-0.70710678118654746, abs=tolerance)
    assert model.cb == approx(0.0, abs=tolerance)
    assert model.cc == approx(0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(0.0, math.pi / 4.0)
    assert model.ca == approx(0.0, abs=tolerance)
    assert model.cb == approx(0.0, abs=tolerance)
    assert model.cc == approx(1.0, abs=tolerance)

    model.compute(0.0, -math.pi / 4.0)
    assert model.ca == approx(0.0, abs=tolerance)
    assert model.cb == approx(0.0, abs=tolerance)
    assert model.cc == approx(1.0, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(math.pi / 4.0, math.pi / 4.0)
    assert model.ca == approx(0.5, abs=tolerance)
    assert model.cb == approx(0.5, abs=tolerance)
    assert model.cc == approx(0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(-math.pi / 4.0, math.pi / 4.0)
    assert model.ca == approx(-0.5, abs=tolerance)
    assert model.cb == approx(-0.5, abs=tolerance)
    assert model.cc == approx(0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(math.pi / 4.0, -math.pi / 4.0)
    assert model.ca == approx(0.5, abs=tolerance)
    assert model.cb == approx(-0.5, abs=tolerance)
    assert model.cc == approx(0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(-math.pi / 4.0, -math.pi / 4.0)
    assert model.ca == approx(-0.5, abs=tolerance)
    assert model.cb == approx(0.5, abs=tolerance)
    assert model.cc == approx(0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(2.0 * math.pi / 4.0, 0.0)
    assert model.ca == approx(1.0, abs=tolerance)
    assert model.cb == approx(0.0, abs=tolerance)
    assert model.cc == approx(0.0, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(3.0 * math.pi / 4.0, 0.0)
    assert model.ca == approx(0.70710678118654757, abs=tolerance)
    assert model.cb == approx(0.0, abs=tolerance)
    assert model.cc == approx(-0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(4.0 * math.pi / 4.0, 0.0)
    assert model.ca == approx(0.0, abs=tolerance)
    assert model.cb == approx(0.0, abs=tolerance)
    assert model.cc == approx(-1.0, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(5.0 * math.pi / 4.0, 0.0)
    assert model.ca == approx(-0.70710678118654757, abs=tolerance)
    assert model.cb == approx(0.0, abs=tolerance)
    assert model.cc == approx(-0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(6.0 * math.pi / 4.0, 0.0)
    assert model.ca == approx(-1.0, abs=tolerance)
    assert model.cb == approx(0.0, abs=tolerance)
    assert model.cc == approx(0.0, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(7.0 * math.pi / 4.0, 0.0)
    assert model.ca == approx(-0.70710678118654757, abs=tolerance)
    assert model.cb == approx(0.0, abs=tolerance)
    assert model.cc == approx(0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(8.0 * math.pi / 4.0, 0.0)
    assert model.ca == approx(0.0, abs=tolerance)
    assert model.cb == approx(0.0, abs=tolerance)
    assert model.cc == approx(1.0, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(math.pi / 4.0, 2.0 * math.pi / 4.0)
    assert model.ca == approx(0.0, abs=tolerance)
    assert model.cb == approx(0.70710678118654757, abs=tolerance)
    assert model.cc == approx(0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(math.pi / 4.0, 3.0 * math.pi / 4.0)
    assert model.ca == approx(-0.5, abs=tolerance)
    assert model.cb == approx(0.5, abs=tolerance)
    assert model.cc == approx(0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(math.pi / 4.0, 4.0 * math.pi / 4.0)
    assert model.ca == approx(-0.70710678118654757, abs=tolerance)
    assert model.cb == approx(0.0, abs=tolerance)
    assert model.cc == approx(0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(math.pi / 4.0, 5.0 * math.pi / 4.0)
    assert model.ca == approx(-0.5, abs=tolerance)
    assert model.cb == approx(-0.5, abs=tolerance)
    assert model.cc == approx(0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(math.pi / 4.0, 6.0 * math.pi / 4.0)
    assert model.ca == approx(0.0, abs=tolerance)
    assert model.cb == approx(-0.70710678118654757, abs=tolerance)
    assert model.cc == approx(0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(math.pi / 4.0, 7.0 * math.pi / 4.0)
    assert model.ca == approx(0.5, abs=tolerance)
    assert model.cb == approx(-0.5, abs=tolerance)
    assert model.cc == approx(0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 0.0, 1.0)
    model.compute(math.pi / 4.0, 8.0 * math.pi / 4.0)
    assert model.ca == approx(0.70710678118654757, abs=tolerance)
    assert model.cb == approx(0.0, abs=tolerance)
    assert model.cc == approx(0.70710678118654757, abs=tolerance)

    model = DirectionCosine(0.0, 1.0, 0.0)
    model.compute(0.0, 0.0)
    assert model.ca == approx(0.0, abs=tolerance)
    assert model.cb == approx(1.0, abs=tolerance)
    assert model.cc == approx(0.0, abs=tolerance)

    model = DirectionCosine(0.0, 1.0, 0.0)
    model.compute(math.pi / 4.0, 0.0)
    assert model.ca == approx(0.70710678118654757, abs=tolerance)
    assert model.cb == approx(0.70710678118654757, abs=tolerance)
    assert model.cc == approx(0.0, abs=tolerance)
