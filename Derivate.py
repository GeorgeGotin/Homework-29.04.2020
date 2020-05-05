import math as m

def derivative(f,x,h):
	return (f(x+h)-f(x))/h


def f1(x):
	return x**5+17*x**2
def f1_d(x):
	return 5*x**4+34*x
	
def f2(x):
	return m.sin(x)*m.cos(x)

def f2_d(x):
	return (m.cos(x))**2-(m.sin(x))**2

def f3(x):
	return x+m.sin(x)+m.exp(x)

def f3_d(x):
	return 1+m.cos(x)+m.exp(x)

import matplotlib.pyplot as plt


fs=[[f1,f1_d,'x^5+17*x^2'],[f2,f2_d,'sin(x)*cos(x)'],[f3,f3_d,'x+sin(x)+e^x']]
fig = plt.figure()
a=[]
print('Input x, please:',end='')
xs = int(input())
for i in range(3):
	a.append(fig.add_subplot(1,3,i+1))
	x = [j for j in range(20)]
	y = [fs[i][1](xs)-derivative(fs[i][0],xs,0.1**j) for j in range(20)]
	a[i].grid(axis='both')
	a[i].set_title(fs[i][2])
	a[i].plot(x,y)

plt.show()

