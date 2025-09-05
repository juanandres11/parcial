import tkinter as tk
from tkinter import messagebox

class FrmCuadrado:
    def __init__(self, master, titulo):
        self.master = master
        master.title(titulo)
        master.geometry("300x200")
        master.resizable(False, False)

        self.label_lado = tk.Label(master, text="Ingrese la longitud del lado:", font=("Arial", 12))
        self.label_lado.pack(pady=10)

        self.entry_lado = tk.Entry(master, width=20, font=("Arial", 12))
        self.entry_lado.pack(pady=5)
        self.entry_lado.focus_set()

        self.btn_calcular = tk.Button(master, text="Calcular Área", command=self.calcular_area, width=15, height=1)
        self.btn_calcular.pack(pady=10)

        self.label_resultado = tk.Label(master, text="Área: ", font=("Arial", 12, "bold"))
        self.label_resultado.pack(pady=5)

    def calcular_area(self):
        try:
            lado = float(self.entry_lado.get())
            if lado < 0:
                messagebox.showerror("Error de Entrada", "El lado no puede ser negativo.")
                return
            area = lado ** 2
            self.label_resultado.config(text=f"Área: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingrese un número válido para el lado.")