import ClassNode
import repeatedA
import adaptive
import os

height = ClassNode.height
width = ClassNode.width
reverse = False  #true for backward repeated A*
Adaptive = True #true for adaptive


lines = [[int(v) for v in line.split()]
         for line in open('10.txt')] #insert appropriate directory of generated maze.

# 2D array
cols = []

# A*algo variables
openedSet = []
closedSet = []
pathSet = []

test = []

cols = ClassNode.createGrid(lines, width, height)



# start and end indexes for cols grid
start = cols[0][0]
end = cols[width-1][height-1]
cols = ClassNode.loadNeighbors(cols, width, height)

#print(ClassNode.sys.getsizeof(cols[100][100])) #gets bytes used by one cell

if reverse:
    end.g = 0
    end.h = ClassNode.heuristic(end, start)
    end.f = end.g + end.h
    start_Timer = ClassNode.timeit.default_timer()
    ClassNode.heapq.heappush(test, (end.f, end))
    pathSet = repeatedA.repeatedAStar(cols, openedSet, closedSet, end, start, test)
    end_Timer = ClassNode.timeit.default_timer()
    time = end_Timer - start_Timer
    #average += time
else:
    start.g = 0
    start.h = ClassNode.heuristic(start, end)
    start.f = start.g + start.h
    if Adaptive:
        ClassNode.heapq.heappush(test, (start.f, start))
        pathSet = adaptive.adaptiveAStar(cols, openedSet, closedSet, start, end, test)
    else:
        start_Timer = ClassNode.timeit.default_timer()
        ClassNode.heapq.heappush(test, (start.f, start))
        pathSet = repeatedA.repeatedAStar(cols, openedSet, closedSet, start, end, test)
        end_Timer = ClassNode.timeit.default_timer()
        time = end_Timer - start_Timer

if not Adaptive:
    print("Time of Algorithm: ", time)
print("Number of Expansions: " , len(closedSet))
print("Path Length: ", len(pathSet))
ClassNode.updateGrid(cols, pathSet)
#ClassNode.printGrid(cols, width, height)  # final path is labeled as 8 in cols
print("Done")


if(reverse):
    start.value = 6
    end.value = 3
else:
    start.value = 3
    end.value = 6

zvals = []

for i in range(width):
     zvals1 = []
     for j in range(height):
        zvals1.append(cols[i][j].value)
     zvals.append(zvals1)


cmap = ClassNode.mpl.colors.ListedColormap(['white', 'black', 'green', 'red', 'yellow'])
bounds = [0, 0.5, 2, 5, 7, 10]
norm = ClassNode.mpl.colors.BoundaryNorm(bounds, cmap.N)

img = ClassNode.pyplot.imshow(zvals, interpolation='nearest',
                     cmap=cmap, norm=norm)

ClassNode.pyplot.show()