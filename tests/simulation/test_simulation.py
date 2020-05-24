#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.simulation.test_simulation
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the :py:mod:`mcbse.simulation.simulation` module.
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
from mcbse.inputs import Input
from mcbse.inputs.element import Element
from mcbse.simulation.simulation import Simulation
from mcbse.models.random_number import RandomNumber
from mcbse.models.random_seed import RandomSeed
from tests import slow_test

# Globals and constants variables.


def test_is_discovered():
    """
    Test used to validate the file is included in the tests
    by the test framework.
    """
    # assert False
    assert True


@slow_test
def test_do_simulation_carbon():  # pragma: no cover
    number_trajectories = 1000
    initial_energy_eV = 10.0e3
    inputs = Input(Element(6), initial_energy_eV, number_trajectories)
    simulation = Simulation(inputs, RandomNumber.magic_seed)

    simulation.do_simulation()

    tolerance = 0.0001
    assert simulation.bse.counts == number_trajectories
    assert simulation.bse.mean == approx(0.060, abs=tolerance)
    assert simulation.bse.standard_deviation == approx(0.0075099933422074355, abs=tolerance)
    assert simulation.te.counts == number_trajectories
    assert simulation.te.mean == approx(0.0, abs=tolerance)
    assert simulation.te.standard_deviation == approx(0.0, abs=tolerance)
    assert simulation.elapse_time_s < 20.0


def test_do_simulation_carbon_thin_film():
    number_trajectories = 1000
    initial_energy_eV = 10.0e3
    inputs = Input(Element(6), initial_energy_eV, number_trajectories)
    inputs.thickness_nm = 300.0
    simulation = Simulation(inputs, RandomNumber.magic_seed)

    simulation.do_simulation()

    tolerance = 0.0001
    assert simulation.bse.counts == number_trajectories
    assert simulation.bse.mean == approx(0.039, abs=tolerance)
    assert simulation.bse.standard_deviation == approx(0.006122009474020765, abs=tolerance)
    assert simulation.te.counts == number_trajectories
    assert simulation.te.mean == approx(0.94, abs=tolerance)
    assert simulation.te.standard_deviation == approx(0.0075099933422074355, abs=tolerance)
    assert simulation.elapse_time_s < 5.0


def test_do_simulation_carbon_very_thin_film():
    number_trajectories = 1000
    initial_energy_eV = 10.0e3
    inputs = Input(Element(6), initial_energy_eV, number_trajectories)
    inputs.thickness_nm = 1.0
    simulation = Simulation(inputs, RandomNumber.magic_seed)

    simulation.do_simulation()

    tolerance = 0.0001
    assert simulation.bse.counts == number_trajectories
    assert simulation.bse.mean == approx(0.001, abs=tolerance)
    assert simulation.bse.standard_deviation == approx(0.0009994998749374609, abs=tolerance)
    assert simulation.te.counts == number_trajectories
    assert simulation.te.mean == approx(0.999, abs=tolerance)
    assert simulation.te.standard_deviation == approx(0.000999499874937447, abs=tolerance)
    assert simulation.elapse_time_s < 5.0


@slow_test
def test_do_simulation_random_seed():  # pragma: no cover
    number_trajectories = 1000
    initial_energy_eV = 10.0e3
    inputs = Input(Element(29), initial_energy_eV, number_trajectories)

    rand_seed = RandomSeed()

    simulation1 = Simulation(inputs, rand_seed())
    simulation1.do_simulation()

    simulation2 = Simulation(inputs, rand_seed())
    simulation2.do_simulation()

    simulation3 = Simulation(inputs, rand_seed())
    simulation3.do_simulation()

    simulation4 = Simulation(inputs, rand_seed())
    simulation4.do_simulation()

    simulation5 = Simulation(inputs, rand_seed())
    simulation5.do_simulation()

    tolerance = 0.0001
    assert simulation1.bse.mean != approx(simulation2.bse.mean, abs=tolerance)
    assert simulation1.bse.mean != approx(simulation3.bse.mean, abs=tolerance)
    assert simulation1.bse.mean != approx(simulation4.bse.mean, abs=tolerance)
    assert simulation1.bse.mean != approx(simulation5.bse.mean, abs=tolerance)

    assert simulation2.bse.mean != approx(simulation3.bse.mean, abs=tolerance)
    assert simulation2.bse.mean != approx(simulation4.bse.mean, abs=tolerance)
    assert simulation2.bse.mean != approx(simulation5.bse.mean, abs=tolerance)

    assert simulation3.bse.mean != approx(simulation4.bse.mean, abs=tolerance)
    assert simulation3.bse.mean != approx(simulation5.bse.mean, abs=tolerance)

    assert simulation4.bse.mean != approx(simulation5.bse.mean, abs=tolerance)
