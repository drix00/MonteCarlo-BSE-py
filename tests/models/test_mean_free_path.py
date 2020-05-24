#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.models.test_mean_free_path
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the :py:mod:`mcbse.models.mean_free_path` module.
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

# Third party modules.
from pytest import approx

# Local modules.

# Project modules.
from mcbse.models.rutherford import Rutherford
from mcbse.models.mean_free_path import MeanFreePath

# Globals and constants variables.


def test_is_discovered():
    """
    Test used to validate the file is included in the tests
    by the test framework.
    """
    # assert False
    assert True


def test_lambda():
    model = MeanFreePath(12.011, 2.62)
    model_cs = Rutherford(6)

    assert model.compute_nm(model_cs.compute_sigma_nm2(1000.0)) == approx(1.4784352041, rel=0.01)
    assert model.compute_nm(model_cs.compute_sigma_nm2(10000.0)) == approx(14.3837782086, rel=0.01)
    assert model.compute_nm(model_cs.compute_sigma_nm2(100000.0)) == approx(123.4571899308, rel=0.01)


def test_step():
    model = MeanFreePath(12.011, 2.62)
    model_cs = Rutherford(6)

    lambda_nm = model.compute_nm(model_cs.compute_sigma_nm2(10000.0))
    # assert model.step_nm(lambda_nm, 1.0) == approx(80.0, rel=0.01)
    assert model.step_nm(lambda_nm, 0.999) == approx(99.3596198521, rel=0.01)
    assert model.step_nm(lambda_nm, 0.5) == approx(9.9700753111, rel=0.01)
    assert model.step_nm(lambda_nm, 0.01) == approx(0.1445618018, rel=0.01)
    assert model.step_nm(lambda_nm, 0.0) == approx(0.0, rel=0.01)
