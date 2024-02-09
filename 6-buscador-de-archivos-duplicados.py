import os
import tkinter as tk 
from tkinter import ttk

class BuscadorDuplicadosApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Buscador de Archivos Duplicados")

        self.label_directorio = ttk.Label(self.master, text="Directorio:")
        self.label_directorio.grid(row=0, column=0, padx=5, pady=5)

        self.directorio_entry = ttk.Entry(self.master, width=50)
        self.directorio_entry.grid(row=0, column=1, padx=5, pady=5)

        self.buscar_button = ttk.Button(self.master, text="Buscar", command=self.buscar_duplicados)
        self.buscar_button.grid(row=0, column=2, padx=5, pady=5)

        self.resultado_text = tk.Text(self.master, height=20, width=70, )
        self.resultado_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    def buscar_duplicados(self):
        directorio = self.directorio_entry.get()
        print("directorio a buscar:", directorio)
        if not os.path.isdir(directorio):
            self.resultado_text.delete("1.0", tk.END)
            self.resultado_text.insert(tk.END, "Error: El directorio específico no existe. ") 
            return
        
        archivos_por_tamano = []
        archivos_duplicados = []

        for directorio_raiz, _, archivos in os.walk(directorio):
            for archivo in archivos:
                ruta_completa = os.path.join(directorio_raiz, archivo)
                tamano = os.path.getsize(ruta_completa)

                if tamano in archivos_por_tamano:
                    archivos_por_tamano[tamano].append(ruta_completa)
                else:
                    archivos_por_tamano[tamano] = [ruta_completa]

        for tamano, archivos in archivos_por_tamano.items():
            if len(archivos) > 1:
                archivos_duplicados.append(archivos)

        if archivos_duplicados:
            self.resultado_text.delete("1.0", tk.END)
            self.resultado_text.insert(tk.END, "Archivos duplicados encontrados:\n")
            for grupo in archivos_duplicados:
                self.resultado_text.insert(tk.END, "Grupo de archivos duplicados:\n")
                for archivo in grupo:
                    self.resultado_text.insert(tk.END, f"- {archivo}\n")
        else:
            self.resultado_text.delete("1.0", tk.END)
            self.resultado_text.insert(tk.END, "No se encontraron archivos duplicados en el directorio.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BuscadorDuplicadosApp(root)
    root.mainloop()


                                
