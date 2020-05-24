#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.models.test_rutherford
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the :py:mod:`mcbse.models.rutherford` module.
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
import math

# Third party modules.
from pytest import approx

# Local modules.

# Project modules.
from mcbse.models.rutherford import Rutherford

# Globals and constants variables.


def test_is_discovered():
    """
    Test used to validate the file is included in the tests
    by the test framework.
    """
    # assert False
    assert True


def test_rutherford_compute_alpha():
    model = Rutherford(13)

    assert model.compute_alpha(1000.0) == approx(0.0189592417, rel=0.01)
    assert model.compute_alpha(10000.0) == approx(0.0018959242, rel=0.01)
    assert model.compute_alpha(100000.0) == approx(0.0001895924, rel=0.01)


def test_rutherford_compute_sigma_nm2():
    model = Rutherford(13)

    assert model.compute_sigma_nm2(1000.0) == approx(0.0142905422, rel=0.01)
    assert model.compute_sigma_nm2(10000.0) == approx(0.0014788533, rel=0.01)
    assert model.compute_sigma_nm2(100000.0) == approx(0.0001724173, rel=0.01)


def test_rutherford_compute_scattering_angle_rad():
    model = Rutherford(13)

    assert model.compute_scattering_angle_rad(10000.0, 0.0) == approx(0.0, rel=0.01)
    assert model.compute_scattering_angle_rad(10000.0, 0.1) == approx(0.0289986301, rel=0.01)
    assert model.compute_scattering_angle_rad(10000.0, 0.5) == approx(0.0869471704, rel=0.01)
    assert model.compute_scattering_angle_rad(10000.0, 1.0) == approx(3.1415924959, rel=0.01)
    assert model.compute_scattering_angle_rad(10000.0, 1.0) == approx(math.pi, rel=0.01)


def test_rutherford_compute_azimuthal_angle_rad():
    model = Rutherford(13)

    assert model.compute_azimuthal_angle_rad(0.0) == approx(0.0, rel=0.01)
    assert model.compute_azimuthal_angle_rad(0.1) == approx(0.6283185307, rel=0.01)
    assert model.compute_azimuthal_angle_rad(0.5) == approx(3.1415926536, rel=0.01)
    assert model.compute_azimuthal_angle_rad(1.0) == approx(6.2831853072, rel=0.01)
    assert model.compute_azimuthal_angle_rad(1.0) == approx(2.0 * math.pi, rel=0.01)
