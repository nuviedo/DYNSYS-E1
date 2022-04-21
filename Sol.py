"""
DYNSYS-E1: Dynamic Systems | Flow in a bidimensional Torus.
Copyright (C) 2022 Alexis H. Nuviedo A.
https://github.com/nuviedo/DYNSYS-E1

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import numpy as np
import matplotlib.pyplot as plt

a=2/3   #Alpha Constant
x=0     #Initial coordinates
y=0
t=np.arange(0,30,1/1000) #Resolution of t [0,30]

#Initialize figure for plotting
fig = plt.Figure()
ax = fig.add_axes([0, 0, 1,1])
ax=plt.subplot()

def Flow(x,y):  #Define function as present in 
    global a,t  #Example 1.1 (Flow on a Torus)
    return (x+t)%1,(y+a*t)%1

#Evaluate over the domain
X,Y=Flow(x,y)

#Plot & display the resulting figure
ax.set_aspect(1)
ax.scatter(X,Y,s=.5,color=(1,0,0))

plt.savefig(f"FLOW.{a:.02f}.png")
plt.show()
