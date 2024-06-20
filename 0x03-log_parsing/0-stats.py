#!/usr/bin/python3
import sys


states = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                states[code] += 1
            size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(size))
            for key, value in sorted(states.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(size))
    for key, value in sorted(states.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
