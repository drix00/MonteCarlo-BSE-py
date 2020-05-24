#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcbse.simulation.simulation
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Monte Carlo simulation of electron trajectories.
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

# Third party modules.

# Local modules.

# Project modules.
from mcbse.results.counter import Counter
from mcbse.models.energy_loss import EnergyLoss
from mcbse.models.mean_free_path import MeanFreePath
from mcbse.models.rutherford import Rutherford
from mcbse.models.random_number import RandomNumber
from mcbse.models.direction_cosine import DirectionCosine

# Globals and constants variables.


class Simulation:
    def __init__(self, inputs, seed):
        self.inputs = inputs
        self.bse = Counter()
        self.te = Counter()

        self.energy_loss = EnergyLoss(inputs.element.atomic_number, inputs.element.atomic_weight_g_mol)
        self.mean_free_path = MeanFreePath(inputs.element.atomic_weight_g_mol, inputs.element.density_g_cm3)
        self.cross_section = Rutherford(inputs.element.atomic_number)
        self.random_number = RandomNumber(seed)

        self.elapse_time_s = 0.0
        self.nm2cm = 1.0e-7
        self.keV2eV = 1.0e3

    def do_simulation(self):
        start_time = time.time()

        minimum_energy_eV = 50.0

        for trajectory_id in range(self.inputs.number_trajectories):
            direction = DirectionCosine(0.0, 0.0, -1.0)
            energy_eV = self.inputs.initial_energy_eV
            x = 0.0
            y = 0.0
            z = 0.0

            sigma_nm2 = self.cross_section.compute_sigma_nm2(energy_eV)
            mfp_nm = self.mean_free_path.compute_nm(sigma_nm2)
            step_nm = self.mean_free_path.step_nm(mfp_nm, self.random_number())

            theta_rad = 0.0
            phi_rad = 0.0
            direction.compute(theta_rad, phi_rad)

            factor1 = self.nm2cm * self.inputs.element.density_g_cm3 * self.keV2eV
            delta_energy_eV = step_nm * self.energy_loss.compute_keV_g_cm2(energy_eV) * factor1
            energy_eV += delta_energy_eV

            x += step_nm * direction.ca
            y += step_nm * direction.cb
            z += step_nm * direction.cc

            if z < -self.inputs.thickness_nm:
                self.bse.add_value(0.0)
                self.te.add_value(1.0)
                continue

            while energy_eV > minimum_energy_eV:
                sigma_nm2 = self.cross_section.compute_sigma_nm2(energy_eV)
                mfp_nm = self.mean_free_path.compute_nm(sigma_nm2)
                step_nm = self.mean_free_path.step_nm(mfp_nm, self.random_number())

                theta_rad = self.cross_section.compute_scattering_angle_rad(energy_eV, self.random_number())
                phi_rad = self.cross_section.compute_azimuthal_angle_rad(self.random_number())
                direction.compute(theta_rad, phi_rad)

                factor1 = self.nm2cm * self.inputs.element.density_g_cm3 * self.keV2eV
                delta_energy_eV = step_nm * self.energy_loss.compute_keV_g_cm2(energy_eV) * factor1
                energy_eV += delta_energy_eV

                x += step_nm * direction.ca
                y += step_nm * direction.cb
                z += step_nm * direction.cc

                if z > 0.0:  # pragma: no branch
                    self.bse.add_value(1.0)
                    self.te.add_value(0.0)
                    break

                if z < -self.inputs.thickness_nm:  # pragma: no branch
                    self.bse.add_value(0.0)
                    self.te.add_value(1.0)
                    break

            if z <= 0.0 and z >= -self.inputs.thickness_nm:
                self.bse.add_value(0.0)
                self.te.add_value(0.0)

        end_time = time.time()
        self.elapse_time_s = end_time - start_time
