# Entregable 3: Natalia Carpintero, Paula Nuñez e Isabella Arrieta.

class PerfectMatch: # Clase principal
    def __init__(self,archivo_empleados, archivo_clientes):
        self.empleados = self.leer_empleados(archivo_empleados)
        self.clientes = self.leer_clientes(archivo_clientes)
        self.grafo= self.crear_grafo()

    def leer_empleados(self,archivo_empleados): # Función para leer empleados.txt
        empleados = []
        with open(archivo_empleados, 'r') as file: #abrir archivo
            for line in file:
                nombre, ocupacion, precio_hora= line.strip().split(';') #separar por ;
                empleados.append((nombre, ocupacion, float(precio_hora)))
        return empleados
    
    def leer_clientes(self, archivo_clientes): # Función para leer clientes.txt
        clientes = []
        with open(archivo_clientes, 'r') as file:
            for line in file:
                nombre, ocupacion_requerida, presupuesto= line.strip().split(';')
                clientes.append((nombre, ocupacion_requerida, float(presupuesto)))
        return clientes
            
    def crear_grafo(self): # Grafo ()
        grafo = [[0] * len(self.clientes) for _ in range(len(self.empleados))] # Matriz de ceros
        for i, empleado in enumerate(self.empleados):
            for j, cliente in enumerate(self.clientes):
                if empleado[1] == cliente[1] and empleado[2] <= cliente[2]:
                    grafo[i][j] = 1
        return grafo
 
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
 













# INICIO
print("Bienvenidx a PerfectMatch")
print("Cargando base de datos...")
print("Base de datos cargada exitosamente")
print("Estos son los resultados:")
