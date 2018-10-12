def find_starting_node(n, incoming_edges, outgoing_edges):
    current_node = n[0]
    path = []
    while True:
        if len(incoming_edges[current_node]) == 0:
            return current_node
        if current_node in path:
            path = [current_node] + path
            return path
        path = [current_node] + path
        current_node = incoming_edges[current_node][0]

def remove_node(node, n, incoming_edges, outgoing_edges):
    n.remove(node)
    incoming_edges.pop(node)
    outgoing_edges.pop(node)
    for k, v in incoming_edges.items():
        if node in v:
            v.remove(node)
        incoming_edges[k] = v
    for k, v in outgoing_edges.items():
        if node in v:
            v.remove(node)
        outgoing_edges[k] = v

def topsort(n, incoming_edges, outgoing_edges):
    num_elts = len(n)
    sorted_order = []
    while len(sorted_order) < num_elts:
        start = find_starting_node(n, incoming_edges, outgoing_edges)
        if type(start) == list:
            return start
        sorted_order.append(start)
        remove_node(start, n, incoming_edges, outgoing_edges)
    return sorted_order


n = [0, 1, 2, 3]
outgoing_edges = {
    3: [0, 1, 2],
    2: [1],
    1: [3],
    0: [1, 2]
}
incoming_edges = {
    0: [3],
    1: [0, 2],
    2: [0, 3],
    3: [1]
}

print(topsort(n, incoming_edges, outgoing_edges))