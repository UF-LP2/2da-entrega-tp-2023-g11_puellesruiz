import pytest
from src.clases import Paciente, evaluar_paciente, construir_arbol, mapeo_sintomas

def test_TRIAGE_ROJO():
    nodo_raiz = construir_arbol()
    paciente = Paciente()
    paciente.lista_sintomas[0] = False #no respira
    color = evaluar_paciente(paciente, nodo_raiz, mapeo_sintomas)
    assert color == 0

def test_TRIAGE_NARANJA1():
    nodo_raiz = construir_arbol()
    paciente = Paciente()
    paciente.lista_sintomas = [True, False, False, False, False, False, False]#no esta conciente
    color = evaluar_paciente(paciente, nodo_raiz, mapeo_sintomas)
    assert color == 1

def test_TRIAGE_NARANJA2():
    nodo_raiz = construir_arbol()
    paciente = Paciente()
    paciente.lista_sintomas = [True, True, True, False, False, False, False]#hemorragia
    color = evaluar_paciente(paciente, nodo_raiz, mapeo_sintomas)
    assert color == 1

def test_TRIAGE_AMARILLO1():
    nodo_raiz = construir_arbol()
    paciente = Paciente()
    paciente.lista_sintomas = [True, True, False, True, False, False, False]#hipertension
    color = evaluar_paciente(paciente, nodo_raiz, mapeo_sintomas)
    assert color == 2

def test_TRIAGE_AMARILLO2():
    nodo_raiz = construir_arbol()
    paciente = Paciente()
    paciente.lista_sintomas = [True, True, False, False, True, False, False]#disfuncion motora
    color = evaluar_paciente(paciente, nodo_raiz, mapeo_sintomas)
    assert color == 2

def test_TRIAGE_AMARILLO3():
    nodo_raiz = construir_arbol()
    paciente = Paciente()
    paciente.lista_sintomas = [True, True, False, False, False, True, False]#delirio
    color = evaluar_paciente(paciente, nodo_raiz, mapeo_sintomas)
    assert color == 2

def test_TRIAGE_VERDE():
    nodo_raiz = construir_arbol()
    paciente = Paciente()
    paciente.lista_sintomas = [True, True, False, False, False, False, True]#dolor
    color = evaluar_paciente(paciente, nodo_raiz, mapeo_sintomas)
    assert color == 3

def test_TRIAGE_AZUL():
    nodo_raiz = construir_arbol()
    paciente = Paciente()
    paciente.lista_sintomas = [True, True, False, False, False, False, False]#no dolor
    color = evaluar_paciente(paciente, nodo_raiz, mapeo_sintomas)
    assert color == 4