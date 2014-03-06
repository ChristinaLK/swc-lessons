import sys
import ipythonblocks as blocks
import numpy as np

filename = sys.argv[1] 
data = np.loadtxt(filename,delimiter=',')

heat_map = blocks.ImageGrid(data.shape[1],data.shape[0], block_size = 5)

for i in range(0,heat_map.height):
    for j in range(0,heat_map.width):
        data_val = data[i,j]
        if data_val < 4:
            heat_map[j,i] = blocks.colors['Blue']
        elif data_val < 9:
            heat_map[j,i] = blocks.colors['Green']
        elif data_val < 14:
            heat_map[j,i] = blocks.colors['Yellow']
        elif data_val < 19:
            heat_map[j,i] = blocks.colors['Orange']
        else:
            heat_map[j,i] = blocks.colors['Red']

heat_map.lines_on = False
heat_map.show()



