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
            
    def crear_grafo(self): # Grafo (matriz de adyacencia)
        grafo = [[0] * len(self.clientes) for _ in range(len(self.empleados))] # Matriz de ceros
        for i, empleado in enumerate(self.empleados): # Recorrer empleados
            for j, cliente in enumerate(self.clientes): # Recorrer clientes
                # Si la ocupación del empleado es igual a la ocupación requerida del cliente y el precio del empleado es menor o igual al presupuesto del cliente
                if empleado[1] == cliente[1] and empleado[2] <= cliente[2]: 
                    grafo[i][j] = 1 # Se asigna un 1 en la matriz (hay una arista/relación)
        return grafo
 
    # A DFS based recursive function
    # that returns true if a matching 
    # for vertex u is possible (Fuente: GeeksforGeeks)
    def bpm(self, u, matchR, seen): # Función Bipartite Matching 
        # Probar cada cliente
        for v in range(len(self.clientes)):
            # Si hay una arista entre u(empleado) y v(cliente) y v no se ha visto 
            if self.grafo[u][v] and seen[v] == False:
                # Se marca como visitado el cliente
                seen[v] = True
                '''Si el cliente 'v' no está asignado a ningun empleado (en la lista el indice es -1). 
                   O si el cliente 'v' ya está asignado a otro empleado, se encuentra
                   un nuevo emparejamiento para el empleado actualmente asignado al cliente 'v'
                   osea se hace el llamado recursivo'''
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u # si se cumplen las condiciones, se le asigna el cliente 'v' al empleado 'u'
                    return True # Se retorna verdadero (hay emparejamiento!)
        return False
 
    
    def maxBPM(self):
        '''Una lista que mantiene el seguimiento de los
           clientes asignados a los empleados. 
           El valor de matchR[i] es el
           numeris the 
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
