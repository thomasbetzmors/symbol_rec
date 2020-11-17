#!/usr/bin/env python

# Third party modules
import click

# First party modules
import _minimal_symbol_recognizer_proj


@click.group()
@click.version_option(version=_minimal_symbol_recognizer_proj.__version__)
def entry_point():
    """Awesomeproject spreads pure awesomeness."""
