from iterator import *

#Backtracking (Iterative)
def C(grid, i, j):
	if grid[i][j] == 0:
		return 0
	res=0
	plus=[]
	iterator = T_Iterator(grid, i, j)
	while iterator.hasNext():
		plus = iterator.next()
		for k in range(len(plus)):
			if plus[k] == 0:
				return res

		res = res+1

	return res

#Calculate the size of the largest '+' formed by 1's
def calculateSizeBI(grid):
	N = len(grid)
	res = 0
	for i in range(N):
		for j in range(N):
			n=C(grid, i, j)
			if res < n*4+grid[i][j]:
				res=n*4+grid[i][j]

	return res