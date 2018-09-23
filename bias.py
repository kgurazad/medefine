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
sys.stderr.write((sum/(len(sys.argv)-1)) + " <- bias")
sys.stderr.write("finished bias!\n")
c = []

for x in range(1, len(sys.argv)):
    c.append(x)

slope, intercept, r_value, p_value, std_err= stats.linregress(c,s)

def fit_func(x, a, b, c, d):
    return a*x*x*x+b*x*x+c*x+d
params = curve_fit(fit_func, c, s)
[a, b, c, d, e, f, g, h, i, j, k, l, m] = params[0]
def predict_next(a, b, c, d):
    x = len(sys.argv)
    return a*x*x*x+b*x*x+c*x+d
plt.plot(c,s)
savefig('foo.jpg')
