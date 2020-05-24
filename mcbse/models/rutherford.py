#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcbse.models.rutherford
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Rutherford cross section model.
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


class Rutherford:
    def __init__(self, atomic_number):
        self.atomic_number = atomic_number
        self.cm2nm = 1.0e7

    def compute_alpha(self, energy_eV):
        energy_keV = energy_eV * 1.0e-3

        alpha = 3.4e-3 * math.pow(self.atomic_number, 0.67) / energy_keV

        return alpha

    def compute_sigma_nm2(self, energy_eV):
        energy_keV = energy_eV * 1.0e-3

        nominator = 5.21e-21 * self.cm2nm * self.cm2nm * (self.atomic_number * self.atomic_number)
        denominator = (energy_keV * energy_keV)
        factor1 = nominator / denominator

        alpha = self.compute_alpha(energy_eV)
        factor2 = 4.0 * math.pi / (alpha * (1.0 + alpha))
        factor3 = (energy_keV + 511.0) / (energy_keV + 1024.0)

        value_nm2 = factor1 * factor2 * factor3 * factor3
        return value_nm2

    def compute_scattering_angle_rad(self, energy_eV, random_number):
        alpha = self.compute_alpha(energy_eV)
        nominator = 2.0 * alpha * random_number
        denominator = 1.0 + alpha - random_number
        cos_theta = 1.0 - nominator / denominator
        theta_rad = math.acos(cos_theta)

        return theta_rad

    def compute_azimuthal_angle_rad(self, random_number):
        value = 2.0 * math.pi * random_number
        return value
