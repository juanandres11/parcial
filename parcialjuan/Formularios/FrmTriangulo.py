import tkinter as tk
from tkinter import messagebox

class FrmTriangulo:
    def __init__(self, master, titulo):
        self.master = master
        master.title(titulo)
        master.geometry("300x250")
        master.resizable(False, False)

        self.label_base = tk.Label(master, text="Ingrese la base:", font=("Arial", 12))
        self.label_base.pack(pady=10)

        self.entry_base = tk.Entry(master, width=20, font=("Arial", 12))
        self.entry_base.pack(pady=5)
        self.entry_base.focus_set()

        self.label_altura = tk.Label(master, text="Ingrese la altura:", font=("Arial", 12))
        self.label_altura.pack(pady=10)

        self.entry_altura = tk.Entry(master, width=20, font=("Arial", 12))
        self.entry_altura.pack(pady=5)

        self.btn_calcular = tk.Button(master, text="Calcular Área", command=self.calcular_area, width=15, height=1)
        self.btn_calcular.pack(pady=10)

        self.label_resultado = tk.Label(master, text="Área: ", font=("Arial", 12, "bold"))
        self.label_resultado.pack(pady=5)

    def calcular_area(self):
        try:
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            if base < 0 or altura < 0:
                messagebox.showerror("Error de Entrada", "La base y la altura no pueden ser negativas.")
                return
            area = (base * altura) / 2
            self.label_resultado.config(text=f"Área: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingrese números válidos para la base y la altura.")