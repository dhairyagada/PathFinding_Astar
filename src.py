import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
""" gridMap =  np.array([[0,0,0,1,0,0,1,1,1,0,1,0,1,0],
            [1,1,1,1,1,0,1,0,1,0,1,1,1,0],
            [1,1,1,0,1,1,0,1,1,0,1,0,1,0],
            [1,0,0,1,0,1,0,1,1,0,0,1,1,0],
            [0,0,0,0,1,1,1,1,0,1,1,1,1,0],
            [0,1,1,0,0,1,0,0,0,1,0,0,0,0],
            [1,1,0,1,1,0,0,0,1,1,0,0,0,0],
            [1,1,0,1,0,1,0,1,0,0,1,1,0,1],
            [1,1,1,0,1,0,1,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,1,0,1,0,1,1,0,0],
            [0,0,0,0,0,0,0,0,1,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,1,0,1,0,1,1],
            [1,1,0,0,0,1,1,1,1,0,0,0,1,1],
            [1,1,0,1,0,1,0,0,1,1,0,1,0,0],
            [0,0,0,1,1,1,0,0,1,1,0,0,0,0],    
            [0,0,1,0,0,0,0,0,0,1,1,0,0,0],
            [1,0,1,1,0,1,0,0,0,1,1,0,0,0],
            [0,0,1,0,0,1,0,1,0,1,1,0,1,0],
            [1,0,0,0,0,1,1,1,0,1,0,0,0,0],
            [0,0,0,1,0,0,1,0,0,1,0,1,0,1],
            [0,0,0,1,0,0,0,1,0,0,0,1,1,0],
            [0,0,0,1,1,1,1,1,1,1,1,0,1,1],
            [1,1,1,1,1,1,0,0,0,1,0,1,0,0],
            [0,0,1,1,0,0,0,0,0,0,1,0,1,1],
            [1,1,1,1,0,1,0,1,0,0,1,1,1,1],
            [1,1,1,1,0,1,0,1,1,0,0,1,0,1],
            [0,1,0,0,0,0,1,0,0,0,0,0,1,0],
            [0,1,0,0,1,0,1,0,0,0,1,0,1,0],
            [1,1,0,1,1,1,1,1,0,0,1,0,1,0]]) """

gridMap = np.array([[1, 1, 1, 0, 0],[0, 0, 0, 0, 1],[0, 1, 1, 0, 0],[0, 0, 1, 1, 0],[1, 0, 0, 0, 0]]) 
X=gridMap.shape[0]-1
Y=gridMap.shape[1]-1

## Start Location 
startrow = int(X/2)
startcol = 0

## End Location
endrow = int(X/2)
endcol = int(Y)

def heuristic(currentrow,currentcol,endrow,endcol):
    # Estimating Distance Between Point and End Location
    d_x=endrow-currentrow
    d_y=endcol-currentcol
    d=((d_x**2)+(d_y**2))
    d=np.sqrt(d)
    return d



# Generating Succesors
Succesors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                                            for y2 in range(y-1, y+2)
                                                if (-1 < x <= X and -1 < y <= Y and
                                                    (x != x2 or y != y2) and
                                                    (0 <= x2 <= X) and 
                                                    (0 <= y2 <= Y))]

def move_cost(cr,cc,nr,nc):
    if gridMap[nr,nc]==1:
        return 1000
    else:
        return np.sqrt((cr-nr)**2+(cc-nc)**2)

start=(startrow,startcol)
end=(endrow,endcol)

g={}
f={}

''' --------------------- INITIALIZATIONS------------------------------------
'''

g[start]=0
f[start]=heuristic(startrow,startcol,endrow,endcol)

cl=set()
ol=set([start])

parent={}

while len(ol) > 0:

    current = None
    currentFScore = None

    for pos in ol:
        if current is None or f[pos] < currentFScore:
            currentFScore = f[pos]
            current = pos
    ol.remove(current)
    cl.add(current)
    if current == end:
			#Retrace our route backward
            	
        path = [current]
        #print ("Current", current)
        while current in parent:
            current = parent[current]
            path.append(current)
       
        path.reverse()
        print('Path is :',path)
    
   
    
    for neighbour in Succesors(current[0],current[1]):
        if neighbour in cl: 
            continue #We have already processed this node exhaustively
        candidateG = g[current] + move_cost(current[0],current[1], neighbour[0],neighbour[1])

        if neighbour not in ol:
            ol.add(neighbour) #Discovered a new vertex
        elif candidateG >= g[neighbour]:
            continue #This G score is worse than previously found

        #Adopt this G score
        parent[neighbour] = current
        g[neighbour] = candidateG
        h = heuristic(neighbour[0],neighbour[1],endrow,endcol)
        f[neighbour] = g[neighbour] + h

""" gridDisplay=np.array(gridMap)

for each in path:
    gridDisplay[each[0],each[1]]=4

print(gridDisplay) """



cmap = colors.ListedColormap(['white', 'black'])
bounds = [0,1,5]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
ax.imshow(gridMap, cmap=cmap, norm=norm)

ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-0.5,gridMap.shape[1],gridMap.shape[1]))
ax.set_yticks(np.arange(-0.5,gridMap.shape[0],gridMap.shape[0]))

ax.plot(np.asarray(path)[:,1], np.asarray(path)[:,0])
plt.show()