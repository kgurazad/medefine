import sys
from scipy import stats
import numpy as np
from scipy.optimize import curve_fit 
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
s = []
for x in range(1,len(sys.argv)):
    s.append(sys.argv[x])

sum = 0

for x in s:
    sum = sum + float(x)

print(sum/(len(sys.argv)-1))

c = []
for x in range(1,len(sys.argv)):
    c.append(x)

plt.plot(c,s)
plt.xlabel('#Report')
plt.ylabel('Symptom Score')
plt.savefig('/home/karangurazada/medefine/foo.png', bbox_inches='tight')
