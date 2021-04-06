#!/usr/bin/python
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
fp=open('/home/rachanareddy/Documents/contiki-2.7-sensors/src/examples/sensors-general/soundtry.txt','r')
line=fp.readline()
sums=0
s0=[]
s1=[]
while line:
	line=line.split()
	x=line[0]
	line.pop(0)
	y=line[0]
	line.pop(0)
	for i in range(len(line)):
			line[i]=int(line[i])
	numsum=(sum(line)/70.0)
	for i in range(len(line)):
		sums+=pow((line[i]-numsum),2)
	s0.append(sqrt(sums/len(line)))
	z=(1000*x+2*y)
	s1.append(z)
	line=fp.readline()
plt.plot(s0,s1)
plt.show()
'''fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.scatter(s0,s1,color='red')
plt.tight_layout()
fig=plt.gcf()
plt.show()'''	
fp.close()
