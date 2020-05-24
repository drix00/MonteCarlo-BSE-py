#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcbse.models.direction_cosine
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Direction cosine model.
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


class DirectionCosine:
    def __init__(self, ca, cb, cc):
        self.ca = ca
        self.cb = cb
        self.cc = cc

        self.epsilon = 0.000001

    def compute(self, theta_rad, phi_rad):
        self.compute_joy1995(theta_rad, phi_rad)

    def compute_joy1995(self, theta_rad, phi_rad):
        cos_theta = math.cos(theta_rad)
        sin_theta = math.sin(theta_rad)

        cos_phi = math.cos(phi_rad)
        sin_phi = math.sin(phi_rad)

        cx = self.ca
        cy = self.cb
        cz = self.cc
        if cz == 0.0:
            cz = self.epsilon

        AN = -cx / cz
        AM = 1.0 / math.sqrt(1.0 + AN * AN)

        V1 = AM * sin_theta
        V2 = AN * AM * sin_theta
        V3 = cos_phi
        V4 = sin_phi

        self.ca = cx * cos_theta + V1 * V3 + cy * V2 * V4
        self.cb = cy * cos_theta + V4 * (cz * V1 - cx * V2)
        self.cc = cz * cos_theta + V2 * V3 - cy * V1 * V4
