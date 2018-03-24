import numpy as np

gridMap = np.array([[1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 1],
                    [0, 1, 1, 0, 0],
                    [0, 0, 1, 1, 0],
                    [1, 0, 0, 0, 0]]) 

X=gridMap.shape[0]-1
Y=gridMap.shape[1]-1

## Start Location 
startrow = 2
startcol = 0

## End Location
endrow = 2
endcol = 4

def heuristic(start0,start1, goal0,goal1):
		#Use Chebyshev distance heuristic if we can move one square either
		#adjacent or diagonal
		D = 1
		D2 = 1
		dx = abs(start0 - goal0)
		dy = abs(start1 - goal1)
		return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)


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
        print(path)
    
   
    
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

