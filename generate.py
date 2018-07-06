
"""
im starting to think we should create everything into a list first, then write it to the file
- how do we know what is a face in a complex shape?

steps:
loop through corners/intersections, add vertices
loop through corners creating faces
loop through corners making opposite faces
"""

import sys

img_path = sys.argv[1]
obj_path = sys.argv[2]

test_data_front = [(0,0),(1,0),(1,1),(0,1)]
test_data_top   = [(0,0),(1,0),(1,1),(0,1)]
test_data_right = [(0,0),(1,0),(1,1),(0,1)]


"""
Since we are only dealing with rectangluar shapes for now,
we are restricted to the following normals...

vn  0.0  0.0  1.0
vn  0.0  0.0 -1.0
vn  0.0  1.0  0.0
vn  0.0 -1.0  0.0
vn  1.0  0.0  0.0
vn -1.0  0.0  0.0
"""

"""
lot of code reuse going on in here -- should probably refactor a bit
"""
def generate():
    vertCount = 1
    # can probably do this in a list with indices -- just remember it is not 0 index
    vertList = []
    vertMap = {}
    with open(obj_path, 'w+') as f:
        # TOP
        for vertex in test_data_top:
            vertc = (vertex[0], vertex[1], 1)
            if vertc not in vertList:
                vertList.append(vertc)
            vert = 'v '+str(vertex[0])+ " " +str(vertex[1])+" 1"
            if vert not in vertMap:
                vertMap[vert] = vertCount
                f.write(vert+'\n')
                vertCount += 1


        # FRONT
        for vertex in test_data_front:
            vertc = (vertex[0], 0, vertex[1])
            if vertc not in vertList:
                vertList.append(vertc)
            vert = 'v '+str(vertex[0])+ " 0 " +str(vertex[1])
            if vert not in vertMap:
                vertMap[vert] = vertCount
                f.write(vert+"\n")
                vertCount += 1

        # RIGHT
        for vertex in test_data_right:
            vertc = (1, vertex[0], vertex[1])
            if vertc not in vertList:
                vertList.append(vertc)
            vert = 'v 1 '+str(vertex[0])+ " " +str(vertex[1])
            if vert not in vertMap:
                vertMap[vert] = vertCount
                f.write(vert+"\n")
                vertCount += 1

        for vertex in test_data_top:
            flist = []
            vert = 'v '+str(vertex[0])+ " " +str(vertex[1])+" 1"
            flist.append(vertMap[vert])
            f1 = ""
            for face in flist:
                f1 = f1 + " " + str(face)
            f.write("f " +f1)

        f.write("\nvn  0.0  0.0  1.0 \nvn  0.0  0.0 -1.0\nvn  0.0  1.0  0.0\nvn  0.0 -1.0  0.0\nvn  1.0  0.0  0.0\nvn -1.0  0.0  0.0")

    return vertList


if __name__ == '__main__':

    print(generate())
