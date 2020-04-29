def derivative(f,x,h):
	return (f(x+h)-f(x))/h


def f(x):
	return x**5+17*x**2
def f_d(x):
	return 5*x**4+34*x

import matplotlib.pyplot as plt


plt.plot([i for i in range(10)],[f_d(0)-derivative(f,0,0.1**i) for i in range(10)])
plt.show()
