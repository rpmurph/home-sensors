import partlycloudy as cloud
from constants import DEVICE_ID
from constants import ACCESS_TOKEN

import numpy as np
from numpy import pi

from bokeh.client import push_session
from bokeh.driving import cosine
from bokeh.plotting import figure, curdoc

tm = []
tmp = []

bit = cloud.Bit(ACCESS_TOKEN, DEVICE_ID)

#tm.append(0)
tmp.append( int(bit.input()) )

for i in range(0,100):
    tm.append(i)
    tmp.append(0)

p = figure(y_range=(60, 80))
r1 = p.line(tm, tmp, color="firebrick")

# open a session to keep our local document in sync with server
session = push_session(curdoc())

def update():
    t = int(bit.input())
    if t > 0:
        tmp.pop()
        tmp.insert(0, t)
        #tmp.remove(0)
        #tmp.append(t)
        r1 = p.line(tm, tmp, color="firebrick")

curdoc().add_periodic_callback(update, 2500)

#session.show() # open the document in a browser

session.loop_until_closed() # run forever
    
    
#if __name__ == '__main__':
#    main()