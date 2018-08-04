import random
inf=9999
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

city_list=['arad',
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

#generate random parents or cromosomes from city list
def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(city_list))
        genes.extend(random.sample(city_list, sampleSize))
    return genes

#generate intial population
def get_intial_population(set_number,gene_size):
    chunks=[]
    '''
     n= len(city_list)/set_number
     r=len(city_list)%set_number

     chunks = [city_list[x:x + n] for x in range(0, len(city_list), n)]
     if r !=0:
         l=chunks[-1]+chunks[-2]
         #print len(chunks)
         chunks.pop(-1)
         chunks.pop(-2)
        #print len(chunks)
         chunks.append(l)
     '''
    for i in range(0,set_number):
        chunks.append(generate_parent(gene_size))
    return chunks

#perform mutation operation by randomly change a city(gene) with another
def mutate(parent):
    child=[]
    for gene in parent:
        index = random.randrange(0, len(gene))
        newGene, alternate = random.sample(city_list, 2)
        if gene[index] == newGene:
            gene[index] = alternate
        else:
            gene[index] = newGene
        child.append(gene)
    return child

#perform crossover operation between two set of cities (cromosomes)
def cross_over(parent1,parent2):
    lis=[]
    mi=min(len(parent1),len(parent2))
    n=random.randint(0,mi)
    child1=parent1[:n]+parent2[n:]
    child2=parent2[:n]+parent1[n:]
    lis.append(child1)
    lis.append(child2)
    lis.append(parent1)
    lis.append(parent2)
    return lis

#get the cost of a solution, by checking if the path is connected, if so return the cost, if not return infinity
def getCost(parent,child):
    index=-1
    children=graph[parent]
    for city in children:
        index += 1
        if city[0]==child:
            return city[1]
    return  inf

#used as a key in sorting each generation
def cost(member):
    return member[1]

#Computes the fitness function
def fitness(population):
    i=0
    lis=[]

   # population=[['arad','sibiu','fagaras'],['mahadia','craiova','fagaras'],['iasi','neamt','vaslui']]
    for pop in population:
        totalcost = 0
        for i in range(0,len(pop)-1,1):
            totalcost+=getCost(pop[i],pop[i+1])
            if(pop[0]!='arad'):
                totalcost+=inf
            if(pop[-1]!='bucharest'):
                totalcost+=inf
            if(pop[i] in pop[i+1:]):
                totalcost+=inf
        lis.append((pop,totalcost))
    lis.sort(key=cost)
    return lis

def start():
    set_number = 200            #number of intial population
    gene_size = 5               #Size of cromosome(solution size),number of genes
    intial_population = get_intial_population(set_number, gene_size)
    generation_count = 0
    while True:
        new_generation = []
        next_generation = []
        for i in range(0, set_number, 2):
            new_generation += (cross_over(intial_population[i], intial_population[i + 1]))
        if random.randint(0, 100) % 4:
            new_generation = mutate(new_generation)
        generations = fitness(new_generation)
        top = generations[0][1]
        for cromosome in generations[0:set_number]:
            next_generation.append(cromosome[0])
        intial_population = next_generation
        print 'iteration', generation_count
        print intial_population
        generation_count += 1
        if top < inf:
            break
start()
