#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.models.test_energy_loss
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the :py:mod:`mcbse.models.energy_loss` module.
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
from mcbse.models.energy_loss import EnergyLoss

# Globals and constants variables.


def test_is_discovered():
    """
    Test used to validate the file is included in the tests
    by the test framework.
    """
    # assert False
    assert True


def test_compute_mean_ionisation_potential_eV():
    model = EnergyLoss(13, 26.98)

    assert model.compute_mean_ionisation_potential_eV() == approx(162.8140881753, abs=0.01)


def test_compute_bethe1933():
    model = EnergyLoss(13, 26.98)

    assert model.compute_bethe1930(200.0) == approx(-67949.0105710835, abs=0.01)
    assert model.compute_bethe1930(300.0) == approx(-96420.8060125956, abs=0.01)
    assert model.compute_bethe1930(1000.0) == approx(-74465.6875715554, abs=0.01)
    assert model.compute_bethe1930(10000.0) == approx(-16155.9389847331, abs=0.01)
    assert model.compute_bethe1930(100000.0) == approx(-2486.5309212311, abs=0.01)


def test_compute_joy_luo1989():
    model = EnergyLoss(13, 26.98)

    # assert model.compute_joy_luo1989(1.0) == approx(-167405.6897613208, abs=0.01)
    assert model.compute_joy_luo1989(10.0) == approx(-230075.2937567497, abs=0.01)
    assert model.compute_joy_luo1989(50.0) == approx(-226563.7595207261, abs=0.01)
    assert model.compute_joy_luo1989(200.0) == approx(-167405.6897613208, abs=0.01)
    assert model.compute_joy_luo1989(300.0) == approx(-144247.2503022708, abs=0.01)
    assert model.compute_joy_luo1989(1000.0) == approx(-79368.3510660936, abs=0.01)
    assert model.compute_joy_luo1989(10000.0) == approx(-16207.925895783, abs=0.01)
    assert model.compute_joy_luo1989(100000.0) == approx(-2487.0540175087, abs=0.01)


def test_compute_keV_g_cm2():
    model = EnergyLoss(13, 26.98)

    # assert model.compute_joy_luo1989(1.0) == approx(-167405.6897613208, abs=0.01)
    assert model.compute_keV_g_cm2(10.0) == approx(-230075.2937567497, abs=0.01)
    assert model.compute_keV_g_cm2(50.0) == approx(-226563.7595207261, abs=0.01)
    assert model.compute_keV_g_cm2(200.0) == approx(-167405.6897613208, abs=0.01)
    assert model.compute_keV_g_cm2(300.0) == approx(-144247.2503022708, abs=0.01)
    assert model.compute_keV_g_cm2(1000.0) == approx(-79368.3510660936, abs=0.01)
    assert model.compute_keV_g_cm2(10000.0) == approx(-16207.925895783, abs=0.01)
    assert model.compute_keV_g_cm2(100000.0) == approx(-2487.0540175087, abs=0.01)
