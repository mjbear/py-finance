# https://github.com/ficusrobusta/Quantitative-Trading-Strategies-Using-Python/blob/main/Electronic_Market_Chapter_2.ipynb

import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = np.loadtxt('BenchmarkDatasets/NoAuction/3.NoAuction_DecPre/NoAuction_DecPre_Training/Train_Dst_NoAuction_DecPre_CF_7.txt')
print(df.shape)

# Let us extract the price-volume pairs across all timestamps. Remember to transpose the dataset, which is achieved by accessing the .T attribute. 
# The final result is then converted into a Pandas DataFrame format for better processing later. 
df2 = pd.DataFrame(df[:40, :].T)

labels = ["Up", "Stationary", "Down"]
            
def printdistribution(dataset):   
    fig = make_subplots(rows=1, cols=5,
                       subplot_titles=("k=10", "k=20", "k=30", "k=50", "k=100"))            
    fig.add_trace(      
        go.Histogram(x=dataset[144,:], histnorm='percent'),      
        row=1, col=1            
    )
           
    fig.add_trace(        
        go.Histogram(x=dataset[145,:], histnorm='percent'),      
        row=1, col=2          
    )
          
    fig.add_trace(      
        go.Histogram(x=dataset[146,:], histnorm='percent'),     
        row=1, col=3          
    )
            
    fig.add_trace(     
        go.Histogram(x=dataset[147,:], histnorm='percent'),    
        row=1, col=4        
    )
           
    fig.add_trace(       
        go.Histogram(x=dataset[148,:], histnorm='percent'),     
        row=1, col=5,         
    )
         
    fig.update_layout(     
        title="Label distribution of mid-point movement",     
        width=700, 
        height=300,     
        showlegend=False   
    )
       
    fig.update_xaxes(ticktext=labels, tickvals=[1, 2, 3], tickangle = -45)        
    fig.update_yaxes(visible=False, showticklabels=False)       
    fig.layout.yaxis.title.text = 'percent'

    print('Test')          
    fig.show()

printdistribution(df)

# Now we would like to dissect this DataFrame and allocate each component to a separate DataFrame. 
# We subset the DataFrame based on the sequence of columns for each component, 
# resulting in four DataFrames: dfAskPrices, dfAskVolumes, dfBidPrices, and dfBidVolumes. 
# Subsetting the DataFrame is completed by calling the loc() function and supplying the corresponding row and column indexes.

dfAskPrices = df2.loc[:, range(0,40,4)]
dfAskVolumes = df2.loc[:, range(1,40,4)]
dfBidPrices = df2.loc[:, range(2,40,4)]
dfBidVolumes = df2.loc[:, range(3,40,4)]

print(dfAskPrices.loc[0,:])
print(dfBidPrices.loc[0,:])

# The results show that the ask prices follow an increasing sequence, while the bid prices follow a decreasing sequence. 
# Since we often work with price data that follow an increasing sequence in analyses such as plotting, 
# we need to reverse the order of the bid prices.
# The order could be reversed by rearranging the sequence of columns in the DataFrame

print(dfBidPrices.columns)

# We can reverse the ordering by the [::-1] command:

print(dfBidPrices.columns[::-1])

dfBidPrices = dfBidPrices[dfBidPrices.columns[::-1]]
dfBidVolumes = dfBidVolumes[dfBidVolumes.columns[::-1]]

print(dfBidPrices.loc[0,:])

# Since the price increases from the bottom (buy side) to the top (sell side) in a limit order book, 
# we can join the price tables from both sides to show the continuum. 

# Concatenate Bid and Ask together to form complete orderbook picture
           
dfPrices = dfBidPrices.join(dfAskPrices, how='outer')
dfVolumnes = dfBidVolumes.join(dfAskVolumes, how='outer')

#Rename columns starting from 1->20    
dfPrices.columns = range(1, 21)         
dfVolumnes.columns = range(1, 21)

print(dfPrices.loc[0,:])

# The result shows that all prices are in increasing order. 
# Since the first ten columns show the buy-side prices and the last ten columns belong to the sell-side prices, 
# the best bid price would be the highest price at the buy side, that is, 0.2606, 
# while the best ask price (best offer) would be the lowest price at the sell side, that is, 0.2615.

fig = go.Figure()
              
for i in dfPrices.columns:  
    fig.add_trace(go.Scatter(y=dfPrices[:50][i]))
             
fig.update_layout(        
    title='10 price levels of each side of the orderbook',  
    xaxis_title="Time snapshot index",          
    yaxis_title="Price levels",          
    height=500,        
    showlegend=False,          
)
fig.show()

# Note that the graph is interactive, offering the usual set of flexible controls 
# (such as zooming, highlighting via selection, and additional data upon hovering) 
# based on the plotly library

px.bar(dfVolumnes.head(5).transpose(), orientation='h')

colors = ['lightslategrey',] * 10
colors = colors + ['crimson',] * 10
fig = go.Figure()
timestamp = 0
fig.add_trace(go.Bar(
    y= ['price-'+'{:.4f}'.format(x) for x in dfPrices.iloc[timestamp].
    tolist()],
    x=dfVolumnes.iloc[timestamp].tolist(),
    orientation='h',
    marker_color=colors
))
fig.update_layout(
    title='Volume of 10 price levels of each side of the orderbook',
    xaxis_title="Volume",
    yaxis_title="Price levels",
#     template='plotly_dark'
)
fig.show()

# We can also combine the previous two charts together,
fig = make_subplots(rows=1, cols=2)
for i in dfPrices.columns:
    fig.add_trace(go.Scatter(y=dfPrices.head(20)[i]), row=1, col=1)
timestamp = 0
fig.add_trace(go.Bar(
    y= ['price-'+'{:.4f}'.format(x) for x in dfPrices.iloc[timestamp].tolist()],
    x= dfVolumnes.iloc[timestamp].tolist(),
    orientation='h',
    marker_color=colors
), row=1, col=2)
fig.update_layout(
    title='10 price levels of each side of the orderbook for multiple time points, bar size represents volume',
    xaxis_title="Time snapshot",
    yaxis_title="Price levels",
    template='plotly_dark'
)
fig.show()
     
# Animating the price movement

widthOfTime = 100
priceLevel = 1
fig = go.Figure(
    data=[go.Scatter(
        x=dfPrices.index[:widthOfTime].tolist(),
        y=dfPrices[:widthOfTime][priceLevel].tolist(),
        name="frame",
        mode="lines",
        line=dict(width=2, color="blue"),
    )],
    layout=go.Layout(
        width=1000, 
        height=400,
        xaxis=dict(range=[0, 100], autorange=False, zeroline=False),
        yaxis=dict(range=[0.257, 0.261], autorange=False,zeroline=False),
        title="10 price levels of each side of the orderbook",
        xaxis_title="Time snapshot index",
        yaxis_title="Price levels",
        template='plotly_dark',
        hovermode="closest",
        updatemenus=[dict(
            type="buttons",
            showactive=True,
            x=0.01,
            xanchor="left",
            y=1.15,
            yanchor="top",
            font={"color":'blue'},
            buttons=[dict(
                label="Play",
                method="animate",
                args=[None])])]),
    frames=[go.Frame(
        data=[go.Scatter(
            x=dfPrices.iloc[k:k+widthOfTime].index.tolist(),
            y=dfPrices.iloc[k:k+widthOfTime][priceLevel].tolist(),
            mode="lines",
            line=dict(color="blue", width=2)
        )] 
    ) for k in range(widthOfTime, 1000)]
    )
fig.show()

# Animating the volume movement     
timeStampStart = 100
fig = go.Figure(
    data=[go.Bar(y= ['price-'+'{:.4f}'.format(x) for x in
    dfPrices[:timeStampStart].values[0].tolist()],
    x=dfVolumnes[:timeStampStart].values[0].tolist(),
    orientation='h',
    name="priceBar",
    marker_color=colors),
    ],
    layout=go.Layout(width=800, height=450,
        title="Volume of 10 buy, sell price levels of anorderbook",
        xaxis_title="Volume",
        yaxis_title="Price levels",
        template='plotly_dark',
        hovermode="closest",
        updatemenus=[dict(
            type="buttons",showactive=True,
            x=0.01,
            xanchor="left",
            y=1.15,
            yanchor="top",
            font={"color":'blue'},
            buttons=[dict(label="Play",
            method="animate",
            args=[None])])]),
    frames=[go.Frame(
    data=[go.Bar(y= ['price-'+'{:.4f}'.format(x) for x in dfPrices.
iloc[k].values.tolist()],
    x=dfVolumnes.iloc[k].values.tolist(),
    orientation='h',
    marker_color=colors)],
    layout=go.Layout(width=800, height=450,
    title="Volume of 10 buy, sell price levels of an orderbook [Snapshot=" + str(k) +"]",
    xaxis_title="Volume",
    yaxis_title="Price levels",
    template='plotly_dark',
    hovermode="closest")) for k in
range(timeStampStart, 500)]
)
fig.show()

print('END')