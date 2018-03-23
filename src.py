import numpy as np
#from anytree import Node, RenderTree, AsciiStyle
#import anytree

gridMap = np.array([[1, 1, 1, 0, 0],[0, 0, 0, 0, 1],[0, 1, 1, 0, 0],[0, 0, 1, 1, 0],[1, 0, 0, 0, 0]]) 

X=gridMap.shape[0]-1
Y=gridMap.shape[1]-1
#print(X)
#print(Y)
## Start Location 
startrow = 2
startcol = 0

## End Location
endrow = 2
endcol = 4

""" print(gridMap)
print('Starting Location ',startrow,startcol)
print('End Location ',endrow,endcol)
print('Starting Pixel',gridMap[startrow,startcol])
print('Ending Pixel',gridMap[endrow,endcol]) """

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
f=np.zeros((5,5))

for i in range(5):
    for j in range(5):
        h[i,j]=heuristic(i,j,endrow,endcol)
        if gridMap[i,j]!=0:  
            g[i,j]=100 

   # print(h)
    #print(g)
    
    current_node=[startrow,startcol]         # Current Location Co-ordinates
    
    open_list=[current_node]             # List of Frontier Locations -- Visited But Not Explored
   # l=len(open_list)
    #print('Frontier',len(open_list))
    closed_list=[]                        # List of Visted and Explored Locations

    f=np.zeros((5,5))                       # Total Cost Function
   
    f[startrow,startcol]=h[startrow,startcol]   # Initial Cost is Heuristic Cost
    k=50
    while k!=0:
        
       # print(open_list)
        l=len(open_list)
        minval = 1000
        minrow=0
        mincol=0
        for i in range(l):
            f[open_list[i][0],open_list[i][1]]=g[open_list[i][0],open_list[i][1]]+heuristic(open_list[i][0],open_list[i][1],
            endrow,endcol) 
            if minval>=f[open_list[i][0],open_list[i][1]]:
                minval=f[open_list[i][0],open_list[i][1]]
                minrow=open_list[i][0]
                mincol=open_list[i][1]

        current_node=[minrow,mincol]
        print('current node',current_node)
        if(goalTest(current_node[0],current_node[1],endrow,endcol)):
            print('-------------found--------------',k)
            break
        
        node_successor=Succesors(current_node[0],current_node[1])
      #  print(node_successor)
        nsl=len(node_successor)
      #  print(nsl)
        for i in range(nsl):
            succesor_cost=g[current_node[0],current_node[1]]+heuristic(current_node[0],current_node[1],
            node_successor[i][0],node_successor[i][1]) 
    #    print('Inside For Loop')
            #succesor_cost=g[current_node[0],current_node[1]]+h[node_successor[i][0],node_successor[i][1]]
       #     print(succesor_cost)
            if [node_successor[i][0],node_successor[i][1]] in open_list:
                if g[node_successor[i][0],node_successor[i][1]] <=succesor_cost: continue
            elif [node_successor[i][0],node_successor[i][1]] in closed_list:
                if g[node_successor[i][0],node_successor[i][1]] <=succesor_cost: continue
                closed_list.remove([node_successor[i][0],node_successor[i][1]])
                open_list.append([node_successor[i][0],node_successor[i][1]])
            else:
                open_list.append([node_successor[i][0],node_successor[i][1]])
         #       print('Appending to open list')
        g[node_successor[i][0],node_successor[i][1]]=succesor_cost
 
       
        closed_list.append(current_node)
    k=k-1
        




copy_succ=Succesors(2,4)
print(copy_succ)
copy_openlist=[[1,1],[1,2],[1,3],[1,4]]
if[copy_succ[1][0],copy_succ[1][1]] in copy_openlist:
    print('y')
    copy_openlist.remove([copy_succ[1][0],copy_succ[1][1]])
print(copy_openlist)
'''
    nodex_open=[]
    nodex_close=[]

        nodex.append(Node([2,0]))
        nodex.append(Node([1,2],parent=nodex[0]))
        nodex.append(Node([0,1],parent=nodex[0]))
        nodex.append(Node([0,2],parent=nodex[2],state="f"))
        print(RenderTree(nodex[0]))
        print(()!=anytree.search.findall_by_attr(nodex[0], name="state",value="f"))


    nodex_open.append(Node([startrow,startcol]))
    f[startrow,startcol]=g[startrow,startcol]
    print([2,0]==nodex_open[0])
    #while nodex_open!=[]:
'''
