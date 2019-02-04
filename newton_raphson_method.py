import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    def function(x):
        return x**2-2 # The main function
    def derivative(x):
        return 2*x # The derivative of the main function

def newton(function, derivative, x0, tolerance, number_of_max_iterations=100):
    x1 = 0

    if abs(x0-x1)<= tolerance and abs((x0-x1)/x0)<= tolerance:
        return x0

    print("k\t x0\t\t function(x0)")
    k = 1

    while k <= number_of_max_iterations:
        x1 = x0 - (function(x0)/derivative(x0))
        print("x%d\t%e\t%e"%(k,x1,function(x1)))

        if abs(x0-x1)<= tolerance and abs((x0-x1)/x0)<= tolerance:
            plt.plot(x0, function(x0), 'or')
            return x1

        x0 = x1
        k = k + 1
        plt.plot(x0, function(x0), 'or')

        # Stops the method if it hits the number of maximum iterations
        if k > number_of_max_iterations:
            print("ERROR: Exceeded max number of iterations")

    return x1 # Returns the value

sqrt = newton(function, derivative, 1.7, 0.0000001)
print("The approximate value of x is: "+str(sqrt))

# Plotting configuration
u = np.arange(1.0, 2.0, 0.0001) # Setting up values for x in the plot
w = u**2 - 2 # Define the main function again

plt.plot(u, w)
plt.axhline(y=0.0, color='black', linestyle='-')
plt.title('Newton-Raphson Graphics for' + ' y = x^2 - 2')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend(['Xn'], loc='upper left')
plt.show()
