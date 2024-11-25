# Python program to find 
# maximal Bipartite matching.
 
class GFG:
    def __init__(self,graph):
         
        # residual graph
        self.graph = graph 
        self.ppl = len(graph)
        self.jobs = len(graph[0])
 
    # A DFS based recursive function
    # that returns true if a matching 
    # for vertex u is possible
    def bpm(self, u, matchR, seen):
 
        # Try every job one by one
        for v in range(self.jobs):
 
            # If applicant u is interested 
            # in job v and v is not seen
            if self.graph[u][v] and seen[v] == False:
                 
                # Mark v as visited
                seen[v] = True
 
                '''If job 'v' is not assigned to
                   an applicant OR previously assigned 
                   applicant for job v (which is matchR[v]) 
                   has an alternate job available. 
                   Since v is marked as visited in the 
                   above line, matchR[v]  in the following
                   recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v], 
                                               matchR, seen):
                    matchR[v] = u
                    return True
        return False
 
    # Returns maximum number of matching 
    def maxBPM(self):
        '''An array to keep track of the 
           applicants assigned to jobs. 
           The value of matchR[i] is the 
           applicant number assigned to job i, 
           the value -1 indicates nobody is assigned.'''
        matchR = [-1] * self.jobs
         
        # Count of jobs assigned to applicants
        result = 0
        for i in range(self.ppl):
             
            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs
             
            # Find if the applicant 'u' can get a job
            if self.bpm(i, matchR, seen):
                result += 1
        return result
 
 
bpGraph =[[0, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1]]
 
g = GFG(bpGraph)
 
print ("Maximum number of applicants that can get job is %d " % g.maxBPM())
 
# Function to read employees from file
def read_employees(file_path):
    employees = []
    with open(file_path, 'r') as file:
        for line in file:
            name, occupation, price = line.strip().split(';')
            employees.append((name, occupation, int(price)))
    return employees

# Function to read clients from file
def read_clients(file_path):
    clients = []
    with open(file_path, 'r') as file:
        for line in file:
            name, required_occupation, budget = line.strip().split(';')
            clients.append((name, required_occupation, int(budget)))
    return clients

# Function to create bipartite graph from employees and clients
def create_bipartite_graph(employees, clients):
    graph = [[0 for _ in range(len(clients))] for _ in range(len(employees))]
    for i, (e_name, e_occupation, e_price) in enumerate(employees):
        for j, (c_name, c_required_occupation, c_budget) in enumerate(clients):
            if e_occupation == c_required_occupation and e_price <= c_budget:
                graph[i][j] = 1
    return graph

# Read employees and clients from files
employees = read_employees('empleados.txt')
clients = read_clients('clientes.txt')

# Create bipartite graph
bpGraph = create_bipartite_graph(employees, clients)

# Find maximum matching
g = GFG(bpGraph)
max_matching = g.maxBPM()

# Print results
print("Maximum number of applicants that can get job is %d " % max_matching)
matchR = [-1] * len(clients)
for i in range(len(employees)):
    seen = [False] * len(clients)
    g.bpm(i, matchR, seen)

print("Matchings:")
for j in range(len(clients)):
    if matchR[j] != -1:
        print(f"{clients[j][0]} - {employees[matchR[j]][0]}")


# INICIO
print("Bienvenidx a PerfectMatch")
print("Cargando base de datos...")
print("Base de datos cargada exitosamente")
print("Estos son los resultados:")
