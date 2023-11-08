import random
import sys
import time

cur_time = str(time.time()).encode('ASCII')
random.seed(cur_time)

print(cur_time)