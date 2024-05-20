# SPDX-FileCopyrightText: 2024-present Jason W. DeGraw <jason.degraw@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause
import sys

if __name__ == '__main__':
    from .cli import openstudio_service

    sys.exit(openstudio_service())
