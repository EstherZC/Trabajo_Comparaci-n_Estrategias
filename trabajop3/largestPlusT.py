#Tabulation
def calculateSizeT(grid):
    N = len(grid)
    left=[]
    right=[]
    top=[]
    bottom=[]
    for i in range(N):
        left.append([0]*N)
        right.append([0]*N)
        top.append([0]*N)
        bottom.append([0]*N)

    # initialize above matrices
    for i in range(N):
        # initialize first row of top matrix
        top[0][i] = grid[0][i]
        # initialize last row of bottom matrix
        bottom[N - 1][i] = grid[N - 1][i]
        # initialize first column of left matrix
        left[i][0] = grid[i][0]
        # initialize last column of right matrix
        right[i][N - 1] = grid[i][N - 1]
    
    # fill all cells of above four matrix
    for i in range(N):
        for j in range(1,N):
            # fill left matrix
            if grid[i][j] == 1:
                left[i][j] = left[i][j - 1] + 1
            # fill top matrix
            if grid[j][i] == 1:
                top[j][i] = top[j - 1][i] + 1
            # fill bottom matrix
            if grid[N - 1 - j][i] == 1:
                bottom[N - 1 - j][i] = bottom[N - j][i] + 1
            # fill right matrix
            if grid[i][N - 1 - j] == 1:
                right[i][N - 1 - j] = right[i][N - j] + 1
        
    
    # bar stores length of longest + found so far
    bar = 0;
    #compute longest plus
    for i in range(N):
        for j in range(N):
            # find minimum
            length = (min(top[i][j], bottom[i][j], 
                            left[i][j], right[i][j])-1)*grid[i][j]*4 + grid[i][j];
           # largest + is formed by a cell having maximum value
            if length  > bar:
                bar = length ;
       
    return bar  