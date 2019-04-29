
def get_path_child(child_elements, end_node, start_node, graph, currentElement, alreadyVisited):
 
    resultArr = []
    
    for el in child_elements:
        if el != start_node:
            if el not in alreadyVisited:
                
                alreadyVisited.append(
                    el
                )

                if el != end_node:

                    result = get_path_child(
                        graph[el],
                        end_node,
                        start_node,
                        graph,
                        currentElement,
                        alreadyVisited
                    ) 
                    if (
                        result != None
                    ):
                        
                        resultArr += result
                        resultArr += el
                        
                        return resultArr
                else:
                    return currentElement
            else:
                print("el not in alreadyVisited" + str(el not in alreadyVisited))
    
    if(len(resultArr) > 0):
        return resultArr
    
def get_paths(graph, start_node, end_node,):
    
    generalPath = []
    alreadyVisited = []

    if start_node and end_node in graph:
        
        for el in graph[start_node]:
            generalPath.append(
                get_path_child(
                    graph[el],
                    end_node,
                    start_node,
                    graph,
                    el,
                    alreadyVisited
                )
            )

    return generalPath
    


if __name__ == "__main__":

    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    
    print(get_paths(graph, 'A', 'F'))
