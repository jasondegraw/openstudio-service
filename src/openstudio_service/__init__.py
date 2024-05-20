# SPDX-FileCopyrightText: 2024-present Jason W. DeGraw <jason.degraw@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause
from flask import Flask, request
import os
import subprocess
import json

from .__about__ import __version__

def create_app(config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        OPENSTUDIO='openstudio',
    )

    app.config.from_prefixed_env()

    if config is not None:
        app.config.from_mapping(config)
    
    @app.route('/run', methods=['POST'])
    def run_route():
        # POST request
        seed_file = request.form.get('seed_file')
        epw = request.form.get('epw')
        run_dir = request.form.get('run_dir')
        osw = {
            'seed_file': seed_file,
            'steps': [],
            'weather_file': epw
        }
        print(os.path.exists(seed_file))
        print(os.path.exists(epw))
        print(os.path.exists(run_dir))
        print(run_dir)
        with open(os.path.join(run_dir, 'run.osw'), 'w') as output:
            json.dump(osw, output, indent=4)
        with open(os.path.join(run_dir, 'output.txt'), 'w') as output:
            #print([app.config['OPENSTUDIO'], 'run', '--show-stdout', '-w', 'run.osw'])
            subprocess.run([app.config['OPENSTUDIO'], 'run', '-w', 'run.osw'], cwd=run_dir, stdout=output, stderr=subprocess.STDOUT)
        return run_dir

    return app