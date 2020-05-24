#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcbse.models.mean_free_path
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Mean free path model.
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


class MeanFreePath:
    def __init__(self, atomic_weight_g_mol, density_g_cm3):
        self.atomic_weight_g_mol = atomic_weight_g_mol
        self.density_g_cm3 = density_g_cm3
        self.avogadro_number_1_mol = 6.02214076e23
        self.nm2cm = 1.0e-7
        self.cm2nm = 1.0e7

    def compute_nm(self, sigma_nm2):
        sigma_cm2 = sigma_nm2 * self.nm2cm * self.nm2cm
        value_cm = self.atomic_weight_g_mol / (self.avogadro_number_1_mol * self.density_g_cm3 * sigma_cm2)
        value_nm = value_cm * self.cm2nm
        return value_nm

    def step_nm(self, mfp_nm, random_number):
        assert random_number >= 0.0
        assert random_number < 1.0

        value = -1.0 * mfp_nm * math.log(1.0 - random_number)
        return value
