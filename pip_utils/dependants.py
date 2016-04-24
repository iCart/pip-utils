# -*- coding: utf-8 -*-
"""List dependants of package"""

# Python 2 forwards-compatibility
from __future__ import absolute_import, print_function

# standard imports
from site import ENABLE_USER_SITE

# external imports
from pip import get_installed_distributions


def command_dependants(options):
    """Command launched by CLI."""
    dependants = sorted(
        get_dependants(options.package.project_name),
        key=lambda n: n.lower()
    )

    if dependants:
        print(*dependants, sep='\n')


def get_dependants(project_name):
    """Yield dependants of indicated package name."""
    for package in get_installed_distributions(user_only=ENABLE_USER_SITE):
        for requirement_package in package.requires():
            requirement_name = requirement_package.project_name
            # perform case-insensitive matching
            if requirement_name.lower() == project_name.lower():
                yield package.project_name
