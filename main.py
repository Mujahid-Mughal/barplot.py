# barplot.py
DATA VISUALIZATION IN PYTHON 

# Project Whole Code


import numpy as np
from matplotlib import pyplot as plt

exportlist={'2013':40000, '2014':50000, '2015':52000, '2016':65000, '2017':59000, '2018':63000, '2019':75000, '2020':69000,'2021':48000, '2022':56000}
year=list(exportlist.keys())
year

values=list(exportlist.values())
values

plt.bar(year, values)
plt.title("Export list Previous 10 Years")
plt.xlabel("Years")
plt.ylabel("Values in USD")
plt.grid(True)
plt.show()

# FOR LINE PLOT USE COMMAND
plt.plot(year, values)

#FOR SCATTER PLOT USE COMMAND
plt.scatter(year, values)
