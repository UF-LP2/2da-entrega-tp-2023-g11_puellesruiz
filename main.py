import queue
from src.clases import generadorEnfermeros, generadorPacientes, SalaEsperaVORAZ

tiempoMAX=24 ##
ref1=7
ref2=11
ref3=17
ref4=24
##temporales, revisar las condiciones del switch si coinciden
def main() -> None:

##definir si son 5 o 4
  colores=["ROJO","NARANJA","AMARILLO","VERDE","AZUL"]
  colas = [queue.Queue() for _ in range(5)]  # declaro una lista de 5 colas vacias
  listaAtender=[]
  listaEnfermeros=generadorEnfermeros(5)
  j=0 #indice  asignado a los enfermeros atendiendo, si el dia recien empieza, se incializa en 0
  tiempo=0# TEMPORAL!!!!
  e=0
  contadorP=0
  while tiempo<tiempoMAX:

   print(f"Tiempo = {tiempo}")
   #segun la franja horaria se definen los enfermeros 
 
   if (tiempo<=ref1):
    e=1
   elif (ref1<tiempo<=ref2):
    e=2
   elif (ref2<tiempo<=ref3):
    e=5
   elif (ref3<tiempo<=ref4):
    e=3
   print(f"Enfermeros disponibles: {e}")
   listaPacientes=generadorPacientes(e)# funcion que genera de forma aleatoria pacientes, la cantidad es acorde al horaria 
   print(f"Pacientes que llegaron: {len(listaPacientes)}")
   contadorP+=len(listaPacientes)
   if(j>e-1):
      j=0 #esto es para que en los casos donde cambia el turno y baja la cantidad de enfermeros disponibles. Evita acceder a enfermeros que no estan disponibles
   k=0 #indice asignado a los pacientes
   while(k<len(listaPacientes)):
     listaEnfermeros[j].TRIAGE(listaPacientes[k], tiempo, colas)
     print("Paciente numero",listaPacientes[k].numero, "color =", colores[listaPacientes[k].color], "clasificado por el enfermero", listaEnfermeros[j].id)
     if listaPacientes[k].color == 0:
      atendido=colas[0].get() #si es rojo directamente se atiende 
      print("Paciente numero ", atendido.numero, "atendido")
     if(j<e-1):
      j+=1
     else:
      j=0
     k+=1
   listaAtender=SalaEsperaVORAZ(colas,tiempo,e)
   cont=0
   if not listaAtender.empty():
    while not listaAtender.empty():
      atendido= listaAtender.get() #simplemente los elimina 
      print("Paciente num", atendido.numero, "atendido")
      cont+=1

   contadorP=contadorP-cont
   print(f"Pacientes en la sala de espera: {contadorP}")
   tiempo+=1
     


if __name__ == "__main__":
  main()