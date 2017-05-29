grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    x = goal[0]
    y = goal[1]
    dis = 0
    
    lis = [(dis,x,y)]
    value[x][y] = dis
    while True:
        if len(lis) == 0: break;
        
        lis.sort()
        lis.reverse()
        p = lis.pop()
        x = p[1]
        y = p[2]
        dis = p[0]
        
        for i in range(len(delta)):
            
            x2 = x - delta[i][0]
            y2 = y - delta[i][1]
            
            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                
                if value[x2][y2] == 99 and grid[x2][y2] == 0:
                    
                    dis2 = dis + 1
                    value[x2][y2] = dis2
                    policy[x2][y2] = delta_name[i]
                    lis.append((dis2,x2,y2))
                    
    # ----------------------------------------
    policy[goal[0]][goal[1]] = '*'
                
    for i in range(len(value)):
        print value[i]
    for i in range(len(value)):    
        print policy[i]
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 
compute_value(grid,goal,cost)
