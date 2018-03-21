import numpy as np

gridMap = np.array([[1, 1, 1, 0, 0],[0, 0, 0, 0, 1],[0, 1, 1, 0, 0],[0, 0, 1, 1, 0],[1, 0, 0, 0, 0]]) 

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

# Generating Heuristic Matrix

h_matrix=np.zeros((5,5))
for i in range(5):
    for j in range(5):
        h_matrix[i,j]=heuristic(i,j,endrow,endcol)
        if gridMap[i,j]==0:  
            h_matrix[i,j]=100   
print(h_matrix)

