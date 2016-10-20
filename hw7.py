## Dan Smilowitz 
## DATA 602 hw7


## Take what you did on homework 5 as a starting point.  Replace the regression
## calculation using least squares with a curve fitting approach.
## To start, just fit a linear equation.  Output the equation to the console.

# data for regressions
import pandas as pd
brain_body = pd.read_csv('data/brainandbody.csv')
br = brain_body['brain']
bo = brain_body['body']

# regression from hw5
def hw5_regression(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(x * x)
    sum_y = sum(y)
    sum_xy = sum(x * y)
    a = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x * sum_x)
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
    eq = 'y = %.3f + %.3f * x' % (a, b)
    return eq

# regressions using SciPy
from scipy.optimize import curve_fit
from scipy import stats

def linear_func(x, a, b):
    return a + b * x

def scipy_curve(x, y):
    c = curve_fit(linear_func, br, bo)
    eq = 'y = %.3f + %.3f * x' % (c[0][0], c[0][1])
    return eq

def scipy_linreg(x, y):
    l = stats.linregress(x, y)
    eq = 'y = %.3f + %.3f * x' % (l.intercept, l.slope)
    return eq


## Using timeit, compare the performance of your solution in homework 5 to the scipy function
my_setup = '''
import pandas as pd
brain_body = pd.read_csv('data/brainandbody.csv')
br = brain_body['brain']
bo = brain_body['body']

def hw5_regression(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(x * x)
    sum_y = sum(y)
    sum_xy = sum(x * y)
    a = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x * sum_x)
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
    eq = 'y = %.3f + %.3f * x' % (a, b)
    return eq

from scipy.optimize import curve_fit
from scipy import stats

def linear_func(x, a, b):
    return a + b * x

def scipy_curve(x, y):
    c = curve_fit(linear_func, br, bo)
    eq = 'y = %.3f + %.3f * x' % (c[0][0], c[0][1])
    return eq

def scipy_linreg(x, y):
    l = stats.linregress(x, y)
    eq = 'y = %.3f + %.3f * x' % (l.intercept, l.slope)
    return eq
'''


## Try to fit other equations to the data.  Output the equation to the console.

# fit quadratic equation
def quad_func(x, a, b, c):
    return a * x**2 + b*x + c

def fit_quad(x, y):
    quad = curve_fit(quad_func, x, y)
    eq = 'y = %.3f * x^2 + %.3f * x + %.3f' %(quad[0][0], quad[0][1], quad[0][2])
    return eq

# fit Gaussian equation
from numpy import exp
def gauss_func(x, a, b, c):
    return a*exp(-(x-b)**2/(2*c**2))

def fit_gauss(x, y):
    gauss = curve_fit(gauss_func, x, y)
    eq = '''                  _                 _
                     |  -(x - %.3f)^2   |
    y = %.3f * exp | ----------------- |
                     |_  2 * %.3f^2   _|
    ''' %(gauss[0][0], gauss[0][1], gauss[0][2])
    return eq



if __name__ == "__main__":
    import timeit
    x = 1000
    my_reg = hw5_regression(br, bo)
    my_reg_time = timeit.timeit('hw5_regression(br, bo)', setup = my_setup, number = x)
    curve_reg = scipy_curve(br, bo)
    curve_reg_time = timeit.timeit('scipy_curve(br, bo)', setup = my_setup, number = x)
    stat_reg = scipy_linreg(br, bo)
    stat_reg_time = timeit.timeit('scipy_linreg(br, bo)', setup = my_setup, number = x)
    
    print '''
    -----------------------------------------------------
    Execution Times and Results (%d iterations):
    -----------------------------------------------------

    Hand-coded:
      Equation: %s
      Time: %.4f s

    SciPy optimize:
      Equation: %s
      Time: %.4f s

    SciPy stats.linreg:
      Equation: %s
      Time: %.4f s
    
    -----------------------------------------------------
    ''' %(x, my_reg, my_reg_time, curve_reg, curve_reg_time, stat_reg, stat_reg_time)

    my_quad = fit_quad(br, bo)
    my_gauss = fit_gauss(br, bo)

    print '''
    -----------------------------------------------------
    Additional Models:
    -----------------------------------------------------

    Quadratic:
    %s

    Gaussian:
    %s
    -----------------------------------------------------
    ''' %(my_quad, my_gauss)



