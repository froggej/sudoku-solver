import numpy as np
import math
from datetime import datetime

def avails(vec):
  avail = {1,2,3,4,5,6,7,8,9}
  for val in vec:
    if val in avail:
      avail.remove(val)
  return avail

def recompute_square(i, j):
    if s[i][j] > 0:
        s2[i][j] == {}
        return
    i_start = 3*(math.floor(i/3))
    i_end = i_start + 3
    j_start = 3*(math.floor(j/3))
    j_end = j_start + 3
    r = s[i]
    c = s[ :, j]
    ss = s[i_start:i_end,j_start:j_end].flatten()
    r_avail = avails(r)
    c_avail = avails(c)
    ss_avail = avails(ss)
    ij_avail = r_avail & c_avail & ss_avail
    s2[i][j] = ij_avail
    return

def recompute():
  for i in range(0,9):
    for j in range(0,9):
        recompute_square(i, j)
  return


text_file = open("p096_sudoku.txt", "r")
lines = text_file.read().splitlines()
print('lines = ',len(lines))
line_counter = 0
sum = 0
while line_counter in range(0, len(lines)):
  t = []
  print('Processing',lines[line_counter],'. . .')
  for line in range(line_counter + 1,line_counter + 10):
    t.append([])
    for char in range(0,9):
      t[line%10-1].append(int(lines[line][char]))
  text_file.close()
  timeA = datetime.now()
  s = np.array(t)
  s2 = [
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[]]
  ]
  recompute()
  arc = []
  arc_alt_val = []
  while True:
    not_done = 81
    for i in range(0,9):
      for j in range(0,9):
        if len(s2[i][j]) == 0 and s[i][j] > 0:
          not_done -= 1
        elif len(s2[i][j]) == 0 and s[i][j] == 0:
          s = arc.pop()
          alt_val = arc_alt_val.pop()
          s[alt_val[0]][alt_val[1]] = alt_val[2]
          recompute()
          continue        
    if not_done == 0:
      timeB = datetime.now()
      delta = timeB - timeA
      print('done')
      #print(s)
      print(int(delta.total_seconds() * 1000), ' milliseconds') # milliseconds
      break;
    break_val = False
    for x in range(1,10):
      for i in range(0,9):
        for j in range(0,9):
          if s[i][j] == 0:
            if len(s2[i][j]) == x:              
              cur_avail = s2[i][j]
              s[i][j] = cur_avail.pop()
              while len(cur_avail) > 0:
                arc.append(np.copy(s));
                arc_alt_val.append([i,j,cur_avail.pop()])
              recompute()
              break_val = True
              break
      if break_val: break
  line_counter += 10
