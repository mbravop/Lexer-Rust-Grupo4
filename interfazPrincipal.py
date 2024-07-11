import tkinter as tk
import time
import lexer as lx
import parser as ps

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x500")
        self.root.title("Proyecto LP - Analizador de Rust")
        self.root.resizable(False, False)

        # Marco principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Cuadro de texto
        self.textbox_label = tk.Label(main_frame, text="Inserte código aquí:", font=("Arial", 12))
        self.textbox_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.textbox = tk.Text(main_frame, height=15, font=("Arial", 14))
        self.textbox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # Consola
        self.console_label = tk.Label(main_frame, text="Consola:", font=("Arial", 12))
        self.console_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.console = tk.Text(main_frame, height=5, font=("Arial", 14))
        self.console.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        self.console.configure(state='disabled')

        # Botones
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=1, column=1, rowspan=3, padx=5, pady=5, sticky="n")

        self.lexical_button = tk.Button(button_frame, text="Analizador léxico", font=("Arial", 12), command=self.run_lexer)
        self.lexical_button.pack(fill=tk.X, padx=5, pady=5)

        self.syntax_button = tk.Button(button_frame, text="Analizador sintáctico", font=("Arial", 12), command=self.run_syntax)
        self.syntax_button.pack(fill=tk.X, padx=5, pady=5)

        self.semantic_button = tk.Button(button_frame, text="Analizador semántico", font=("Arial", 12), command=self.run_semantic)
        self.semantic_button.pack(fill=tk.X, padx=5, pady=5)

        self.clear_button = tk.Button(button_frame, text="Limpiar código", font=("Arial", 12), command=self.clear_code)
        self.clear_button.pack(fill=tk.X, padx=5, pady=125)

        # Configuración del grid
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)

        self.root.mainloop()

    def run_lexer(self):
        lx.errors = []
        input_text = self.textbox.get("1.0", tk.END)
        result = lx.ejecutarLexer(input_text)
        self.console.configure(state='normal')
        self.console.delete("1.0", tk.END)
        self.console.insert(tk.END, result)
        self.console.configure(state='disabled')

    def run_syntax(self):
        ps.salidaSemantico = ""
        ps.salidaSintactico = ""
        input_text = self.textbox.get("1.0", tk.END)
        sintactico = ps.analizadorSintactico(input_text)[0]
        if sintactico == "None":
            sintactico = "No hay errores sintacticos."

        if sintactico.count("None") > 1:
            sintactico.replace("None","")
        self.console.configure(state='normal')
        self.console.delete("1.0", tk.END)
        self.console.insert(tk.END, sintactico)
        self.console.configure(state='disabled')

    def run_semantic(self):
        ps.listaFunciones = set()
        ps.salidaSemantico = ""
        ps.salidaSintactico = ""
        input_text = self.textbox.get("1.0", tk.END)
        sintactico, semantico = ps.analizadorSintactico(input_text)
        if sintactico == "None":
            if len(semantico) == 0:
                semantico = "No hay errores semanticos."
            self.console.configure(state='normal')
            self.console.delete("1.0", tk.END)
            self.console.insert(tk.END, semantico)
            self.console.configure(state='disabled')
        else:
            self.console.configure(state='normal')
            self.console.delete("1.0", tk.END)
            self.console.insert(tk.END, "Corregir sintaxis antes de analizar semantica")
            self.console.configure(state='disabled')



    def clear_code(self):
        self.textbox.delete("1.0", tk.END)
        self.console.configure(state='normal')
        self.console.delete("1.0", tk.END)
        self.console.configure(state='disabled')


MyGUI()
