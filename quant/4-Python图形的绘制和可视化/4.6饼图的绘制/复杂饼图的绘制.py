from pylab import *
#make a square figure and axes
figure(1, figsize=(6, 6))
ax = axes([0.1, 0.1, 0.8, 0.8])
fracs = [60, 40]
explode = (0, 0.08)
labels = 'Male', 'Female'
pie(fracs, explode=explode, labels=labels, autopct='%1.1f% %', shadow=True, startangle=90, colors=('g', 'r'))
title('Rate of Male and Female')
show()