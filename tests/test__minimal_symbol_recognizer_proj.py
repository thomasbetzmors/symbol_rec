#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `_minimal_symbol_recognizer_proj` package."""

# Third party modules
import pytest

# First party modules
import _minimal_symbol_recognizer_proj


def test_version():
    assert _minimal_symbol_recognizer_proj.__version__.count(".") == 2


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
