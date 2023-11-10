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
    for i in range (random.randint(0,e)):
        paciente = Paciente()
        paciente.camina = random.choice([True, False])
        paciente.consciente = random.choice([True, False])
        paciente.dolor = random.choice([True, False])
        paciente.respira = random.choice([True, False])
        listaPacientes.append(paciente)
    return listaPacientes

def SalaEsperaVORAZ(colas,tiempo,e):
    listaAtender = queue.Queue()
    elementos=[]
    aux=random.randint(0,e+1)
    for i in range (len(colas)):
        if( not colas[i].empty()):
            elementos.append(colas[i].queue[0])
    for i in range(aux):
        if  elementos:
            paciente= min(elementos, key=lambda x: x.tiempoRestante(tiempo))#si dos son iguales elige al que encontro primero que inevitablemente va a ser de mayor color
            colas[paciente.color].get()#lo elimino
            listaAtender.put(paciente)#lo agrego 
    print(f"Consultorios disponibles= {aux}")
    return listaAtender 

#def SalaEsperaPD(colas):

class Paciente:
    contador=0

    color=0
    consciente = False
    respira = False
    camina = False
    dolor = False
    tiempoIngreso=0
    tiempoAsignado=0
  
    def __init__(self):
        Paciente.contador += 1
        self.numero = Paciente.contador

    def tiempoRestante(self,tiempo):
        return self.tiempoAsignado-(tiempo-self.tiempoIngreso)
   


class Enfermero:
    contador=0
    def __init__(self):
        Enfermero.contador += 1
        self.id = Enfermero.contador

    def TRIAGE(self, Paciente, tiempo, colas):
    
        Paciente.tiempoIngreso= tiempo
        if (not Paciente.consciente and not Paciente.respira):
            Paciente.color=0
            Paciente.tiempoAsignado=0
        if (not Paciente.consciente and Paciente.respira):
            Paciente.color=1
            Paciente.tiempoAsignado=2
        if (Paciente.consciente and not Paciente.camina):
            Paciente.color=2
            Paciente.tiempoAsignado=3
        if (Paciente.consciente and Paciente.camina and Paciente.dolor):
            Paciente.color=3
            Paciente.tiempoAsignado=4
        if (Paciente.consciente and Paciente.camina and not Paciente.dolor):
            Paciente.color=4
            Paciente.tiempoAsignado=5
      
        colas[Paciente.color].put(Paciente)
       
