import sys
from scipy import stats
import numpy as np
from scipy.optimize import curve_fit 
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
sys.stderr.write("started bias!\n")
s = []
for x in range(1,len(sys.argv)):
    s.append(sys.argv[x])

sum = 0

for x in s:
    sum = sum + int(float(x))

print(sum/(len(sys.argv)-1))
sys.stderr.write(str(sum/(len(sys.argv)-1)) + " <- bias")
sys.stderr.write("finished bias!\n")
