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
visibleMatrix = [[('g','e'),('h','f'),('c','a'),('d','b')],
                 [('f','h'),('e','g'),('b','d'),('a','c')],
                 [('e','f'),('g','h'),('a','b'),('c','d')],
                 [('h','g'),('f','e'),('d','c'),('b','a')],
                 [('e','a'),('f','b'),('g','c'),('h','d')],
                 [('a','e'),('b','f'),('c','g'),('d','h')]]

drawMatrix = [[],[],[],[],[],[]]

"""
vertexMap maps the vertices to their position in the list...
Could we do this with a list too? Not sure.
"""
vertexMap = {}

#TEST DATA
testMatrix = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]


"""
list of faces per block. Same order - F/B/L/R/T/B by index
with the key representing the block face
"""
blockFaces = {
 'a': [(24,19,1,6),(22,23,5,4),(23,24,6,5),(19,22,4,1),(6,1,4,5),(19,24,23,22)],
 'b': [(19,20,2,1),(21,22,4,3),(22,19,1,4),(20,21,3,2),(1,2,3,4),(20,19,22,21)],
 'c': [(25,26,8,7),(19,24,6,1),(24,25,7,6),(26,19,1,8),(1,6,7,8),(25,26,19,24)],
 'd': [(26,27,9,8),(20,19,1,2),(19,26,8,1),(27,20,2,9),(1,8,9,2),(27,26,19,20)],
 'e': [(6,1,10,15),(4,5,14,13),(5,6,15,14),(1,4,13,10),(10,15,14,13),(6,5,4,1)],
 'f': [(1,2,11,10),(3,4,13,12),(4,1,10,13),(2,3,12,11),(10,11,12,13),(2,1,4,3)],
 'g': [(7,8,17,16),(1,6,15,10),(6,7,16,15),(8,1,10,17),(10,15,16,17),(9,8,1,2)],
 'h': [(8,9,18,17),(2,1,10,11),(1,8,17,10),(9,2,11,18),(10,17,18,11),(8,7,6,1)]
}

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


for k in range(len(drawMatrix)):
    for j in range(BLOCK_LEN*BLOCK_LEN):
        if visibleMatrix[k][j][0] in confirmed:
            drawMatrix[k].append(visibleMatrix[k][j][0])
        elif visibleMatrix[k][j][1] in confirmed:
            drawMatrix[k].append(visibleMatrix[k][j][1])
        else:
            #there is nothing here to draw
            pass



with open(obj_path, 'a+') as fle:
    count = 0
    for block in drawMatrix:
        for face in block:
            faceCoords = blockFaces[face][count]
            f = ""

            for k in range(4):
                f += str(faceCoords[k])
                f += " " # i hate how hacky this is but i just want to get it done
            f = "f " + f + "\n" # and dont really feel like thinking about efficiency
            fle.write(f)
        count += 1


"""
Vertex Bois

v 0 0 0
v 1 0 0
v 1 1 0
v 0 1 0
v -1 1 0
v -1 0 0
v -1 -1 0
v 0 -1 0
v 1 -1 0
v 0 0 1
v 1 0 1
v 1 1 1
v 0 1 1
v -1 1 1
v -1 0 1
v -1 -1 1
v 0 -1 1
v 1 -1 1
v 0 0 -1
v 1 0 -1
v 1 1 -1
v 0 1 -1
v -1 1 -1
v -1 0 -1
v -1 -1 -1
v 0 -1 -1
v 1 -1 -1
"""
