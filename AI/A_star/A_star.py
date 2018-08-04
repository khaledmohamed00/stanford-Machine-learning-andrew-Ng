import heapq

graph={
    'arad':[('zerind',75),('timisoara',118),('sibiu',140)],
    'zerind': [('arad', 75), ('oradea', 71)],
    'timisoara': [('arad', 118), ('lugoj', 111)],
    'sibiu': [('arad', 140), ('oradea', 151), ('fagaras', 99), ('rimnicu vilcea', 80)],
    'oradea': [('zerind', 71), ('sibiu', 151)],
    'lugoj': [('timisoara', 111), ('mahadia', 70)],
    'fagaras': [('sibiu', 99), ('bucharest', 211)],
    'rimnicu vilcea': [('sibiu', 80), ('pitesti', 97), ('craiova', 146)],
    'mahadia': [('lugoj', 70), ('drobeta', 75)],
    'bucharest': [('fagaras', 211), ('pitesti', 101), ('giurgiu', 90), ('urziceni', 85)],
    'pitesti': [('rimnicu vilcea', 97), ('craiova', 138), ('bucharest', 101)],
    'craiova': [('drobeta', 120), ('rimnicu vilcea', 146), ('pitesti', 138)],
    'drobeta': [('craiova', 120), ('mahadia', 75)],
    'giurgiu': [('bucharest', 90)],
    'urziceni': [('bucharest', 85), ('hirsova', 98), ('vaslui', 142)],
    'hirsova': [('urziceni', 98), ('eforie', 86)],
    'vaslui': [('iasi', 92), ('urziceni', 142)],
    'eforie': [('hirsova', 86)],
    'iasi': [('neamt', 87), ('vaslui', 92)],
    'neamt': [('iasi', 87)]
}

heuristic={'arad': 366,
           'bucharest': 0,
           'craiova': 160,
           'drobeta': 242,
           'eforie': 161,
           'fagaras': 176,
           'giurgiu': 77,
           'hirsova': 151,
           'iasi': 226,
           'lugoj': 244,
           'mahadia': 241,
           'neamt': 234,
           'oradea': 380,
           'pitesti': 100,
           'rimnicu vilcea': 193,
           'sibiu': 253,
           'timisoara': 329,
           'urziceni': 80,
           'vaslui': 199,
           'zerind': 374,
           }
#key=None

class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)



explored=[]

def parent_cost(parent):

   if parent=='arad':
       return 0

   for item in explored:
       if item[0]==parent:

          return item[1]






visited=[]

def A_star():

    visited.append(('arad',None))

    explored.append(('arad',0))
    qu=PriorityQueue()
    child=graph['arad']
    for item in child:
       if item[0] not in visited:
         explored.append((item[0],parent_cost('arad')+item[1]))
         qu.push((item[0],'arad'),heuristic[item[0]]+parent_cost('arad')+item[1])

    while(qu.isEmpty()==False ):
      nod=qu.pop()
      #print nod
      visited.append(nod)
      if nod[0]=='bucharest':
        break


      child=graph[nod[0]]
      for item in child:
        if item[0] not in visited:
            explored.append((item[0], parent_cost(nod[0]) + item[1]))
            qu.push((item[0],nod[0]), heuristic[item[0]] +parent_cost(nod[0])+item[1])



path = []
def get_path(city):



    if city==None:
        return
    for item in visited:

        if item[0]==city:

            path.append(item[0])

            get_path(item[1])
            break



A_star()
get_path('bucharest')
print path[::-1]