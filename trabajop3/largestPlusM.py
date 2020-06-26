#Memoization

def calculateSizeM(grid):

	n=0
	res=0
	cacheR={}
	cacheL={}
	cacheT={}
	cacheB={}

	def R(grid, i, j):
		if grid[i][j] == 0:
			return 0
		if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid)-1:
			return grid[i][j]
		key =str(i)+" "+str(j)
		if key not in cacheR:
			cacheR[key]= R(grid, i, j+1)*grid[i][j] + grid[i][j]			
		return cacheR[key]

	def L(grid, i, j):
		if grid[i][j] == 0:
			return 0
		if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid)-1:
			return grid[i][j]
		key =str(i)+" "+str(j)
		if key not in cacheL:
			cacheL[key]= L(grid, i, j-1)*grid[i][j] + grid[i][j]
		return cacheL[key]

	def T(grid, i, j):
		if grid[i][j] == 0:
			return 0
		if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid)-1:
			return grid[i][j]
		key =str(i)+" "+str(j)
		if key not in cacheT:
			cacheT[key]= T(grid, i-1, j)*grid[i][j] + grid[i][j]	
		return cacheT[key]

	def B(grid, i, j):
		if grid[i][j] == 0:
			return 0
		if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid)-1:
			return grid[i][j]
		key =str(i)+" "+str(j)
		if key not in cacheB:
			cacheB[key]= B(grid, i+1, j)*grid[i][j] + grid[i][j]		
		return cacheB[key]

	def C(grid, i, j):
		if grid[i][j] == 0:
			return 0	

		if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid)-1:
			return grid[i][j]
		return min(min(R(grid, i,j+1),B(grid, i+1,j)),min(T(grid, i-1, j), L(grid, i, j-1)))*grid[i][j]*4 + grid[i][j]


	for j in range(len(grid)):
		for i in range(len(grid)):
			n=C(grid, i, j)
			if res < n:
				res=n

	return res