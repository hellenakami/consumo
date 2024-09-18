import tkinter as tk
from tkinter import messagebox

def calcular_conta():
    try:
        kwh = float(entry_kwh.get())
        tipo_instalacao = var_tipo.get()

        if tipo_instalacao == 'R':
            if kwh <= 500:
                valor = kwh * 0.40
            else:
                valor = kwh * 0.65
        elif tipo_instalacao == 'C':
            if kwh <= 1000:
                valor = kwh * 0.55
            else:
                valor = kwh * 0.60
        elif tipo_instalacao == 'I':
            if kwh <= 5000:
                valor = kwh * 0.55
            else:
                valor = kwh * 0.60
        else:
            raise ValueError("Tipo de instalação inválido")

        messagebox.showinfo("Resultado", f"Valor da conta: R$ {valor:.2f}")
    except ValueError as e:
        messagebox.showerror("Erro", "Verifique se os valores estão corretos")

# Configurações da interface gráfica
root = tk.Tk()
root.title("Calculadora de Conta de Luz")

# Label e campo de entrada para KWh
label_kwh = tk.Label(root, text="Consumo em KWh:")
label_kwh.pack()

entry_kwh = tk.Entry(root)
entry_kwh.pack()

# Opções de tipo de instalação
var_tipo = tk.StringVar(value='R')

label_tipo = tk.Label(root, text="Tipo de instalação:")
label_tipo.pack()

radio_residencial = tk.Radiobutton(root, text="Residencial", variable=var_tipo, value='R')
radio_comercial = tk.Radiobutton(root, text="Comercial", variable=var_tipo, value='C')
radio_industrial = tk.Radiobutton(root, text="Industrial", variable=var_tipo, value='I')

radio_residencial.pack()
radio_comercial.pack()
radio_industrial.pack()

# Botão para calcular
button_calcular = tk.Button(root, text="Calcular", command=calcular_conta)
button_calcular.pack()

# Iniciar o loop da interface gráfica
root.mainloop()