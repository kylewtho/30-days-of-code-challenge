#!/bin/python3

import math
import os
import random
import re
import sys

def find_max_sum(arr):
    curr_sum, max_sum = None, None
        
    for row in range(4):
        for col in range(4):
            curr_sum = sum((arr[row][col], arr[row][col+1], arr[row][col+2],
                            arr[row+1][col+1],
                            arr[row+2][col], arr[row+2][col+1], arr[row+2][col+2]))
            if max_sum is None:
                max_sum = curr_sum
            elif curr_sum > max_sum:
                max_sum = curr_sum
                
    return max_sum


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    print(find_max_sum(arr))

