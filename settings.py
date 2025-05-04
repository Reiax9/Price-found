import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Ejemplo de Frame")

    # Creamos un Frame dentro de la ventana principal
    frame = tk.Frame(root, bg="lightblue", bd=2, relief=tk.SOLID)
    frame.pack(padx=10, pady=10)

    # Creamos algunos widgets dentro del Frame
    label = tk.Label(frame, text="Esto es un Label dentro del Frame", bg="lightblue")
    label.pack(pady=5)

    button = tk.Button(frame, text="Esto es un Button dentro del Frame", bg="lightblue")
    button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
