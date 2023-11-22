
import random 
import queue


def generadorEnfermeros(cant):
    listaEnfermeros=[]
    for i in range (cant):
        enfermero=Enfermero()
        listaEnfermeros.append(enfermero)
    return listaEnfermeros

def generadorPacientes(e):
    listaPacientes=[]
    for i in range (random.randint(0,2*e)):
        paciente = Paciente()
        paciente.lista_sintomas = [True, True, False, False, False, False, True]#verde
        """
        #trabajo con las probabilidades de tener cada sintoma
        valoresROJO = [True,False]
        probabilidadesROJO = [0.9, 0.1]
        paciente.lista_sintomas[0]= random.choices(valoresROJO, probabilidadesROJO, k=1)

        paciente.lista_sintomas[1]= random.choice([True, False])
        paciente.lista_sintomas[2]= random.choice([True, False])
        paciente.lista_sintomas[3]= random.choice([True, False])
        paciente.lista_sintomas[4]= random.choice([True, False])
        paciente.lista_sintomas[5]= random.choice([True, False])
        paciente.lista_sintomas[6]= random.choice([True, False])
        """
     
        
        listaPacientes.append(paciente) #lo agrego a la lista final 
    return listaPacientes

def SalaEsperaVORAZ(colas,tiempo,e):
    listaAtender = queue.Queue()
    elementos=[]
    aux=random.randint(0,e+1)
    print(f"Consultorios disponibles= {aux}")
    if(aux == 0):
        return listaAtender
    for i in range (len(colas)):
        if( not colas[i].empty()):
            elementos.append(colas[i].queue[0])
    for i in range(aux):#aca hay un problema, me agrega lo que hay en elementos dos veces
        if  elementos or i<len(elementos):
            paciente= min(elementos, key=lambda x: x.tiempoRestante(tiempo))#si dos son iguales elige al que encontro primero que inevitablemente va a ser de mayor color
            colas[paciente.color].get()#lo elimino
            listaAtender.put(paciente)#lo agrego 
  
    return listaAtender 

#def SalaEsperaPD(colas):

class Paciente:
    contador=0

    color=0
    lista_sintomas=[False, False, False, False, False, False, False]
    #lista_sintomas=[respira, conciente, hemorragia, hipertension, disfuncion motora, delirio, dolor]
    tiempoIngreso=0
    tiempoAsignado=0
  
    def __init__(self):
        Paciente.contador += 1
        self.numero = Paciente.contador
    
    def asignarTiempo(self):
        if self.color == 0:#ROJO
             self.tiempoAsignado = 0
        elif self.color == 1:#NARANJA
             self.tiempoAsignado = 10
        elif self.color == 2:#AMARILLO
             self.tiempoAsignado = 60
        elif self.color == 3:#VERDE
             self.tiempoAsignado = 120
        elif self.color == 4:#AZUL
             self.tiempoAsignado = 240

    def tiempoRestante(self,tiempo):
        return self.tiempoAsignado-(tiempo-self.tiempoIngreso)
   
class Nodo:
    def __init__(self, sintoma, color=None, izquierda=None, derecha=None):
        self.sintoma = sintoma
        self.color = color
        self.izquierda = izquierda
        self.derecha = derecha

#construyo el arbol
def construir_arbol():
    #ROJO=0, NARANJA=1, AMARILLO=2, VERDE=3, AZUL=4
    
    nodo_1 = Nodo(sintoma="Respira", color=None)
    nodo_2 = Nodo(sintoma=None, color=0)  # Nodo hoja con color rojo
    nodo_3 = Nodo(sintoma="Conciente", color=None)
    nodo_4 = Nodo(sintoma=None, color=1)  # Nodo hoja con color naranja
    nodo_5 = Nodo(sintoma="Hemorragia", color=None)
    nodo_6 = Nodo(sintoma=None, color=1)  # Nodo hoja con color naranja
    nodo_7 = Nodo(sintoma="Hipertension", color=None)
    nodo_8 = Nodo(sintoma=None, color=2)  # Nodo hoja con color amarillo
    nodo_9 = Nodo(sintoma="Disfuncion motora", color=None)
    nodo_10 = Nodo(sintoma=None, color=2)  # Nodo hoja con color amarillo
    nodo_11 = Nodo(sintoma="Delirio", color=None)
    nodo_12 = Nodo(sintoma=None, color=2)  # Nodo hoja con color amarillo
    nodo_13 = Nodo(sintoma="Dolor", color=None)
    nodo_14 = Nodo(sintoma=None, color=3)  # Nodo hoja con color verde
    nodo_15 = Nodo(sintoma=None, color=4)  # Nodo hoja con color azul

    nodo_1.izquierda = nodo_2
    nodo_1.derecha = nodo_3
    nodo_3.izquierda = nodo_4
    nodo_3.derecha = nodo_5
    nodo_5.izquierda = nodo_7
    nodo_5.derecha = nodo_6
    nodo_7.izquierda = nodo_9
    nodo_7.derecha = nodo_8
    nodo_9.izquierda = nodo_11
    nodo_9.derecha = nodo_10
    nodo_11.izquierda = nodo_13
    nodo_11.derecha = nodo_12
    nodo_13.izquierda = nodo_15
    nodo_13.derecha = nodo_14

    return nodo_1  #devuelvo la raiz del arbol

mapeo_sintomas = {
    "Respira": 0,
    "Conciente": 1,
    "Hemorragia": 2,
    "Hipertension": 3,
    "Disfuncion motora": 4,
    "Delirio": 5,
    "Dolor": 6,
}


# funcion que evalua los sintomas del paciente y devuelve un color
def evaluar_paciente(paciente, nodo_actual, mapeo_sintomas):

    if nodo_actual.sintoma is not None:  #verifica que el nodo tenga asignado un sintoma
        sintoma_actual = nodo_actual.sintoma 
        indice_sintoma = mapeo_sintomas.get(sintoma_actual)#obtiene el indice en el que se encuentra en sintoma en la lista de sintomas 
        
      
        if paciente.lista_sintomas[indice_sintoma]:  #accedo al sintoma en la lista del paciente
            if nodo_actual.derecha: #verifico que tenga subarbol der
               return evaluar_paciente(paciente, nodo_actual.derecha, mapeo_sintomas) #lo analizo
        else:
           
            if nodo_actual.izquierda: #verifico que tenga un subarbol izq
               return evaluar_paciente(paciente, nodo_actual.izquierda, mapeo_sintomas)#analizo el subarbol izq
      
    else:
        return nodo_actual.color #caso base, que el nodo_actual sea un color




class Enfermero:
    contador=0
    def __init__(self):
        Enfermero.contador += 1
        self.id = Enfermero.contador

    def TRIAGE(self, paciente, tiempo, colas, arbol_TRIAGE):#que reciba arbol_TRIAGE
    
        paciente.tiempoIngreso= tiempo #asigno el tiempo de ingreso

        #llamo a evaluar paciente
        color=evaluar_paciente(paciente, arbol_TRIAGE, mapeo_sintomas)

        paciente.color=color #asigno color

        paciente.asignarTiempo() #asigno tiempo de espera maximo

        colas[paciente.color].put(paciente)#lo agrego a la cola correspondiente
       
