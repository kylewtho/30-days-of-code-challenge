#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    arr_reverse = []
    
    for i in range(n):
        arr_reverse.append(str(arr.pop()))
    
    print(' '.join(arr_reverse))
