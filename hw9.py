## Dan Smilowitz 
## DATA 602 hw9


## Use the pandas module to answer the following questions about the EPA-HTTP data set.


import pandas as pd

## data preparation and sanitizing ##
# read file as pandas series
epa_raw = pd.read_table('data/epa-http.txt', header=None, squeeze=True)
# replace issues with placement of quotation marks in invalid requests
epa_raw = epa_raw.str.replace('gifalt=" HTTP/1.0"', 'gifalt= HTTP/1.0"')

## collecting into pandas DataFrame ##
# pull first two columns
epa = pd.DataFrame(epa_raw.str.split(' ', 2).tolist(), columns=['host', 'date', None])[['host', 'date']]
# pull third column
epa['request'] = pd.DataFrame(epa_raw.str.split('"', 2).tolist())[1]
# pull fourth and fifth columns
epa['reply'] = pd.DataFrame(epa_raw.str.rsplit(' ', 2).tolist())[1]
epa['size'] = pd.DataFrame(epa_raw.str.rsplit(' ', 2).tolist())[2]

## DataFrame sanitization ##
# convert date to datetimeformat
epa['date'] = '1995-08' + epa['date']
epa['date'] = pd.to_datetime(epa['date'], format='%Y-%m[%d:%H:%M:%S]')
# convert size to numeric, coercing '-' to 0
epa['size'] = pd.to_numeric(epa['size'], errors='coerce')


## Which hostname or IP address made the most requests?
most_requests = epa.groupby('host').count().sort_values(by='request', ascending=False)
print '%s made the most (%d) requests.' %(most_requests.index[0], most_requests.iloc[0,0])

## Which hostname or IP address received the most total bytes from the server?  How many bytes did it receive?
most_bytes = epa.groupby('host')['size'].sum().sort_values(ascending=False)
print '%s received the most data (%.0f bytes) from the server.' %(most_bytes.index[0], most_bytes.iloc[0])

## During what hour was the server the busiest in terms of requests?
busiest_hour = pd.DataFrame({'hour': epa['date'].dt.hour})
busiest_hour = busiest_hour.groupby('hour').size().sort_values(ascending=False)
print 'The most requests (%d) occured during hour %s.' %(busiest_hour.iloc[0], busiest_hour.index[0])

## Which .gif image was downloaded the most during the day?
gifs = epa.request.str.extract('(?P<gifname>/.*.gif)', expand=True)
gifs = gifs.gifname.value_counts()
print 'The .gif with the most downloads (%d) was %s.' %(gifs.iloc[0], gifs.index[0])

## What HTTP reply codes were sent other than 200?
import numpy as np
codes = np.sort(epa['reply'].unique())
codes = codes[np.where(codes != '200')]
print 'Besides 200, the following HTTP reply codes were sent:\n%s.' %', '.join(codes)