from tkinter import *

def main():
    # Crear la ventana principal
    root_window = Tk()

    root_window.geometry("480x240")

    frame = Frame(root_window, bg="#2E2E2E")

    # Crear una etiqueta
    label = Label(
        frame,
        text="Hello world!!",
        fg="#FF493B",
        bg="#2E2E2E",
        width=20,
        height=10
        )

    button = Button(
        frame,
        text="Click me!",
        width=20,
        height=5,
        bg="blue",
        fg="yellow",
        command='' # Aquí se puede poner una funcion
    )

    # Colocar la etiqueta en la ventana
    frame.pack(fill=BOTH, expand=True)
    label.pack(padx=20, pady=10)
    button.pack()

    # Ejecutar el bucle principal de la aplicación
    root_window.mainloop()

if __name__ == "__main__":
    main()