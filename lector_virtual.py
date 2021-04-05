# librería de voz
import pyttsx3

# libreria grafica
import tkinter as tk

# creamos una ventana grafica
root = tk.Tk()
root.geometry('400x700')
root.resizable(0,0)

# inicializamos la libreríra
engine = pyttsx3.init()

# obetenemos las voces de pyttsx
voices = engine.getProperty('voices')
# obtenemos uns voz en específico de las lista que esta en voices
engine.setProperty('voice', voices[0].id)



saludo = 'Buenos dias, '
instruccion = 'Escriba el texto para reproducirlo'
engine.say(saludo + instruccion)
engine.runAndWait()

# ---------------------------------------------------------------------------------------------------------------
def talktext():
    text = writeText.get(1.0,tk.END)
    engine.say(text)
    engine.runAndWait()

# creamos la ventana grafica

# titulo
title = tk.Label(root)
title["text"] = "Lector virtual"
title.pack()

# espacio para escribir
writeText = tk.Text(root)
writeText.pack()
writeText.config(width=30, height=30, font=("Consolas",12), padx=15, pady=15, selectbackground="red")

playStop = tk.Button(root, command=talktext)
playStop["text"] = "Reproducir"
playStop.pack()

root.mainloop()

