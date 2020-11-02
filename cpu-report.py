#!/usr/bin/env python

import psutil
import time

while True:
    print(f'Current CPU utilization: {psutil.cpu_percent()}')
    time.sleep(5)
