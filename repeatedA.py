import ClassNode


def repeatedAStar(grid, openedSet, closedSet, start, end, test):
    count = 0
    counter = 0
    done = False

    while len(test) > 0:
        curr = test[0][1]
        ClassNode.heapq.heappop(test)
        count += 1
        if curr == end:
            closedSet.append(curr)
            done = True
            pathSet1 = []
            temp = curr
            while(temp.prev):
                pathSet1.append(temp.prev)
                temp = temp.prev
            print("DONE")
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
                    node_Neighbor.prev = curr
                    node_Neighbor.g = tempG
                    node_Neighbor.h = ClassNode.heuristic(node_Neighbor, end)
                    node_Neighbor.f = node_Neighbor.g + node_Neighbor.h
                    if(node_Neighbor not in test):
                        ClassNode.heapq.heappush(
                            test, (node_Neighbor.f, node_Neighbor))

    if done == False:
        print("Path Not Found")
        return
    return False
