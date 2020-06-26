import sys
import os.path 

class Control():

	
	def __init__(self, len, sysargv):
		self.len=len
		self.sysargv=sysargv
		error=self.__control_De_Errores()
		self.mostrarError(error)


	def __control_De_Errores(self):
		if self.len <2:
			return -1
		elif self.len == 2:
		
			if self.sysargv[1] == "-h":
				self.__mostrarMenu()
				sys.exit(0) 	#salir del pograma, después de mostrar el menú
			return -1
		elif self.len >= 5 and self.len <= 8:
			if self.sysargv[1] == "-f":
				if os.path.exists("./"+self.sysargv[2]) == bool(0):
					return -4
			
			else:
				return -1
			if self.sysargv[3] in ["-bi", "-br","-fi","-fr","-t","-m"]:
				try:
					number= int(self.sysargv[4])
					dirfile="./"+self.sysargv[2]
					file=open(dirfile,'r')
					limite=int(int(file.readline()))
					if number >1 and number<=limite:
						for i in self.sysargv[5:]:
							if i not in ["-di","-do","-dt"]:
								return -1
						return 0
					else:
						return -3 
				except ValueError:
					return -2
			
		return -1

	def mostrarError(self,error):

		if error==-1:
			print("Error:: usage: main.py [-h] [-f FILE [-bi -br -fi -fr -t -m] n] [-di] [-do] [-dt]")
			sys.exit(-1)
		elif error==-2:
			print("Error:: [n] is not a number")
			sys.exit(-2)
		elif error==-3:
			print("Error:: n (exceeds the file limit or it's 0)") 
			sys.exit(-3)
		elif error==-4:
			print("Error File:: "+ self.sysargv[2]+" doesn't exists or it's not in the current directory")
			sys.exit(-4)
		

	def __mostrarMenu(self):
		  print( "usage: main.py [-h] [-f FILE [-bi -br -fi -fr -t -m] n] [-di] [-do] [-dt]", 
			"\n optional arguments:",
			"\n -h           show this help message and exit",
			"\n -f [FILE]    input file",
			"\n -bi          Backtracking (iterator): Calculate size of the largest plus of 1's in binary matrix",
			"\n -br          Backtracking (recursive): Calculate size of the largest plus of 1's in binary matrix",
			"\n -fi          Brute Force (iterator): Calculate size of the largest plus of 1's in binary matrix",
			"\n -fr          Brute Force (recursive): Calculate size of the largest plus of 1's in binary matrix",
			"\n -t           Dynamic Programming (Tabulation): Calculate size of the largest plus of 1's in binary matrix",
			"\n -m           Dynamic Programming (Memoization): Calculate size of the largest plus of 1's in binary matrix",
			"\n  n           matrix size (n*n) ", 
			"\n -dt          display time in seconds",
			"\n -di          display input data",
			"\n -do          display output data")
