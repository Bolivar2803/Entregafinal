import tkinter as tk
from tkinter import messagebox



class RobotGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Robot Story")
        self.geometry("400x300")
   

        self.state_label = tk.Label(self, text="Estado: Inicio")
        self.state_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack()

        self.stop_button = tk.Button(self.buttons_frame, text="Parada de Emergencia", command=self.stop)
        self.stop_button.grid(row=0, column=0, padx=5)

        self.continue_button = tk.Button(self.buttons_frame, text="Continuar", command=self.continue_execution)
        self.continue_button.grid(row=0, column=1, padx=5)

        self.start_button = tk.Button(self.buttons_frame, text="Inicio", command=self.start)
        self.start_button.grid(row=0, column=2, padx=5)

        self.grab_object_button = tk.Button(self, text="Agarrar objeto", command=self.grab_object)
        self.grab_object_button.pack(pady=10)

        self.release_object_button = tk.Button(self, text="Soltar objeto", command=self.release_object, state=tk.DISABLED)
        self.release_object_button.pack(pady=10)

        self.change_category_button = tk.Button(self, text="Cambiar categoría", command=self.change_category, state=tk.DISABLED)
        self.change_category_button.pack(pady=10)

        self.container_button = tk.Button(self, text="Objeto en contenedor", command=self.object_in_container)
        self.container_button.pack(pady=10)

        self.camera_disconnect_button = tk.Button(self, text="Cámara desconectada", command=self.camera_disconnect)
        self.camera_disconnect_button.pack(pady=10)


        # Estado inicial del robot
        self.robot_state = "Inicio"

        # Lista de categorías de objetos a recoger
        self.object_categories = ["botellas plásticas", "latas", "recipientes plásticos", "recipiente de comida de papeles/cartón"]

        # Categoría actual de objetos que se están recogiendo
        self.current_category = None

        # Variable para controlar si hay más objetos reciclables disponibles
        self.more_objects_available = True

    def stop(self):
        messagebox.showinfo("Evento", "Se oprimió el botón de parada de emergencia.")
        self.update_state("Parada de emergencia")

    def continue_execution(self):
        messagebox.showinfo("Evento", "Se oprimió el botón de continuar.")
        self.update_state("Continuar")

    def start(self):
        messagebox.showinfo("Evento", "Se oprimió el botón de inicio.")
        self.update_state("Inicio")

        # Comienza la exploración del robot
        self.explore()

    def grab_object(self):
        if self.robot_state == "Alcanzando objeto":
            messagebox.showinfo("Evento", "El robot intenta agarrar el objeto.")
            self.update_state("Agarrando objeto")

            # Verificar si quedan más objetos de la misma categoría
            self.check_objects_available()

            # Si no quedan más objetos, cambiar a la siguiente categoría
            if not self.more_objects_available:
                self.change_category_button.config(state=tk.NORMAL)
        
        self.release_object_button.config(state=tk.NORMAL)
        self.grab_object_button.config(state=tk.DISABLED)

    def release_object(self):
        messagebox.showinfo("Evento", "Se soltó el objeto de la garra del robot.")
        self.update_state("Objeto soltado")

        self.release_object_button.config(state=tk.DISABLED)
        self.change_category_button.config(state=tk.NORMAL)
        self.grab_object_button.config(state=tk.NORMAL)

    def change_category(self):
        if self.robot_state == "Objeto en contenedor":
            messagebox.showinfo("Evento", "Se cambió la categoría de los objetos que se quieren recoger.")

            # Cambiar a la siguiente categoría de objetos
            if self.current_category is None:
                self.current_category = self.object_categories[0]
            else:
                current_index = self.object_categories.index(self.current_category)
                if current_index + 1 < len(self.object_categories):
                    self.current_category = self.object_categories[current_index + 1]
                else:
                    self.current_category = None

            self.update_state("Categoría cambiada")

            # Recolectar automáticamente todos los objetos de la categoría actual
            self.collect_objects()

            self.change_category_button.config(state=tk.DISABLED)
            self.grab_object_button.config(state=tk.NORMAL)

    def object_in_container(self):
        messagebox.showinfo("Evento", "El robot llegó a la posición del contenedor.")
        self.update_state("Objeto en contenedor")

        # Verificar si quedan más objetos de la misma categoría
        self.check_objects_available()

        # Si no quedan más objetos, cambiar a la siguiente categoría
        if not self.more_objects_available:
            self.change_category_button.config(state=tk.NORMAL)

    def camera_disconnect(self):
        messagebox.showinfo("Evento", "La cámara se desconectó y no hay imágenes.")
        self.update_state("Cámara desconectada")

    def update_state(self, state):
        self.robot_state = state
        self.state_label.config(text=f"Estado: {state}")

    def explore(self):
        if self.robot_state == "Inicio":
            messagebox.showinfo("Exploración", "El robot está explorando en busca de objetos.")

            # Lógica de exploración del robot
            # ...

            # Simulación de encontrar un objeto
            self.update_state("Objeto encontrado")
            self.move_to_object()

    def move_to_object(self):
        if self.robot_state == "Objeto encontrado":
            messagebox.showinfo("Movimiento", "El robot se mueve hacia el objeto.")

            # Lógica de movimiento del robot
            # ...

            # Simulación de alcanzar el objeto
            self.update_state("Alcanzando objeto")

    def check_objects_available(self):
        # Verificar si quedan más objetos de la misma categoría
        if self.current_category is not None:
            # Lógica para verificar si hay más objetos disponibles
            # ...

            self.more_objects_available = False  # Simulación de no encontrar más objetos

    def collect_objects(self):
        if self.robot_state == "Categoría cambiada":
            messagebox.showinfo("Recolección", f"El robot está recolectando objetos de la categoría: {self.current_category}")

            # Lógica de recolección del robot
            # ...

            # Simulación de recolectar todos los objetos
            self.more_objects_available = False

            # Si no hay más objetos disponibles, cambiar a la siguiente categoría
            if not self.more_objects_available:
                self.change_category_button.config(state=tk.NORMAL)
            

if __name__ == "__main__":
    app = RobotGUI()
    app.mainloop()

