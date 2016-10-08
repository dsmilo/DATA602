## Dan Smilowitz 
## DATA 602 hw6


## Using your submission of homework 1 as a base, replace as many of the functions as you can with numpy functions.
## Using the timeit function measure the execution times of all the sort and search functions you have.

# sorting functions from hw1
def sortwithloops(input):
    output = []
    input2 = input[:]
    for i in range(len(input2)):
        curr_min = min(input2)
        output.append(curr_min)
        input2.remove(curr_min)  
    return output
	
def sortwithoutloops(input): 
    return sorted(input)

# searching functions from hw1
def searchwithloops(input, value):
    found = False
    for item in input:
        if item == value:
            found = True
    return found

def searchwithoutloops(input, value):
    return value in input

# functions using numpy
import numpy as np

def sortnumpy(input):
    return np.msort(input)

def searchnumpy(input, value):
    found = False
    find_array = np.where(input == value)[0]
    if find_array.size > 0: found = True
    return found

# setup for evaluation
my_setup = '''
def sortwithloops(input):
    output = []
    input2 = input[:]
    for i in range(len(input2)):
        curr_min = min(input2)
        output.append(curr_min)
        input2.remove(curr_min)  
    return output
    
def sortwithoutloops(input): 
    return sorted(input)

def searchwithloops(input, value):
    found = False
    for item in input:
        if item == value:
            found = True
    return found

def searchwithoutloops(input, value):
    return value in input

import numpy as np

def sortnumpy(input):
    return np.sort(input)

def searchnumpy(input, value):
    found = False
    find_array = np.where(input == value)[0]
    if find_array.size > 0: found = True
    return found

np.random.seed(42)
N10 = np.random.randint(5000, size=10)
L10 = N10.tolist()

np.random.seed(42)
N100 = np.random.randint(5000, size=100)
L100 = N100.tolist()

np.random.seed(42)
N1000 = np.random.randint(5000, size=1000)
L1000 = N10.tolist()
'''


if __name__ == "__main__":	
    import timeit
    x = 10000
    sort1_10 = timeit.timeit('sortwithloops(L10)', setup = my_setup, number = x)
    sort2_10 = timeit.timeit('sortwithoutloops(L10)', setup = my_setup, number = x)
    sort3_10 = timeit.timeit('sortnumpy(N10)', setup = my_setup, number = x)
    sort1_100 = timeit.timeit('sortwithloops(L100)', setup = my_setup, number = x)
    sort2_100 = timeit.timeit('sortwithoutloops(L100)', setup = my_setup, number = x)
    sort3_100 = timeit.timeit('sortnumpy(N100)', setup = my_setup, number = x)
    sort1_1000 = timeit.timeit('sortwithloops(L1000)', setup = my_setup, number = x)
    sort2_1000 = timeit.timeit('sortwithoutloops(L1000)', setup = my_setup, number = x)
    sort3_1000 = timeit.timeit('sortnumpy(N1000)', setup = my_setup, number = x)
    search1t = timeit.timeit('searchwithloops(L100, 34)', setup = my_setup, number = x)
    search1f = timeit.timeit('searchwithloops(L100, 1)', setup = my_setup, number = x)
    search2t = timeit.timeit('searchwithoutloops(L100, 34)', setup = my_setup, number = x)
    search2f = timeit.timeit('searchwithoutloops(L100, 1)', setup = my_setup, number = x)
    search3t = timeit.timeit('searchnumpy(N100, 34)', setup = my_setup, number = x)
    search3f = timeit.timeit('searchnumpy(N100, 1)', setup = my_setup, number = x)

    print '''

    -----------------------------------------------------
    Execution Times (%d iterations):
    -----------------------------------------------------

    Sort Functions (by list length):
      Method      | 10 items   | 100 items  | 1000 items 
      ------------|------------|------------|------------
      Loops       | %.4f s   | %.4f s   | %.4f s   
      Base Python | %.4f s   | %.4f s   | %.4f s   
      NumPy       | %.4f s   | %.4f s   | %.4f s   
    
    Search functions (for 100 items):
      Method      | Found    | Not Found
      ------------|----------|-----------
      Loops       | %.4f s | %.4f s
      Base Python | %.4f s | %.4f s
      NumPy       | %.4f s | %.4f s

    -----------------------------------------------------
    ''' %(x, sort1_10, sort2_10, sort3_10, sort1_100, sort2_100, sort3_100, sort1_1000, sort2_1000, sort3_1000, search1t, search1f, search2t, search2f, search3t, search3f)
