import numpy as np

x = np.array(([1,2,3],[4,5,6]))
print("matrik x")
print(x)

y = np.array(([2],[4],[6]))
print("matrik y")
print(y)

#perkaliaan matrik
#cara pertama
z1=np.dot(x,y)
print("matrik z1")
print(z1)

#cara kedua
z2=x.dot(y)
print("matrik z2")
print(z2)