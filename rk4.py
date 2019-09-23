#!/usr/bin/env python3

import matplotlib.pyplot as plt
import math

PI = math.pi
g = 9.8 #m/s
l = 1.0 #m
x0 = 10.0  #sec
y0 = PI -0.0001   #0.0065 + 0.002  #PI/4.0 #radians
u0 = 0.0 #(PI/2.0)/90.0   #rad/sec
dx = 0.1 #sec
C = 0.9 #Constant of dumping

def f(x,y,u):
    return u

def F(x,y,u):
    return (-g/l)*math.sin(y) - C*u

x=x0
y=y0
u=u0

iterations = range(30000)
t=[x]
theta=[y]


for i in iterations:
    q1= dx*F(x,y,u)
    k1= dx*f(x,y,u)

    k2=dx*f(x+(dx/2.0),y+(k1/2.0),u+(q1/2.0))
    q2= dx*F(x+(dx/2.0),y+(k1/2.0),u+(q1 /2.0))

    k3=dx*f(x+(dx/2.0),y+(k2/2.0),u+(q2 /2.0))
    q3= dx*F(x+(dx/2.0),y+(k2/2.0),u+(q2 /2.0))

    k4= dx*f(x+dx,y+k3,u+q3)
    q4= dx*F(x+dx,y+k3,u+q3)

    x = x + dx
    y = y + (1.0/6.0)*(k1+(2.0*k2)+(2.0*k3)+k4)
    u = u + (1.0/6.0)*(q1+(2.0*q2)+(2.0*q3)+q4)

    t.append(x)
    theta.append(y)

fig, ax = plt.subplots()
ax.plot(t,theta,'*')
ax.set(xlabel='time [sec]', ylabel='$\theta$',
       title="Armonic Oscilator")
ax.grid()
plt.show()
