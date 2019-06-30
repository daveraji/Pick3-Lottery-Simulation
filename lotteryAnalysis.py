import pandas as pd
import holoviews as hv
from holoviews import opts
from collections import defaultdict
hv.extension('bokeh')

filename = r'DownloadAllNumbers.txt'
df = pd.read_csv(filename, skiprows=5, header=None, delimiter = '\s+', skipinitialspace = True)
df.columns =  ['draw', 'day', 'm', 'dm', 'yr', 'n1', 'n2', 'n3']
df = df[:1000].copy()

#DATA CLEANUP
#print(df.head(5))
df = df.astype(str)
df['num'] = df['n1'].str.cat(df['n2'],sep='')
df['num'] = df['num'].str.cat(df['n3'],sep='')
df =df.drop(columns =['day', 'm','dm', 'yr','n1', 'n2', 'n3'])
print(df.head(5))

#getting runing frequency of Numbers
def numFrequecy(df, num):
    '''
    Create a curve that tracks how frequently a number shows up in the draw (will add all the curves together later)
    '''
    count=0
    i=0
    df = df[::-1]
    for a in df['num']: #when number shows up in category add to count
        if str(num) in a:
            count +=1
        df.loc[999-i,'count']=count
        i+=1
    #return df.head(5)
    return hv.Curve(df, 'draw', 'count', label=str(num))

#print(numFrequecy(df[:1000],1,2))

group = [numFrequecy(df[:1000],a) for a in range(9)]
overlay= hv.Overlay(group)
overlay.opts(width=1000 )
#color=hv.Cycle(values=['indianred', 'slateblue', 'lightseagreen', 'coral']
renderer = hv.renderer('bokeh')
app= renderer.app(overlay, show=True)
print(app)
