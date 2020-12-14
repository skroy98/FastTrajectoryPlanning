import ClassNode
import repeatedA
def adaptiveAStar(grid, openedSet, closedSet, start, end, test):

    pathLength = len(repeatedA.repeatedAStar(grid, openedSet, closedSet, start, end, test))
    start_Timer = ClassNode.timeit.default_timer()
    while(len(closedSet) > 0):
        temp1 = closedSet.pop()
        #temp1.h = end.g - temp1.g
        #temp1.f = temp1.h + temp1.g
        temp1.adjust = True #marking the nodes which were expanded


    test = []

    ClassNode.heapq.heappush(test, (start.f, start))
    count = 0
    counter = 0
    done = False
    while len(test) > 0:
        curr = test[0][1]
        ClassNode.heapq.heappop(test)
        count += 1

        if curr == end:
            done = True
            pathSet1 = []
            temp = curr
            while (temp.prev):
                pathSet1.append(temp.prev)
                temp = temp.prev
            print("DONE")
            end_Timer = ClassNode.timeit.default_timer()
            time = end_Timer - start_Timer
            print("Time of Algorithm: ", time)
            return pathSet1

        # print("pop", pop)
        # print("list: ", test)
        if curr in closedSet:
            continue

        closedSet.append(curr)
        # for i in range(len(closedSet)):
        # print("closed : ", closedSet[i].i, closedSet[i].j)

        node_Neighbors = curr.neighbors  # get all neighbors

        # check every neighbor
        for i in range(len(node_Neighbors)):
            node_Neighbor = node_Neighbors[i]

            if node_Neighbor not in closedSet and node_Neighbor.value != 1:
                tempG = curr.g + 1  # heuristic(node_Neighbor, current)

                if tempG < node_Neighbor.g or node_Neighbor not in test:
                    # if adjust:
                    #node_Neighbor.g = tempG
                    #node_Neighbor.f = node_Neighbor.h - node_Neighbor.g
                    # else:
                    node_Neighbor.g = tempG
                    # pathLength - node_Neighbor.g
                    if(node_Neighbor.adjust): #Checking if the new node was in the previous closed set
                        node_Neighbor.h = pathLength - node_Neighbor.g
                    node_Neighbor.f = node_Neighbor.h + node_Neighbor.g
                    if (node_Neighbor not in test):
                        ClassNode.heapq.heappush(test, (node_Neighbor.f, node_Neighbor))

    if done == False:
        print("Path Not Found")
        return
    return False