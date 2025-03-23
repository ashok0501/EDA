import numpy as np
import matplotlib.pyplot as plt
import math
def rotation ( theta ):
    rotation_matrix = np. matrix ([[ np.cos ( theta ), 
                                    -np.sin( theta )], 
                                   [np.sin ( theta ), np.cos ( theta )]])
    return rotation_matrix

def speedometer ( percentile , ax = None , fsize = 20) :
    angles = np. linspace (0, np.pi , 100)
    x = np. cos ( angles )
    y = np. sin ( angles )
    if ax is None :
        ax = plt.gca ()
    ax. set_aspect ('equal')
    ax. axis ('off')
    ax. plot (x,y, linewidth = 3, color = 'black')
    theta = -np.pi * ( percentile /100)
    length = 0.8
    base = np. matrix ([0 ,0])
    tip = np. matrix ([- length ,0])
    points = [base , tip ]
    new_points = [ rotation ( theta )*p.T for p in points ]
    x = [np. array (p). flatten () [0] for p in new_points ]
    y = [np. array (p). flatten () [1] for p in new_points ]
    ax. plot (x,y, color = 'darkred',
              linewidth = 4, solid_capstyle = 'round')
    ax. plot (0 ,0 , marker = 'o',color = 'darkred', markersize = 10)
    ticks = np. linspace (0 ,180 , 11)
    for angle in ticks : #np. arange (0 ,181 , step = step ):
        radians = math.radians ( angle )
        x1 , y1 = np. cos ( radians ), np. sin( radians )
        x2 , y2 = .95* x1 , .95* y1
        ax. plot ([x1 ,x2], [y1 ,y2],
                  color = 'black', zorder = -1)
        raw = 180 - angle
        ptile = raw /180 * 100
        s = " {:.0f}%". format ( ptile ) 
        ax. text (.9* x2 , .9* y2 , s,ha = 'center', zorder = -1)
        ax. text (0.04 , .15 , '{:.0f}%'. format ( percentile )
                  ,va= 'bottom',ha = 'center',size = fsize ,alpha = 0.2)
        ax. text (.9* x2 , .9* y2 , s,ha = 'center', zorder = -1)
    ax. text (0.04 , .15 , '{:.0f}%'. format ( percentile ),va= 'bottom',ha = 'center',size = fsize ,alpha = 0.2)



fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10, 12))
axes = axes.flatten()
axes[0].set_title("SVM")
axes[1].set_title("DT")
axes[2].set_title("RF")
axes[3].set_title("kNN")
speedometer (54 ,ax=axes[0], fsize = 65)
speedometer (42 ,ax=axes[1], fsize = 65)

speedometer (88 ,ax=axes[2], fsize = 65)
speedometer (100 ,ax=axes[3], fsize = 65)

speedometer (71 ,ax=axes[4], fsize = 65)
speedometer (90 ,ax=axes[5], fsize = 65)
plt.tight_layout() 
plt.show()