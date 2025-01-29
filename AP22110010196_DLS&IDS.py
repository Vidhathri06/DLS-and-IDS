from collections import defaultdict
def graph():
    graph=defaultdict(list)
    edges={
        'a':[('b',9),('c',4),('d',7)],
        'b':[('e',11)],
        'c':[('f',17)],
        'd':[('f',12)],
        'e':[('z',5)],
        'f':[('z',9)]
    }
    for node,neighbors in edges.items():
        for neighbor,cost in neighbors:
            graph[node].append(neighbor)
    return graph
def dls(graph,node,target,depth,path):
    path.append(node)
    print(f"Visiting Node:{node},Depth:{depth},Path:{path}")
    if node==target:
        print(f"Goal Node '{target}'Found! Path:{path}")
        return True
    if depth==0:
        path.pop()
        return False
    for neighbor in graph.get(node,[]):
        if dls(graph,neighbor,target,depth-1,path):
            return True
    path.pop()
    return False
def ids(graph,start,target,max_depth):
    for depth in range(max_depth+1):
        print(f"Performing IDS with depth limit {depth}")
        path=[]
        if dls(graph,start,target,depth,path):
            return f"Target '{target}' found at depth {depth} with path{path}"
    return f"Target '{target}' not found within depth {max_depth}"
if __name__=="__main__":
    graph=graph()
    source='a'
    target='e'
    depth_limit=2
    print(f"DLS Result (l={depth_limit}):",dls(graph,source,target,depth_limit,[]))
    print("IDS Result:",ids(graph,source,target,depth_limit))
