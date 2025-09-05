import tkinter as tk
from tkinter import messagebox
import math

class FrmCirculo:
    def __init__(self, master, titulo):
        self.master = master
        master.title(titulo)
        master.geometry("300x200")
        master.resizable(False, False)

        self.label_radio = tk.Label(master, text="Ingrese el radio:", font=("Arial", 12))
        self.label_radio.pack(pady=10)

        self.entry_radio = tk.Entry(master, width=20, font=("Arial", 12))
        self.entry_radio.pack(pady=5)
        self.entry_radio.focus_set()

        self.btn_calcular = tk.Button(master, text="Calcular Área", command=self.calcular_area, width=15, height=1)
        self.btn_calcular.pack(pady=10)

        self.label_resultado = tk.Label(master, text="Área: ", font=("Arial", 12, "bold"))
        self.label_resultado.pack(pady=5)

    def calcular_area(self):
        try:
            radio = float(self.entry_radio.get())
            if radio < 0:
                messagebox.showerror("Error de Entrada", "El radio no puede ser negativo.")
                return
            area = math.pi * (radio ** 2)
            self.label_resultado.config(text=f"Área: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingrese un número válido para el radio.")