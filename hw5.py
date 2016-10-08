## Dan Smilowitz
## DATA 602 hw5


# Perform a linear regression using the least squares method on the relationship of 
# brain weight [br] to body weight [bo].  using just the built in Python functions.
# Find values for X and Y in the equation bo = X * br + Y and print the model to the console.

import pandas as pd
brain_body = pd.read_csv('data/brainandbody.csv')

#  from Wolfram Mathworld:
#
#       Sum(y) * Sum(x^2) - Sum(x) * Sum(x * y)          n * Sum(x * y) - Sum(x) * Sum(y)
#  a = ----------------------------------------- ;  b = ----------------------------------
#            n * Sum(x^2) - [Sum(x)]^2                     n * Sum(x^2) - [Sum(x)]^2 

br = brain_body['brain']  # independent variable
bo = brain_body['body']  # dependent variable
n = len(brain_body)

sum_x = sum(br)
sum_x2 = sum(br * br)
sum_y = sum(bo)
sum_xy = sum(br * bo)

a = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x * sum_x)
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)

print ('bo = %.3f + %.3f * br' % (a, b))