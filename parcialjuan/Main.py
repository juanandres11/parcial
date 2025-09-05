import tkinter as tk
from tkinter import messagebox
from Formularios.FrmCirculo import FrmCirculo
from Formularios.FrmCuadrado import FrmCuadrado
from Formularios.FrmRectangulo import FrmRectangulo
from Formularios.FrmTriangulo import FrmTriangulo

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Áreas")
        master.geometry("400x300")
        master.resizable(False, False)

        self.label = tk.Label(master, text="Seleccione el cálculo a realizar:", font=("Arial", 14))
        self.label.pack(pady=20)

        self.btn_circulo = tk.Button(master, text="Área de un Círculo", command=self.abrir_circulo, width=30, height=2)
        self.btn_circulo.pack(pady=5)

        self.btn_cuadrado = tk.Button(master, text="Área de un Cuadrado", command=self.abrir_cuadrado, width=30, height=2)
        self.btn_cuadrado.pack(pady=5)

        self.btn_rectangulo = tk.Button(master, text="Área de un Rectángulo", command=self.abrir_rectangulo, width=30, height=2)
        self.btn_rectangulo.pack(pady=5)

        self.btn_triangulo = tk.Button(master, text="Área de un Triángulo", command=self.abrir_triangulo, width=30, height=2)
        self.btn_triangulo.pack(pady=5)

    def abrir_circulo(self):
        self.abrir_formulario(FrmCirculo, "Área del Círculo")

    def abrir_cuadrado(self):
        self.abrir_formulario(FrmCuadrado, "Área del Cuadrado")

    def abrir_rectangulo(self):
        self.abrir_formulario(FrmRectangulo, "Área del Rectángulo")

    def abrir_triangulo(self):
        self.abrir_formulario(FrmTriangulo, "Área del Triángulo")

    def abrir_formulario(self, FormularioClase, titulo):
        new_window = tk.Toplevel(self.master)
        FormularioClase(new_window, titulo)
        new_window.grab_set()  # Bloquea la ventana principal hasta cerrar la nueva
        self.master.wait_window(new_window) # Espera a que la ventana secundaria se cierre

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()