import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox

def ventanaPrincipal():
    global ventana
    ventana = tk.Tk()
    frm = ttk.Frame(ventana, padding=10)
    frm.grid()
    ventana.title("Actividad 07 ")
    ventana.geometry("600x600")

    boton_examinar = ttk.Button(ventana, text="Examinar", command=examinar)
    boton_examinar.grid(column=1, row=0)
    boton_comprimir = ttk.Button(ventana, text="Comprimir", command=comprimir).grid(column=1, row=1)
    boton_descomprimir = ttk.Button(ventana, text="Descomprimir", command=descomprimir).grid(column=1, row=2)
    
    ventana.mainloop()

archivo = open("Gullivers_Travels.txt", mode="r", encoding="UTF-8")
archivoComprimido = open("archivoComprimido.bin", mode="wb") 

def examinar():
    global archivob
    archivob = filedialog.askopenfilename()
    with open(archivo, 'r') as f:
        text = f.read()
    
def calcularFrecuencia():
    frecuenciaLetras = {}
    for palabras in archivo:
        for letras in palabras:
            letras = letras.lower()
            if letras in frecuenciaLetras:
                frecuenciaLetras[letras] = frecuenciaLetras[letras] + 1  
            else:
                frecuenciaLetras[letras] = 1
    return frecuenciaLetras

class Node:
    def __init__(self, letra=None, freq=0, left=None, right=None):
        self.letra = letra
        self.freq = freq
        self.left = left
        self.right = right

def creacionArbol():
    ListaNodos = []
    valorTotal = 0
    class vertice:
        def __init__(self, letra, frecuencia):
            self.letra = letra
            self.frecuencia = frecuencia
            self.left = None
            self.right = None
    for letra, valor in calcularFrecuencia().items():
        valorTotal = valorTotal + valor
        vertices = vertice(letra, valor)
        ListaNodos.append(vertices)

    while len (ListaNodos) > 1:
        ListaNodos = sorted(ListaNodos, key=lambda x: x.frecuencia)
        nodoUnion = vertice(None,ListaNodos[0].frecuencia + ListaNodos[1].frecuencia)
        nodoUnion.left = ListaNodos[0]
        nodoUnion.right = ListaNodos[1]
        ListaNodos.append(nodoUnion)
        ListaNodos.pop(0)
        ListaNodos.pop(0)
    
    return ListaNodos


tabla = {}

def tablaValores(arbol,codigo,tablaA):
    global archivo
    if arbol.letra is not None:
        tablaA[arbol.letra] = codigo
    if arbol.left is not None:
        arbol2 = arbol.left
        tablaValores(arbol2,codigo + "0",tablaA)
    if arbol.right is not None:
        arbol2 = arbol.right
        tablaValores(arbol2,codigo + "1",tablaA)
        
arbolH = creacionArbol()[0]
tablaValores(arbolH,"",tabla)
print(tabla)


def imprimirTablaValores(tabla, archivo):
    with open(archivo, 'w') as f:
        for letra, codigo in tabla.items():
            f.write(f"{letra}: {codigo}\n")

imprimirTablaValores(tabla, "tabla_huffman.txt")
archivo.close()
def comprimir():
    archivo = open("Gullivers_Travels.txt", mode="r", encoding="UTF-8")
    valor1 = 0
    listValores = []
    for claves, valores in tabla.items():
        tabla[claves] = valor1
        valor1 = valor1 + 1
    for palabras in archivo:
        for letras in palabras:
            letras = letras.lower()
            listValores.append(tabla[letras])
    archivoComprimido.write(bytearray(listValores))
    archivo.close()
    archivoComprimido.close()

#comprimir()



def descomprimir():
    archivoComprimido = open("archivoComprimido.bin", mode="rb") 
    archivoDescomprimido = open("archivoDescomprimido.txt", mode="w", encoding="UTF-8") 
    lista = list(archivoComprimido.read())
    print(lista)
    for valor in lista:
        for claves, valores in tabla.items():
            if valor == valores:
                archivoDescomprimido.write(claves)
    archivoComprimido.close()
    archivoDescomprimido.close()

    


#descomprimir()
ventanaPrincipal()
