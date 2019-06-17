import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import matplotlib.dates as mdates

register_matplotlib_converters()

#Styling
plt.style.use('seaborn-darkgrid') 

XL = pd.read_csv(
    './dataSaham/EXCL.JK.csv', delimiter=',', 
    index_col=False,
    parse_dates=['Date'])

FR = pd.read_csv(
    './dataSaham/FREN.JK.csv', delimiter=',', 
    index_col=False,
    parse_dates=['Date'])

ISAT = pd.read_csv(
    './dataSaham/ISAT.JK.csv', delimiter=',', 
    index_col=False,
    parse_dates=['Date'])   

TLKM = pd.read_csv(
    './dataSaham/TLKM.JK.csv', delimiter=',', 
    index_col=False,
    parse_dates=['Date'])                 

#DATA BULAN APRIL
XL = XL.set_index('Date')                  
XL = XL['2019-04']
FR = FR.set_index('Date')
FR = FR['2019-04']                  
ISAT = ISAT.set_index('Date')
ISAT = ISAT['2019-04']     
TLKM = TLKM.set_index('Date')
TLKM = TLKM['2019-04']     

#PLOTTING
plt.figure("Harga Historis Saham", figsize=(16,10))
ax = plt.subplot()
ax.plot(XL.index, XL['Close'], label='PT. XL Axiata Tbk', color='g')
ax.plot(FR.index, FR['Close'], label='PT Smartfren Telecom Tbk', color='cyan')
ax.plot(ISAT.index, ISAT['Close'], label='PT Indosat Tbk', color='b')
ax.plot(TLKM.index, TLKM['Close'], label='PT Telekomunikasi Indonesia Tbk', color='r')

ax.grid(True)
ax.set_title("Harga Historis Saham Provider Telco Indonesia Bulan April 2019", y=1.08, fontsize=15)

ticks = pd.date_range(start='20190331', end='20190501', freq='D', name='titik')
myFmt = mdates.DateFormatter('%d-%m-%Y')
ax.xaxis.set_major_formatter(myFmt)
plt.xticks(ticks, rotation=30, fontsize=8) 

plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.legend(bbox_to_anchor=(0., 1.0, 1., .102), loc=3,
           ncol=4, mode="expand", borderaxespad=0.)

plt.show()

