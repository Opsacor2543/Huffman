import tkinter as tk
from tkinter import filedialog
import os

class Huffman:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Huffman")

        self.button_buscar = tk.Button(ventana, text="Buscar archivo", command=self.examine_file)
        self.button_buscar.pack()

        self.button_compress = tk.Button(ventana, text="Comprimir", command=self.compress_file)
        self.button_compress.pack()

        self.button_decompress = tk.Button(ventana, text="Descomprimir", command=self.decompress_file)
        self.button_decompress.pack()

        self.textbox = tk.Text(ventana, height=10, width=50)
        self.textbox.pack()

        self.archivo = ""

    def examine_file(self):
        archivo = filedialog.askopenfilename()
        if archivo:
            self.archivo = archivo
            with open(archivo, 'r') as file:
                content = file.read()
                imprimir = self.contenido(content)
                self.textbox.insert(tk.END, f"Frecuencia de caracteres:\n{imprimir}\n")

    def contenido(self, content):
        imprimir = {}
        for char in content:
            if char in imprimir:
                imprimir[char] += 1
            else:
                imprimir[char] = 1
        return imprimir

    def compress_file(self):
        if self.archivo:
            # Construir el árbol de Huffman, asignar códigos y comprimir el archivo
            pass

    def decompress_file(self):
        archivo = filedialog.askopenfilename()
        if archivo:
            # Descomprimir el archivo
            pass

root = tk.Tk()
huffman = Huffman(root)
root.mainloop()
