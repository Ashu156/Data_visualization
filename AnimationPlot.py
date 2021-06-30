# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 17:14:11 2020

@author: Dell
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ffmpeg import *

overdoses = pd.read_excel('C:/Users/Dell/Downloads/overdose_data_1999-2015.xls', sheet_name = 'Online', skiprows = 6)

def get_data(table, rownum, title):
    data = pd.DataFrame(table.loc[rownum][2:]).astype(float)
    data.columns = {title}
    return data


title = 'Heroin Overdoses'
d = get_data(overdoses, 18, title)
x = np.array(d.index)
y = np.array(d['Heroin Overdoses'])
overdose = pd.DataFrame(y, x)
overdose.columns = {title}

#Writer = animation.FFMpegWriter['ffmpeg']
writer = animation.FFMpegWriter(fps=20, metadata=dict(artist='Me'), bitrate=1800)

fig = plt.figure(figsize=(10,6))
plt.xlim(1999, 2016)
plt.ylim(np.min(overdose)[0], np.max(overdose)[0])
plt.xlabel('Year',fontsize=20)
plt.ylabel(title,fontsize=20)
plt.title('Heroin Overdoses per Year',fontsize=20)

ax = plt.axes(xlim=(1999, 2016), ylim=(np.min(overdose)[0], np.max(overdose)[0]))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    data = overdose.iloc[:int(i+1)] #select data range
    p = sns.lineplot(x=data.index, y=data[title], data=data, color="r")
    p.tick_params(labelsize=17)
    plt.setp(p.lines,linewidth=7)
    
    
ani = matplotlib.animation.FuncAnimation(fig, animate, frames=17, repeat=True)
ani.save('HeroinOverdosesJumpy.mp4', writer = writer)
plt.show()
