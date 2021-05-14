#!/usr/bin/env python3

import psutil
import time

from swsscommon import swsscommon

start_time = time.time()

ws = swsscommon.WarmStart()
ws.initialize('cpu-report', 'cpu-report')
is_warm_start = ws.checkWarmStart('cpu-report', 'cpu-report')

if is_warm_start:
    ws.setWarmStartState('cpu-report', ws.INITIALIZED)
else:
    ws.setWarmStartState('cpu-report', ws.WSDISABLED)


while True:
    print(f'Current CPU utilization: {psutil.cpu_percent()}')
    time.sleep(5)
    if is_warm_start and (time.time() - start_time) > 15:
        ws.setWarmStartState('cpu-report', ws.RECONCILED)

