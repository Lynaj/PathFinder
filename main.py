from boltons.setutils import IndexedSet
import pdb; 


generalPath = []
def get_path_child(
    child_elements, 
    end_node, 
    start_node,
    graph, 
    currentElement, 
    alreadyVisited
):
    global generalPath
 
    resultArr = []
    print('child_elements : ' + str(child_elements))
    for el in child_elements:
        print('****************************')
        print('****************************')
        print('****************************')
        print('****************************')
        # pdb.set_trace()
        print("EL: " + str(el))
        currentElement = el
        if el != start_node:
            if el not in alreadyVisited:
                
                # pdb.set_trace()

                alreadyVisited.append(
                    el
                )

                print('alreadyVisited: ' + 
                    str(
                        alreadyVisited
                    )
                )
                if el != end_node:

                    print(
                        'el: '
                        +
                        str(el)
                        +
                        ' currentElement: '
                        + str(currentElement)
                        +
                        ' przerabiam: ' 
                        +
                        str(
                            graph[el]
                        )
                    )

                    przefiltrowana = list(
                        filter(
                            lambda x:
                            x not in alreadyVisited
                            ,
                            graph[el]
                        )
                    )

                    print('przefiltrowana: ' + str(przefiltrowana))

                    if(
                        len(
                            przefiltrowana
                        ) > 0
                    ):
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
                            and 
                            result != False
                        ):
                            
                            resultArr += result
                            resultArr += el
                            
                            return resultArr
                    # else:
                        # return False

                else:
                    return currentElement
            # else:
                # print("el not in alreadyVisited" + str(el not in alreadyVisited))
        
# if(len(resultArr) > 0):
    generalPath.append(resultArr)
    
def get_paths(graph, start_node, end_node,):
    global generalPath

    alreadyVisited = []

    if start_node and end_node in graph:
        
        # for el in graph[start_node]:

            # alreadyVisited.append(el)

            # pdb.set_trace()
        returnedList = get_path_child(
            graph[start_node],
            end_node,
            start_node,
            graph,
            start_node,
            alreadyVisited
        )

        if(len(returnedList) > 0):
            generalPath.append(
                returnedList    
            )

    return generalPath

'''
A -> B -> E -> F
A -> C -> F
'''

if __name__ == "__main__":

    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print(get_paths(graph, 'A', 'F'))
