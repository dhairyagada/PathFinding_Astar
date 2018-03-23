import numpy as np

gridMap = np.array([[1, 1, 1, 0, 0],[0, 0, 0, 0, 1],[0, 1, 1, 0, 0],[0, 0, 1, 1, 0],[1, 0, 0, 0, 0]]) 

X=gridMap.shape[0]-1
Y=gridMap.shape[1]-1

## Start Location 
startrow = 2
startcol = 0

## End Location
endrow = 2
endcol = 4

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

h=np.zeros((5,5))
g=np.zeros((5,5))
f=np.zeros((5,5))
for i in range(5):
    for j in range(5):
        h[i,j]=heuristic(i,j,endrow,endcol)
        if gridMap[i,j]!=0:  
            g[i,j]=100 

cn=[startrow,startcol]

ol=[cn]         # Open List   -- Frontier 
cl=[]           # Closed List -- Explored List

f[ol[0][0],ol[0][1]]=h[ol[0][0],ol[0][1]]

k=15
while k!=0:
    
    ol_len=len(ol)
    min_f=10000
    for i in range(ol_len):
        f[ol[i][0],ol[i][1]]=g[ol[i][0],ol[i][1]]+g[ol[i][0],ol[i][1]]
        if min_f>f[ol[i][0],ol[i][1]]:
            min_f=f[ol[i][0],ol[i][1]]
            min_r=ol[i][0]
            min_c=ol[i][1]
    
    cn=[min_r,min_c]
    if goalTest(cn[0],cn[1],endrow,endcol):
        break 
    neighbors=Succesors(cn[0],cn[1])
    
    cl.append(cn)
    
    n_len=len(neighbors)
    min_succ=10000
    for j in range(n_len):
       
       f[neighbors[j][0],neighbors[j][1]]=g[neighbors[j][0],neighbors[j][1]]+h[neighbors[j][0],neighbors[j][1]]
       
       if min_succ>f[neighbors[j][0],neighbors[j][1]]:
            min_succ=f[neighbors[j][0],neighbors[j][1]]
            min_sr=neighbors[j][0]
            min_sc=neighbors[j][1]
      
    
    ol.append([min_sr,min_sc])
    ol.remove(cn)
    print(ol)
    k=k-1
    