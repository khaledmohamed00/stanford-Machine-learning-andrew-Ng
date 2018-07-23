inf =9999
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

geneSet=['arad',
           'bucharest',
           'craiova',
           'drobeta',
           'eforie',
           'fagaras',
           'giurgiu',
           'hirsova',
           'iasi',
           'lugoj',
           'mahadia',
           'neamt',
           'oradea',
           'pitesti',
           'rimnicu vilcea',
           'sibiu',
           'timisoara',
           'urziceni',
           'vaslui',
           'zerind']

gene_size=5;
import random

def mutate(parent):
    index = random.randrange(0, len(parent))
    child = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    if child[index]==newGene:
       child[index]=alternate
    else:
        child[index] = newGene

    #return ''.join(child)
    return child

def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    #return ''.join(genes)
    return genes


def cross_over(parent1,parent2):
    mi = min(len(parent1), len(parent2))
    n = random.randint(0, mi)
    child1 = parent1[:n] + parent2[n:]
    child2 = parent2[:n] + parent2[n:]
    # print n
    lis = []
    lis.append(parent1)
    lis.append(parent2)
    lis.append(child1)
    lis.append(child2)
    return lis
def getCost(parent,child):
    index=-1
    children=graph[parent]
    for city in children:
        index += 1
        if city[0]==child:
            return city[1]
    return  inf

def cost(member):
    return member[1]

def fitness(population):
    i=0
    lis=[]

    #population=[['arad','sibiu','fagaras'],['mahadia','craiova','fagaras'],['iasi','neamt','vaslui']]
    for pop in population:
        totalcost = 0
        for i in range(0,len(pop)-1,1):
            totalcost+=getCost(pop[i],pop[i+1])
            if(pop[0]!='arad'):
                totalcost+=inf
            if(pop[-1]!='bucharest'):
                totalcost+=inf
        lis.append((pop,totalcost))
    lis.sort(key=cost)
    return lis
parent1 = generate_parent(gene_size)
parent2 = generate_parent(gene_size)
parent3 = generate_parent(gene_size)
parent4 = generate_parent(gene_size)
history=0
j=0
opt=366
while True:

    j=j+1
    #print j
    lis= cross_over(parent1,parent2)
    lis+=cross_over(parent3,parent4)

    fit=[]
    fit=fitness(lis)

    if random.randint(0,100)%4:
        #parent1=mutate(fit[0][0])
        parent1 = mutate(fit[0][0])
        parent2 =mutate(fit[1][0])
        parent3 = mutate(fit[0][0])
        parent4 = mutate(fit[1][0])
    else:
        parent1=fit[0][0]
        parent2=fit[1][0]
        parent3 = fit[0][0]
        parent4 = fit[1][0]
    #if fit[0][1]>history:
     # history+=1

    print fit[0]
    print j
    if fit[0][1]>opt and fit[0][1]<inf :
        print fit[0][0]
        print fit[0][1]
        print j
        break