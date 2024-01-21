#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    n_bin = str(bin(n))
    count, count_max = 0, 0
    
for char in n_bin:
    if char == '1':
        count += 1
    else:
        if count > count_max:
            count_max = count
        count = 0
        
if count > count_max:
    count_max = count
    
print(count_max)
