## import modules here 
import pandas as pd
import numpy as np



################# Question 1 #################

def v_opt_dp(x, num_bins):# do not change the heading of the function
    dp_matrix = [[-1 for i in range(len(x))] for j in range(num_bins)]
    dp_index = [[-1 for i in range(len(x))] for j in range(num_bins)]
    
    for i in range(num_bins):
        for j in range(len(x)):
            if (num_bins-i-j) >= 2 or len(x)-j <= i:
                continue
            if not i:
                dp_matrix[i][j] = sse(x[j:])
            else:
                min_val, min_index = float('inf'), -1
                for k in range(j, len(x)):
                    cost = sse(x[j:k+1])+dp_matrix[i-1][k+1] if (k+1)<=len(x)-1 else sse(x[j:k+1])
                    min_val = min(min_val, cost)
                    min_index = k if min_val == cost else min_index
                dp_matrix[i][j] = min_val
                dp_index[i][j] = min_index+1
    start, bins = dp_index[-1][0], []
    prev = start
    bins.append(x[0:start])
    for i in range(len(dp_index)-2, 0, -1):
        start = dp_index[i][start]
        bins.append(x[prev:start])
        prev = start
    bins.append(x[start:])
    return dp_matrix, bins

def sse(nums):
    if not len(nums):
        return 0
    avg = np.average(nums)
    result = sum([(x-avg)*(x-avg) for x in nums])
    return result
