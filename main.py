from boltons.setutils import IndexedSet
import pdb; 


generalPath = []
def get_path_child(
    child_elements, 
    end_node, 
    start_node,
    graph, 
    currentElement, 
    alreadyVisited,
    rootNode=False
):
    global generalPath
 
    resultArr = []
    index = 0
    for el in child_elements:
        index = index + 1
        currentElement = el
        if el != start_node:
            if el not in alreadyVisited:
                if el != end_node:

                    alreadyVisited.append(
                        el
                    )

                    przefiltrowana = list(
                        filter(
                            lambda x:
                            x not in alreadyVisited
                            ,
                            graph[el]
                        )
                    )

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

                            if (rootNode):
                                generalPath.append(resultArr)
                                resultArr = []

                            if((index) == len(child_elements)):
                                return resultArr

                else:
                    return currentElement
    generalPath.append(resultArr)
    
def get_paths(graph, start_node, end_node,):
    global generalPath

    alreadyVisited = []

    if start_node and end_node in graph:

        returnedList = get_path_child(
            graph[start_node],
            end_node,
            start_node,
            graph,
            start_node,
            alreadyVisited,
            True
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
