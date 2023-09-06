import random
import math
import time

class Solution:
    def estimate_pi(n):
        start_time = time.perf_counter()
        num_pts_circle = 0
        num_pts_total = 0
    
        for i in range(n):

            x = random.uniform(0,1)
            y = random.uniform(0,1)
            distance = math.sqrt(x**2+y**2)
            if distance <= 1:
                num_pts_circle += 1
            num_pts_total += 1
     
        result = 4*num_pts_circle/num_pts_total
        end_time = time.perf_counter()
        return (result, end_time - start_time)

    result, runtime = estimate_pi(int(input("number of iterations: ")))

    if result != math.pi:
        error = (result-math.pi)/math.pi*100
        if error < 0:
            error = error*(-1)
    
    print(f"generated result: {result}\nliterature result: {math.pi}\nerror(%): {error}\nruntime(s): {runtime}")
