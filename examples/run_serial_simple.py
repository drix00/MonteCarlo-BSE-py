#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: run_serial_simple
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Run the sets of simulations on the serial and simple program.
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
import time
import csv

# Third party modules.

# Local modules.

# Project modules.
from mcbse.inputs import Input
from mcbse.inputs.element import Element
from mcbse.simulation.simulation import Simulation
from mcbse.models.random_seed import RandomSeed

# Globals and constants variables.


def simulate_number_trajectories_repetitions(suffix):
    number_repetitions = 10
    initial_energy_eV = 10.e3
    list_number_trajectories = [10, 100, 1000, 10000, 100000, 1000000]

    rows = []
    row = []
    row.append("atomic number")
    row.append("initial energy eV")
    row.append("number trajectories")
    row.append("repetition id")
    row.append("bse")
    row.append("bse variance")
    row.append("bse std")
    row.append("te")
    row.append("te variance")
    row.append("te std")
    row.append("elapse time s")
    rows.append(row)

    for number_trajectories in list_number_trajectories:
        for repetition_id in range(1, number_repetitions+1):
            element = Element(29)
            inputs = Input(element, initial_energy_eV, number_trajectories)
            rand_seed = RandomSeed()
            simulation = Simulation(inputs, rand_seed())

            simulation.do_simulation()

            row = []
            row.append(element.atomic_number)
            row.append(initial_energy_eV)
            row.append(number_trajectories)
            row.append(repetition_id)
            row.append(simulation.bse.mean)
            row.append(simulation.bse.variance)
            row.append(simulation.bse.standard_deviation)
            row.append(simulation.te.mean)
            row.append(simulation.te.variance)
            row.append(simulation.te.standard_deviation)
            row.append(simulation.elapse_time_s)
            rows.append(row)

    file_name = "simulate_number_trajectories_repetitions" + suffix + ".csv"
    with open(file_name, 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(rows)


def simulate_elements_energies(suffix):
    repetition_id = 1
    number_trajectories = 1000000
    energies_keV = [1.0, 2.0, 3.0, 4.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0, 60.0]
    elements = [Element(6), Element(13), Element(14), Element(26), Element(29), Element(47), Element(79)]

    rows = []
    row = []
    row.append("atomic number")
    row.append("initial energy eV")
    row.append("number trajectories")
    row.append("repetition id")
    row.append("bse")
    row.append("bse variance")
    row.append("bse std")
    row.append("te")
    row.append("te variance")
    row.append("te std")
    row.append("elapse time s")
    rows.append(row)

    for element in elements:
        for energy_keV in energies_keV:
            initial_energy_eV = energy_keV * 1.0e3
            inputs = Input(element, initial_energy_eV, number_trajectories)
            rand_seed = RandomSeed()
            simulation = Simulation(inputs, rand_seed())

            simulation.do_simulation()

            row = []
            row.append(element.atomic_number)
            row.append(initial_energy_eV)
            row.append(number_trajectories)
            row.append(repetition_id)
            row.append(simulation.bse.mean)
            row.append(simulation.bse.variance)
            row.append(simulation.bse.standard_deviation)
            row.append(simulation.te.mean)
            row.append(simulation.te.variance)
            row.append(simulation.te.standard_deviation)
            row.append(simulation.elapse_time_s)
            rows.append(row)

    file_name = "simulate_elements_energies" + suffix + ".csv"
    with open(file_name, 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(rows)


def simulate_atomic_numbers(suffix):
    repetition_id = 1
    initial_energy_eV = 15.e3
    number_trajectories = 1000000

    rows = []
    row = []
    row.append("atomic number")
    row.append("initial energy eV")
    row.append("number trajectories")
    row.append("repetition id")
    row.append("bse")
    row.append("bse variance")
    row.append("bse std")
    row.append("te")
    row.append("te variance")
    row.append("te std")
    row.append("elapse time s")
    rows.append(row)

    for atomic_number in range(1, 96+1):
        element = Element(atomic_number)
        inputs = Input(element, initial_energy_eV, number_trajectories)
        rand_seed = RandomSeed()
        simulation = Simulation(inputs, rand_seed())

        simulation.do_simulation()

        row = []
        row.append(element.atomic_number)
        row.append(initial_energy_eV)
        row.append(number_trajectories)
        row.append(repetition_id)
        row.append(simulation.bse.mean)
        row.append(simulation.bse.variance)
        row.append(simulation.bse.standard_deviation)
        row.append(simulation.te.mean)
        row.append(simulation.te.variance)
        row.append(simulation.te.standard_deviation)
        row.append(simulation.elapse_time_s)
        rows.append(row)

    file_name = "simulate_atomic_numbers" + suffix + ".csv"
    with open(file_name, 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(rows)


def simulate_densities(suffix):
    number_repetitions = 10
    initial_energy_eV = 15.e3
    number_trajectories = 1000000
    densities_g_cm3 = [0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 8.96, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0,
                       20.0, 30.0, 40.0, 50.0]

    rows = []
    row = []
    row.append("atomic number")
    row.append("density (g/cm3)")
    row.append("initial energy eV")
    row.append("number trajectories")
    row.append("repetition id")
    row.append("bse")
    row.append("bse variance")
    row.append("bse std")
    row.append("te")
    row.append("te variance")
    row.append("te std")
    row.append("elapse time s")
    rows.append(row)

    for density_g_cm3 in densities_g_cm3:
        for repetition_id in range(1, number_repetitions+1):
            element = Element(29)
            element.density_g_cm3 = density_g_cm3
            inputs = Input(element, initial_energy_eV, number_trajectories)
            rand_seed = RandomSeed()
            simulation = Simulation(inputs, rand_seed())

            simulation.do_simulation()

            row = []
            row.append(element.atomic_number)
            row.append(element.density_g_cm3)
            row.append(initial_energy_eV)
            row.append(number_trajectories)
            row.append(repetition_id)
            row.append(simulation.bse.mean)
            row.append(simulation.bse.variance)
            row.append(simulation.bse.standard_deviation)
            row.append(simulation.te.mean)
            row.append(simulation.te.variance)
            row.append(simulation.te.standard_deviation)
            row.append(simulation.elapse_time_s)
            rows.append(row)

    file_name = "simulate_densities" + suffix + ".csv"
    with open(file_name, 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(rows)


def simulate_thickness(suffix):
    repetition_id = 1
    initial_energy_eV = 15.e3
    number_trajectories = 1000000
    elements = [Element(6), Element(13), Element(14), Element(26), Element(29), Element(47), Element(79)]
    thicknesses_nm = [5.0, 10.0, 20.0, 30.0, 40.0, 50.0, 100.0, 150.0, 200.0, 250.0, 500.0, 750.0, 1000.0, 1250.0,
                      1500.0, 1750.0, 2000.0, 2250.0, 2500.0, 3000.0, 4000.0, 5000.0]

    rows = []
    row = []
    row.append("atomic number")
    row.append("thickness (nm)")
    row.append("initial energy eV")
    row.append("number trajectories")
    row.append("repetition id")
    row.append("bse")
    row.append("bse variance")
    row.append("bse std")
    row.append("te")
    row.append("te variance")
    row.append("te std")
    row.append("elapse time s")
    rows.append(row)

    for element in elements:
        for thickness_nm in thicknesses_nm:
            inputs = Input(element, initial_energy_eV, number_trajectories)
            inputs.thickness_nm = thickness_nm
            rand_seed = RandomSeed()
            simulation = Simulation(inputs, rand_seed())

            simulation.do_simulation()

            row = []
            row.append(element.atomic_number)
            row.append(inputs.thickness_nm)
            row.append(initial_energy_eV)
            row.append(number_trajectories)
            row.append(repetition_id)
            row.append(simulation.bse.mean)
            row.append(simulation.bse.variance)
            row.append(simulation.bse.standard_deviation)
            row.append(simulation.te.mean)
            row.append(simulation.te.variance)
            row.append(simulation.te.standard_deviation)
            row.append(simulation.elapse_time_s)
            rows.append(row)

    file_name = "simulate_thickness" + suffix + ".csv"
    with open(file_name, 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(rows)


def main():
    suffix = time.strftime("_%Y%m%d_%H%M%S", time.localtime())

    simulate_number_trajectories_repetitions(suffix)
    simulate_elements_energies(suffix)
    simulate_atomic_numbers(suffix)
    simulate_densities(suffix)
    simulate_thickness(suffix)


if __name__ == '__main__':
    main()
