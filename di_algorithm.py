#创建散列表
#将节点的所有邻居都存储在散列表中
graph = {}
graph["start"] = {}#是一个散列表
graph["start"]["a"] = 6
graph["start"]["b"] = 2
#print(graph["start"].keys())    #获取起点的所有邻居
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {} #终点没有任何邻居

#用一个散列表来存储每个节点的开销
infinity = float("inf") #表示无穷大
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#存储父节点的散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

#需要一个数组，用于记录处理过的节点，因为对于同一个节点，你不用处理多次
processed = []

#find_lowest_cost_node函数
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

#算法实现
node = find_lowest_cost_node(costs) #在未处理的节点中找出开销最小的节点
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
            processed.append(node)
    node = find_lowest_cost_node(costs)
    
print(costs["fin"])
print(parents["fin"])