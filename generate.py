
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

# BOX
# test_data_front = [(0,0),(1,0),(1,1),(0,1)]
# test_data_top   = [(0,0),(1,0),(1,1),(0,1)]
# test_data_right = [(0,0),(1,0),(1,1),(0,1)]

# RECT
test_data_front  = [(0,0),(1,0),(1,.5),(0,.5)]
test_data_top = [(0,0),(1,0),(1,1),(0,1)]
test_data_right = [(0,0),(1,0),(1,.5),(0,.5)]


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
the vertc and vert2 thing assumes complete symmetry throughout the object.
"""
def generate():
    vertCount = 1
    # can probably do this in a list with indices -- just remember it is not 0 index
    vertList = []
    with open(obj_path, 'w+') as f:
        # TOP
        for vertex in test_data_top:
            vertc = (vertex[0], vertex[1], .5)
            vert2 = (vertex[0], vertex[1], 0)
            if vertc not in vertList:
                vertList.append(vertc)
            if vert2 not in vertList:
                vertList.append(vert2)

        # FRONT
        for vertex in test_data_front:
            vertc = (vertex[0], 0, vertex[1])
            vert2 = (vertex[0], 1, vertex[1])
            if vertc not in vertList:
                vertList.append(vertc)
            if vert2 not in vertList:
                vertList.append(vert2)


        # RIGHT
        for vertex in test_data_right:
            vertc = (1, vertex[0], vertex[1])
            vert2 = (0, vertex[0], vertex[1])
            if vertc not in vertList:
                vertList.append(vertc)
            if vert2 not in vertList:
                vertList.append(vert2)

        # WRITING THE VERTICES
        for vertex in vertList:
            f.write("v "+ str(vertex[0]) + " " + str(vertex[1]) + " " + str(vertex[2])+"\n")

        # WRITING THE NORMALS (DO WE NEED THIS)
        #f.write("\nvn  0.0  0.0  1.0 \nvn  0.0  0.0 -1.0\nvn  0.0  1.0  0.0\nvn  0.0 -1.0  0.0\nvn  1.0  0.0  0.0\nvn -1.0  0.0  0.0\n\n")

        # WRITING THE FACES
        # this seems like not a good way to do it...
        face_array = []
        oppo_array = []
        for vertex in test_data_top:
            vertc = (vertex[0], vertex[1], .5)
            vert2 = (vertex[0], vertex[1], 0)
            fid = vertList.index(vertc) + 1
            fid2 = vertList.index(vert2) + 1
            face_array.append(fid)
            oppo_array.append(fid2)

        for vertex in test_data_front:
            vertc = (vertex[0], 0, vertex[1])
            vert2 = (vertex[0], 1, vertex[1])
            fid = vertList.index(vertc) + 1
            fid2 = vertList.index(vert2) + 1
            face_array.append(fid)
            oppo_array.append(fid2)

        for vertex in test_data_right:
            vertc = (1, vertex[0], vertex[1])
            vert2 = (0, vertex[0], vertex[1])
            fid = vertList.index(vertc) + 1
            fid2 = vertList.index(vert2) + 1
            face_array.append(fid)
            oppo_array.append(fid2)

        face = ""
        for k in range(len(face_array)):
            face += " " +str(face_array[k])

            if (k+1) % 4 == 0:
                f.write("f "+face + "\n")
                face = ""

        face = ""
        for k in range(len(oppo_array)):
            face += " " +str(oppo_array[len(oppo_array)-1-k])

            if (k+1) % 4 == 0:
                f.write("f "+face + "\n")
                face = ""


    return vertList


if __name__ == '__main__':

    print(generate())
