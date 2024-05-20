# SPDX-FileCopyrightText: 2024-present Jason W. DeGraw <jason.degraw@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause
import os
import asyncio
import httpx
import time

script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)

osm_dir = os.path.join(script_dir, '..', 'resources')
osms = ['large-hotel-5A-2010-OS321.osm',
        'large-office-5A-2010-OS321.osm',
        'medium-office-5A-2010-OS321.osm',
        'small-office-5A-2010-OS321.osm',
        'primary-school-5A-2010-OS321.osm',
        'secondary-school-5A-2010-OS321.osm']
osm_files = [os.path.join(osm_dir, el) for el in osms]
epw_file = os.path.join(script_dir, '..', 'resources', 'USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw')

run_base_dir = os.path.join(script_dir, '..', 'run') # this one exists
run_dirs = [os.path.join(run_base_dir, '3%s'%el) for el in ['A', 'B', 'C', 'D', 'E', 'F']]
for el in run_dirs:
    os.mkdir(el)

data = [{'seed_file': osm, 'epw': epw_file, 'run_dir': dir} for osm,dir in zip(osm_files, run_dirs)]

async def run():
    async with httpx.AsyncClient() as client:
        tasks = [client.post('http://127.0.0.1:5000/run', data=inputs, timeout=None) for inputs in data]
        result = await asyncio.gather(*tasks)
        return result

start = time.time()
result = asyncio.run(run())
delta = time.time() - start

print('Done! (%s seconds)' % delta)
for el in result:
    print(el.status_code, el.text)