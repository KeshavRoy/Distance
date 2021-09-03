import numpy as np
import matplotlib.pyplot as plt
import math
from line.funcs import *

#if using termux
import subprocess
import shlex
#end if

x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))
print(type(x1)) 
a = (math.cos(math.pi/3))
print(a)
d =((((x2-x1)**2 + (y2-y1)**2 )+ 2 * ((x2-x1) * (y2-y1) * a  )))**0.5
print(d)
#Triangle vertices
A = np.array([x1,y1])
B= np.array([x2,y2])
#Generating lines
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.02), B[1] * (1) , 'B')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.show()
