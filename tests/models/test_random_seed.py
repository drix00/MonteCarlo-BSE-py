#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.models.test_random_seed
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the :py:mod:`mcbse.models.random_seed` module.
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

# Local modules.

# Project modules.
from mcbse.models.random_seed import RandomSeed

# Globals and constants variables.


def test_is_discovered():
    """
    Test used to validate the file is included in the tests
    by the test framework.
    """
    # assert False
    assert True


def test_random_seed():
    rand_seed = RandomSeed()

    seed1 = rand_seed()
    seed2 = rand_seed()
    seed3 = rand_seed()
    seed4 = rand_seed()
    seed5 = rand_seed()
    seed6 = rand_seed()
    seed7 = rand_seed()
    seed8 = rand_seed()
    seed9 = rand_seed()
    seed10 = rand_seed()

    assert seed1 != seed2
    assert seed1 != seed3
    assert seed1 != seed4
    assert seed1 != seed5
    assert seed1 != seed6
    assert seed1 != seed7
    assert seed1 != seed8
    assert seed1 != seed9
    assert seed1 != seed10

    assert seed2 != seed3
    assert seed2 != seed4
    assert seed2 != seed5
    assert seed2 != seed6
    assert seed2 != seed7
    assert seed2 != seed8
    assert seed2 != seed9
    assert seed2 != seed10

    assert seed3 != seed4
    assert seed3 != seed5
    assert seed3 != seed6
    assert seed3 != seed7
    assert seed3 != seed8
    assert seed3 != seed9
    assert seed3 != seed10

    assert seed4 != seed5
    assert seed4 != seed6
    assert seed4 != seed7
    assert seed4 != seed8
    assert seed4 != seed9
    assert seed4 != seed10

    assert seed5 != seed6
    assert seed5 != seed7
    assert seed5 != seed8
    assert seed5 != seed9
    assert seed5 != seed10

    assert seed6 != seed7
    assert seed6 != seed8
    assert seed6 != seed9
    assert seed6 != seed10

    assert seed7 != seed8
    assert seed7 != seed9
    assert seed7 != seed10

    assert seed8 != seed9
    assert seed8 != seed10

    assert seed9 != seed10
