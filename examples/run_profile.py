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


def simulate_serial_simple(suffix):
    number_repetitions = 1
    initial_energy_eV = 10.e3
    number_trajectories = 10000

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

    file_name = "simulate_serial_simple" + suffix + ".csv"
    with open(file_name, 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(rows)


def main():
    suffix = time.strftime("_%Y%m%d_%H%M%S", time.localtime())

    start = time.time()
    simulate_serial_simple(suffix)
    end = time.time()
    print("Elapse time: {:.4f} s".format(end-start))


if __name__ == '__main__':
    main()
