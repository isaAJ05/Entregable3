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
    # for vertex u is possible (Fuente: https://www.geeksforgeeks.org/maximum-bipartite-matching/)
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
           indice del empleado asignado al cliente 'v', 
           el valor -1 indica que no se le ha asignado a nadie.'''
        matchR = [-1] * self.clientes
        result = 0 # Contador de emparejamientos asignados
        for i in range(len(self.empleados)):
            # Marcar todos los clientes como no vistos para la siguiente iteración
            seen = [False] * self.clientes
            # Si el empleado 'i' puede ser asignado a un cliente
            if self.bpm(i, matchR, seen):
                result += 1 # Se incrementa el contador de emparejamientos
        return matchR, result # Se retorna lista de emparejamientos y cantidad de emparejamientos
 
    def output(self):
            matchR, total = self.max_bipartite_matching()
            emparejamientos = []
            for j in range(len(self.clientes)):
                if matchR[j] != -1:
                    emparejamientos.append(f"{self.clientes[j][0]} - {self.empleados[matchR[j]][0]}")
            print("Emparejamientos:")
            for emp in emparejamientos:
                print(emp)
            print(f"Total de emparejamientos realizados: {total}")
    

 













# INICIO
print("Bienvenidx a PerfectMatch")
print("Cargando base de datos...")
print("Base de datos cargada exitosamente")
print("Estos son los resultados:")
