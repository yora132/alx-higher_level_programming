#!/usr/bin/python3
import sys
add = 0
for i in range(len(sys.argv) - 1):
    add += int(sys.argv[i + 1])
print("{}".format(add))
