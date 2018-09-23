import sys
from scipy import stats
s = []
for x in range(1,len(sys.argv)):
    s.append(sys.argv[x])

sum = 0

for x in s:
    sum = sum + x

print(sum/(len(sys.argv)-1))

c = []

for x in range(1, len(sys.argv)):
    c.append(x)

slope, intercept, r_value, p_value, std_err= stats.linregress(c,s)


