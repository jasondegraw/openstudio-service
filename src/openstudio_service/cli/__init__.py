# SPDX-FileCopyrightText: 2024-present Jason W. DeGraw <jason.degraw@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause
import click
import openstudio_service as oss

from ..__about__ import __version__


@click.command()
@click.option('-o', '--openstudio', show_default=True, default='openstudio', help='openstudio CLI executable to use.')
def dev(openstudio):
    """
    Run the dev app.
    """
    config = {
        'OPENSTUDIO': openstudio
    }
    app = oss.create_app(config=config)
    app.run(host='127.0.0.1', port=5000, debug=True)

@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=False)
@click.version_option(version=__version__, prog_name='openstudio-service')
@click.pass_context
def openstudio_service(ctx: click.Context):
    pass

openstudio_service.add_command(dev)