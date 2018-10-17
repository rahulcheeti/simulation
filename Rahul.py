import random
import matplotlib.pyplot as plt


G = {1:[2],
     2:[1,3,4,5],
     3:[2,4],
     4:[2,3,5],
     5:[2,4]}


def edges_in_graph(graph):
    e = 0
    for node in graph:
        e += len(graph[node])
    return e/2

def get_birth_probablity(graph):
    node_prob = {}
    j = 0
    k = edges_in_graph(graph)*2
    for node in graph:
        j += len(graph[node])/k
        node_prob[node] = j
    return node_prob

def get_death_probablity(graph):
    node_prob = {}
    j = 0
    k = (len(graph)*len(graph))-(edges_in_graph(graph)*2)
    for node in graph:
        j += (len(graph)-len(graph[node]))/k
        node_prob[node] = j
    return node_prob

def get_random():
    rand = random.uniform(0,1)
    return rand

def birth_process(t,graph):
    rand = get_random()
    node_prob = get_birth_probablity(graph)
    for select_node in node_prob:
        if (node_prob[select_node] >= rand):
            graph[t] = [select_node]
            graph[select_node].append(t)
            break

def death_process(graph):
    rand = get_random()
    node_prob = get_death_probablity(graph)
    for select_node in node_prob:
        if (node_prob[select_node] >= rand):
            for nodes in graph[select_node]:
                graph[nodes].remove(select_node)
            del graph[select_node]
            break

def process(threshold,t,graph):
    rand = get_random()
    if rand <= threshold:
        birth_process(t,graph)
    else:
        death_process(graph)

def simulation(graph,threshold):
    time = []
    nodes = []
    edges = []
    graph_prob = graph
    for t in range(6,10001):
        process(threshold,t,graph_prob)
        if (t%1000 == 0):
            time.append(t)
            nodes.append(len(graph_prob))
            edges.append(edges_in_graph(graph_prob))
    return nodes, edges, time

def cumulative_prob(graph):
    node_prob = []
    degree = {}
    for node in graph:
        node_prob.append(len(graph[node]))
    for node in node_prob:
        if node not in degree:
            degree[node] = 1
        else:
            degree[node] = degree[node] + 1
    for node in degree:
        degree[node] /= len(graph)
    degree = dict(sorted(degree.items(),reverse=True))
    j = 0
    for node in degree:
        j += degree[node]
        degree[node] = j
    return degree

def distribution(graph,threshold):
    graph_prob = graph
    degree = {}
    for t in range(6,10001):
        process(threshold,t,graph_prob)
    degree = cumulative_prob(graph_prob)
    return degree

nodes1,edges1,time1 = simulation(G,0.7)
G = {1:[2],
     2:[1,3,4,5],
     3:[2,4],
     4:[2,3,5],
     5:[2,4]}
nodes2,edges2,time2 = simulation(G,0.8)
G = {1:[2],
     2:[1,3,4,5],
     3:[2,4],
     4:[2,3,5],
     5:[2,4]}
nodes3,edges3 ,time3= simulation(G,0.9)

line1 = plt.plot(time1,nodes1,time2,nodes2,time3,nodes3)
plt.axis([0, 10000, 0, 10000])
plt.text(2000,8000,'P=0.9\nP=0.8\nP=0.7')
plt.title('No of nodes VS time  for three different values of birth probablity P')
plt.xlabel('Time')
plt.ylabel('No. of Nodes')
plt.show(line1)

line2 = plt.plot(time1,edges1,time2,edges2,time3,edges3)
plt.axis([0, 10000, 0, 10000])
plt.text(2000,8000,'P=0.9\nP=0.8\nP=0.7')
plt.title('No of edges VS time for three different values of birth probablity P')
plt.xlabel('Time')
plt.ylabel('No. of Edges')
plt.show(line2)

G = {1:[2],
     2:[1,3,4,5],
     3:[2,4],
     4:[2,3,5],
     5:[2,4]}
degree1 = distribution(G,0.8)
plot1 = plt.plot(*zip(*sorted(degree1.items())))
plt.title('Cumulative degree distribution with P=0.8 after t=10000 ')
plt.xlabel('k')
plt.ylabel('P(k)')
plt.xscale('log')
plt.yscale('log')
plt.show(plot1)



