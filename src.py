import numpy as np

gridMap = np.array([[1, 1, 1, 0, 0],[0, 0, 0, 0, 1],[0, 1, 1, 0, 0],[0, 0, 1, 1, 0],[1, 0, 0, 0, 0]]) 

X=gridMap.shape[0]
Y=gridMap.shape[1]
print(X)
print(Y)
## Start Location 
startrow = 2
startcol = 0

## End Location
endrow = 2
endcol = 4

print(gridMap)
print('Starting Location ',startrow,startcol)
print('End Location ',endrow,endcol)
print('Starting Pixel',gridMap[startrow,startcol])
print('Ending Pixel',gridMap[endrow,endcol])

def heuristic(currentrow,currentcol,endrow,endcol):
    # Estimating Distance Between Point and End Location
    d_x=endrow-currentrow
    d_y=endcol-currentcol
    d=((d_x**2)+(d_y**2))
    d=np.sqrt(d)
    return d

def goalTest(currentrow,currentcol,endrow,endcol):
    # Testing if the current position is goal position
    return (currentrow==endrow and currentcol==endcol)

# Generating Succesors
Succesors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                                            for y2 in range(y-1, y+2)
                                                if (-1 < x <= X and -1 < y <= Y and
                                                    (x != x2 or y != y2) and
                                                    (0 <= x2 <= X) and 
                                                    (0 <= y2 <= Y))]
                                   

# Generating Heuristic Matrix

h=np.zeros((5,5))
g=np.zeros((5,5))
for i in range(5):
    for j in range(5):
        h[i,j]=heuristic(i,j,endrow,endcol)
        if gridMap[i,j]!=0:  
            g[i,j]=100 
print(h)
print(g)

currentlocn=[startrow,startcol]         # Current Location Co-ordinates

frontier_list=[currentlocn]             # List of Frontier Locations -- Visited But Not Explored

explored_list=[]                        # List of Visted and Explored Locations

f=np.zeros((5,5))                       # Total Cost Function

f[startrow,startcol]=h[startrow,startcol]   # Initial Cost is Heuristic Cost
while frontier_list!=0:
    f[currentlocn[0],currentlocn[1]]= g[currentlocn[0],currentlocn[1]]+ h[currentlocn[0],currentlocn[1]]
    if(goalTest(currentlocn[0],currentlocn[1],endrow,endcol)): break
    next_loc=Succesors(currentlocn[0],currentlocn[1])
    print(next_loc)
    print(next_loc[0][0],next_loc[0][1])
    print(f)
    frontier_list=0
    

                                   
