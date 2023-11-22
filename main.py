import queue
#import time
from src.clases import generadorEnfermeros, generadorPacientes, SalaEsperaVORAZ, construir_arbol

#variables globales
horas_dia = 24
minutos_por_hora = 60
minutos_intervalo = 5

ref1=23
ref2=6
ref3=10
ref4=16

def main() -> None: 
  arbol_TRIAGE = construir_arbol()

  colores = ["ROJO","NARANJA","AMARILLO","VERDE","AZUL"]

  colas = [queue.Queue() for _ in range(5)]  # declaro una lista de 5 colas vacias

  listaAtender=[]

  listaEnfermeros=generadorEnfermeros(5)

  j=0 #indice  asignado a los enfermeros atendiendo, si el dia recien empieza, se incializa en 0

  tiempo = 0

  e=0 #cant enfermeros

  contadorP=0 #contador de pacientes en la sala
 
  while tiempo <= horas_dia * minutos_por_hora:
   horas= tiempo // minutos_por_hora
   #minutos= tiempo % minutos_por_hora

   print("-------------")
   print(f"Tiempo = {tiempo}")

   #segun la franja horaria se definen los enfermeros 
   if (horas>ref1 or horas<=ref2):
    e=1
   elif (ref2<horas<=ref3):
    e=2
   elif (ref3<horas<=ref4):
    e=5
   elif (ref4<horas<=ref1):
    e=3
   print(f"Enfermeros disponibles: {e}")

   #funcion que genera de forma aleatoria pacientes, la cantidad es acorde al horario
   listaPacientes=generadorPacientes(e)
   print(f"Pacientes que llegaron: {len(listaPacientes)}")
   contadorP+=len(listaPacientes)

   if(j>e-1):
      j=0 #esto es para que en los casos donde cambia el turno y baja la cantidad de enfermeros disponibles. Evita acceder a enfermeros que no estan disponibles
  
   k=0 #indice asignado a los pacientes

   while(k<len(listaPacientes)):
     
     listaEnfermeros[j].TRIAGE(listaPacientes[k], tiempo, colas, arbol_TRIAGE)

     print("Paciente numero",listaPacientes[k].numero, "color =", colores[listaPacientes[k].color], "clasificado por el enfermero", listaEnfermeros[j].id)
    
     if listaPacientes[k].color == 0:
      atendido=colas[0].get() #si es rojo directamente se atiende 
      contadorP-=1
      print("Paciente numero ", atendido.numero, "atendido")
    
     if(j<e-1):
      j+=1 #paso al siguiente enfermero
     else:
      j=0 #si llego al final de la lista de enfermeros, vuelvo a empezar

     k+=1
  
   listaAtender=SalaEsperaVORAZ(colas,tiempo,e)
   
   cont=0

   if not listaAtender.empty():
    while not listaAtender.empty():
      atendido= listaAtender.get() #simplemente los elimina 
      print("Paciente num", atendido.numero, "atendido")
      cont+=1
      

   contadorP-=cont

   print(f"Pacientes en la sala de espera: {contadorP}")
   #time.sleep(1)
   tiempo+=minutos_intervalo
     


if __name__ == "__main__":
  main()


 