import heapq
import sys

def dijkstra(adj, src):
    v=len(adj)
     # we will be saving in the min heap(priority queue) the distance from the source to the node and the node itself and also other nodes.
    pq=[]
    dist=[sys.maxsize]*v #giving infinity to all the vertices initially
    #distance of a node to itself is 0
    dist[src]=0
    heapq.heappush(pq,(0,src)) #pushing this into the priority queue 
    while pq: #iterating through all the vertices
        d,u=heapq.heappop(pq) # it will be giving the minimum distance and the node
        if d>dist[u]: #ignore the vertices that has already been relaxed
            continue 

        for v,w in adj[u]: #iterating through all the neighbours of the current vertex
            # if we found a shorter path to v through u then  update it
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    # Return the final shortest distances from the source
    return dist

if __name__ == "__main__":
    src = 0
    
    adj = [
    [(1, 7), (2, 12)],
    [(0, 7), (4, 5), (2, 4)],
    [(0, 12), (3, 6), (1, 4)],
    [(2, 6), (4, 9)],
    [(1, 5), (3, 9)]
    ]
    
    result = dijkstra(adj, src)
    print(*result)


