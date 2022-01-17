import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.widgets import Cursor, Button
import matplotlib.animation as animation

N=20
matrix = np.zeros((N,N))
cmap = colors.ListedColormap(['white', 'black'])
fig = plt.figure()
ax = fig.add_subplot(111)
mat = ax.matshow(matrix, cmap=cmap)
ticks = [i+0.5 for i in range(0,N-1)]
plt.xticks(ticks)
plt.yticks(ticks)    
ax.grid()
def onmouseclick(event):    
    print("onmouseclick")    
    x,y = int(round(event.xdata)),int(round(event.ydata))               
    if(matrix[y,x]==0):
        matrix[y,x]=1
    else: 
        matrix[y,x]=0
    ax.matshow(matrix, cmap=cmap)
    plt.xticks(ticks)
    plt.yticks(ticks) 
    plt.draw()
    


def update(data):
  global matrix
  newMatrix = matrix.copy()
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      total = (int(matrix[i, (j-1)%len(matrix)]) + int(matrix[i, (j+1)%len(matrix)]) +
               int(matrix[(i-1)%len(matrix), j]) + int(matrix[(i+1)%len(matrix), j]) + 
               int(matrix[(i-1)%len(matrix), (j-1)%len(matrix)]) + int(matrix[(i-1)%len(matrix), (j+1)%len(matrix)]) + 
               int(matrix[(i+1)%len(matrix), (j-1)%len(matrix)]) + int(matrix[(i+1)%len(matrix), (j+1)%len(matrix)]))
      print("j-", j, " N-", N, " (j-1)%N-", (j-1)%N)
      if matrix[i, j]  == 1:
        if (total < 2) or (total > 3):
          newMatrix[i, j] = 0
      else:
        if total == 3:
          newMatrix[i, j] = 1

  matrix = newMatrix.copy()
  ax.matshow(matrix, cmap=cmap)
  plt.xticks(ticks)
  plt.yticks(ticks) 
  plt.draw()  



def onkeypress(event):
  global matrix
  newMatrix = matrix.copy()
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      total = (int(matrix[i, (j-1)%len(matrix)]) + int(matrix[i, (j+1)%len(matrix)]) +
               int(matrix[(i-1)%len(matrix), j]) + int(matrix[(i+1)%len(matrix), j]) + 
               int(matrix[(i-1)%len(matrix), (j-1)%len(matrix)]) + int(matrix[(i-1)%len(matrix), (j+1)%len(matrix)]) + 
               int(matrix[(i+1)%len(matrix), (j-1)%len(matrix)]) + int(matrix[(i+1)%len(matrix), (j+1)%len(matrix)]))
      #print("total", total)
      print("j-", j, " N-", N, " (j-1)%N-", (j-1)%N)
      if matrix[i, j]  == 1:
        if (total < 2) or (total > 3):
          newMatrix[i, j] = 0
      else:
        if total == 3:
          newMatrix[i, j] = 1

  matrix = newMatrix.copy()
  ax.matshow(matrix, cmap=cmap)
  plt.xticks(ticks)
  plt.yticks(ticks) 
  plt.draw() 
fig.canvas.mpl_connect('button_press_event', onmouseclick)
fig.canvas.mpl_connect('key_press_event', onkeypress)


plt.show()