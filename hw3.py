## Dan Smilowitz
## DATA 602 hw3

# locate file
import Tkinter, tkFileDialog
root = Tkinter.Tk()
root.withdraw()
filename = tkFileDialog.askopenfilename(parent = root)

# import data as pandas dataframe
import pandas as pd
col_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
cardata = pd.read_csv(filename, names=col_names, usecols=col_names[:-1], index_col=False)

# default sorting (alphabetical) will not return accurate results; convert to categorical series
# also converts disallowed values to NaN
cardata['buying'] = pd.Categorical(cardata['buying'], ['low', 'med', 'high', 'vhigh'])
cardata['maint'] = pd.Categorical(cardata['maint'], ['low', 'med', 'high', 'vhigh'])
cardata['doors'] = pd.Categorical(cardata['doors'], ['2', '3', '4', '5more'])
cardata['persons'] = pd.Categorical(cardata['persons'], ['2', '4', 'more'])
cardata['lug_boot'] = pd.Categorical(cardata['lug_boot'], ['small', 'med', 'big'])
cardata['safety'] = pd.Categorical(cardata['safety'], ['low', 'med', 'high'])

# Print to the console the top 10 rows of the data sorted by 'safety' in descending order
part_a = cardata.sort_values('safety', ascending=False).dropna()
print 'Part a: \n \n %s \n' % part_a.head(10)

# Print to the console the bottom 15 rows of the data sorted by 'maint' in ascending order
part_b = cardata.sort_values('maint', ascending=True).dropna()
print 'Part b: \n \n %s \n' % part_b.tail(15)

# Print to the console all rows that are high or vhigh in fields 'buying', 'maint', and 'safety', 
# sorted by 'doors' in ascending order.  Find these matches using regular expressions.
pattern = r'.*high\b'
part_c = cardata[cardata.buying.str.match(pattern) & cardata.maint.str.match(pattern) & cardata.safety.str.match(pattern)].dropna()
pd.set_option('display.max_rows', 1728)
print 'Part c: \n \n %s' % part_c.sort_values('doors', ascending=True)

# error handling
if len(cardata.dropna()) != len(cardata):
    print '''
WARNING:
One or more rows in the specified file contain missing or invalid entries.
Please refer to the data dictionary below, taken from
https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.names

buying:   vhigh, high, med, low
maint:    vhigh, high, med, low
doors:    2, 3, 4, 5more
persons:  2, 4, more
lug_boot: small, med, big
safety:   low, med, high

Invalid/missing entries have been converted to NaN and excluded from sorted results.
'''
