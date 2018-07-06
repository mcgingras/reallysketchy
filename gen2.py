"""
gen2... start from scratch
"""
import sys

img_path = sys.argv[1]
obj_path = sys.argv[2]

# what are the block dimensions?
BLOCK_LEN = 2

"""
list of tuples of "visible blocks"
a visible block is a block that could be seen in the line of sight for the given square
read left to right top to bottom

FRONT/BACK/LEFT/RIGHT/TOP/BOTTOM
"""

# VISIBLE MATRIX
visibleMatrix = [[('a','c'),('b','d'),('e','g'),('f','h')],
                 [('e','g'),('f','h'),('a','c'),('b','d')],
                 [('e','f'),('a','b'),('g','h'),('c','d')],
                 [('a','b'),('e','f'),('c','d'),('g','h')],
                 [('a','e'),('b','f'),('c','g'),('d','h')],
                 [('a','e'),('b','f'),('c','g'),('d','h')]]

#TEST DATA
testMatrix = [[1,1,0,1],
              [0,1,1,1],
              [1,1,0,1],
              [1,1,1,0],
              [1,1,1,1],
              [1,1,1,1]]

blockCount = {}
# is there a way to dynamically
for k in range(len(testMatrix)):
    for j in range(BLOCK_LEN*BLOCK_LEN):
        if testMatrix[k][j]:
            b1 = visibleMatrix[k][j][0]
            b2 = visibleMatrix[k][j][1]

            if b1 not in blockCount:
                blockCount[b1] = 1
            else:
                blockCount[b1] += 1


            if b2 not in blockCount:
                blockCount[b2] = 1
            else:
                blockCount[b2] += 1



confirmed = []
for block in blockCount:
    if blockCount[block] == 6:
        confirmed.append(block)

print(confirmed)


with open(obj_path, 'w+') as f:
    pass
if __name__ == '__main__':
    pass
