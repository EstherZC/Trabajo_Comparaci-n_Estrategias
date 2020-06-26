class T_Iterator():


	def __init__(self, grid,i,j):
		self.grid=grid
		self.i=i
		self.j=j
		self.up=self.i-1
		self.down=self.i+1
		self.left=self.j-1
		self.right=self.j+1
		
	def next(self):
		res=[]
		res.append(self.grid[self.up][self.j])
		res.append(self.grid[self.down][self.j])
		res.append(self.grid[self.i][self.right])
		res.append(self.grid[self.i][self.left])
		self.up=self.up-1
		self.down=self.down+1
		self.left=self.left-1
		self.right=self.right+1
		return res

	def hasNext(self):
		if self.down >= len(self.grid) or self.up < 0 or self.right >= len(self.grid) or self.left < 0:
			return bool(0)
		return bool(1)	