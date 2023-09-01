# to compile --> python3 my_program.py

#======== Calculate derivatives in Python ===============
import sympy as sym

x = sym.Symbol('x')     # Symbolize X
func= x**3+3*x-2        # Function
sym.Derivative(func, x) # Derivative expression.

sym.Derivative(func, x, evaluate=True) # Calculate derivative of func.
func.diff(x)    # Or use this for the same.

# Create functions with lambdify
expr= sym.lambdify(x, func) 
expr_der=sym.lambdify(x, func.diff(x))

print(f'value of func at x=5: {expr(5)}')
print(f'derivative of func at x=5: {expr_der(5)}')

#======== Visualize derivatives in Python ===============
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#values = np.linspace(-10, 10, 100) # Create values for the function
values = np.linspace(-10, 0, 100) # Create values for the function

#Plot the function
plt.plot(values, expr(values))

# Add points where we want to calculate derivative
x1=-5       
y1=expr(x1)

# Define x range for tangent line
xrange = np.linspace(x1-5, x1+5, 10)

# Define tangent line
# y = m*(x - x1) + y1
def line(x, x1, y1): return expr_der(x1)*(x - x1) + y1

# Add tangent and touching point
plt.plot(xrange, line(xrange, x1, y1), '--')
plt.scatter(x1, y1, s=50, c='C1');

# Display the plot
plt.grid(True)
plt.show()
