from src.clases import Paciente, SalaEsperaVORAZ
import queue

def test_PacienteNaranja_Amarillo():#evalua que se atienda al de mayor prioridad(de menor tiempo restante)
 tiempoIngreso=0
 tiempoActual=5

 colas = [queue.Queue() for _ in range(5)] 
 PacientesIngresados = []

 #creo paciente NARANJA
 pNaranja = Paciente()
 pNaranja.tiempoIngreso = tiempoIngreso
 pNaranja.color = 1
 pNaranja.asignarTiempo()

 PacientesIngresados.append(pNaranja)

 #creo paciente AMARILLO
 pAmarillo = Paciente()
 pAmarillo.tiempoIngreso = tiempoIngreso
 pAmarillo.color = 2
 pAmarillo.asignarTiempo()

 PacientesIngresados.append(pAmarillo)

 #los agrego a las respectivas colas
 for i in range(len(PacientesIngresados)):
  colas[PacientesIngresados[i].color].put(PacientesIngresados[i])

 #llamo sala VORAZ
 #intervalo=1, no interfiere si se le acaba el tiempo a algun paciente
 colaFinal = SalaEsperaVORAZ(colas,tiempoActual,1,1)

 PacienteAtender = colaFinal.get()

 assert PacienteAtender.color == 1 

def test_tiempoLimite(): #que al paciente que se le este por acabar el tiempo sea atendido
 tiempoIngreso=0
 tiempoActual=235
 intervalo = 5

 colas = [queue.Queue() for _ in range(5)] 
 
 #creo paciente AZUL
 pAzul = Paciente()
 pAzul.tiempoIngreso = tiempoIngreso
 pAzul.color = 4
 pAzul.asignarTiempo()

 colas[pAzul.color].put(pAzul)

 #llamo sala VORAZ
 colaFinal = SalaEsperaVORAZ(colas,tiempoActual,1,intervalo)
 
 assert colaFinal.empty() == True #el paciente fue atendido en la sala 