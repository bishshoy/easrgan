import numpy as np

s = 1.4

a = np.zeros([5,5])
k = 2

for i in range(5):
    for j in range(5):
            a[i,j] = (1/(2*np.pi*s*s)) * np.exp(-((i-k)**2 + (j-k)**2)/(2*s*s))

print(a)





































