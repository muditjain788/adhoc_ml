#!/usr/bin/python3
import numpy as np
x=np.random.random((3,2))
y=np.random.random((2,5))
a="array1"+" "+str(x)
b="array2"+" "+str(y)
print(x)
print(y)
f=open('x.txt','w')
f.write(a)
f.write(b)
