import sys
from time import time
from largestPlusBFR import *
from largestPlusBFI import *
from largestPlusBI import *
from largestPlusBR import *
from largestPlusT import *
from largestPlusM import *
from control import *

def createMatrix(dirfile, tam):

  file=open(dirfile, 'r')
  newMatrix=[]
  limite=int(int(file.readline()))
  for i in range(tam):
        newMatrix.append([0]*tam)

  for i in range(tam):
      for j in range(tam):
       newMatrix[i][j] = int(int(file.readline()))

  file.close()

  return newMatrix

def showMatrix(matrix):

  a=""
  for i in range(len(matrix)):
    for j in range(len(matrix)):
        a+=str(matrix[i][j])+" "
    print (a)
    a=""

  

class Main():

  Control(len(sys.argv),sys.argv[:])
  dirfile="./"+sys.argv[2]
  tam=int(sys.argv[4])
  m=createMatrix(dirfile, tam)

  def calculateSize(func,m):
    if func == "Backtracking (iterator)":
      start_time= time()
      result=calculateSizeBI(m)
      elapsed_time = time() - start_time
    elif func == "Backtracking (recursive)":
      start_time= time()
      result=calculateSizeBR(m)
      elapsed_time = time() - start_time
    elif func== "Brute Force (iterator)":
      start_time= time()
      result=calculateSizeBFI(m)
      elapsed_time = time() - start_time
    elif func == "Brute Force (recursive)":
      start_time= time()
      result=calculateSizeBFR(m)
      elapsed_time = time() - start_time
    elif func == "Tabulation":
      start_time= time()
      result=calculateSizeT(m)
      elapsed_time = time() - start_time
    else:
      start_time= time()
      result=calculateSizeM(m)
      elapsed_time = time() - start_time
    return result,elapsed_time
  

  switcher = {
    "-bi": "Backtracking (iterator)",
    "-br": "Backtracking (recursive)",
    "-fi": "Brute Force (iterator)",
    "-fr": "Brute Force (recursive)",
    "-t":  "Tabulation",
    "-m": "Memoization"
  }

  result,time = calculateSize(switcher.get(sys.argv[3]),m)
  if "-di" in sys.argv[:]:
      showMatrix(m)
  if "-do" in sys.argv[:]:
    print(switcher.get(sys.argv[3]),":: Largest Plus of 1's has size of ", result)
  if "-dt" in sys.argv[:]:
    print(switcher.get(sys.argv[3]),":: Time: %.3f seconds." % time)
	