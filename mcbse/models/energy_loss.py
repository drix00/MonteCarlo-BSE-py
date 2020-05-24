#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcbse.models.energy_loss
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Energy loss model.
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

# Local modules.

# Project modules.

# Globals and constants variables.


class EnergyLoss:
    def __init__(self, atomic_number, atomic_weight_g_mol):
        self.atomic_number = atomic_number
        self.atomic_weight_g_mol = atomic_weight_g_mol

    def compute_keV_g_cm2(self, energy_eV):
        value_keV_g_cm2 = self.compute_joy_luo1989(energy_eV)
        return value_keV_g_cm2

    def compute_bethe1930(self, energy_eV):
        energy_keV = energy_eV * 1.0e-3
        factor1 = -78500.0 * self.atomic_number / (self.atomic_weight_g_mol * energy_keV)
        J_keV = self.compute_mean_ionisation_potential_eV() * 1.0e-3
        factor2 = math.log(1.166 * energy_keV / J_keV)
        value = factor1 * factor2

        return value

    def compute_joy_luo1989(self, energy_eV):
        energy_keV = energy_eV * 1.0e-3
        factor1 = -78500.0 * self.atomic_number / (self.atomic_weight_g_mol * energy_keV)
        J_keV = self.compute_mean_ionisation_potential_eV() * 1.0e-3
        factor2 = math.log(1.166 * (energy_keV + 0.85 * J_keV) / J_keV)
        value = factor1 * factor2

        return value

    def compute_mean_ionisation_potential_eV(self):
        value = (9.76 * self.atomic_number + 58.5 / math.pow(self.atomic_number, 0.19))
        return value
