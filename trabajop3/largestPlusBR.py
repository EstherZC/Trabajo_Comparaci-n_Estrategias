#Backtracking (Recursive)
def R(grid, i, j):
	if grid[i][j] == 0:
		return 0
	if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid)-1:
		return grid[i][j]
	return R(grid, i, j+1)*grid[i][j] + grid[i][j]

def L(grid, i, j):
	if grid[i][j] == 0:
		return 0
	if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid)-1:
		return grid[i][j]
	return L(grid, i, j-1)*grid[i][j] + grid[i][j]

def T(grid, i, j):
	if grid[i][j] == 0:
		return 0
	if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid)-1:
		return grid[i][j]
	return T(grid, i-1, j)*grid[i][j] + grid[i][j]

def B(grid, i, j):
	if grid[i][j] == 0:
		return 0
	if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid)-1:
		return grid[i][j]
	return B(grid, i+1, j)*grid[i][j] + grid[i][j]

def C(grid, i, j):
	if grid[i][j] == 0:
		return 0

	if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid)-1:
		return grid[i][j]
	return min(min(R(grid, i,j+1),B(grid, i+1,j)),min(T(grid, i-1, j), L(grid, i, j-1)))*grid[i][j]*4 + grid[i][j]

def calculateSizeBR(grid):

	n=0
	res=0
	
	for j in range(len(grid)):
		for i in range(len(grid)):
			n=C(grid, i, j)
			if res < n:
				res=n

	return res