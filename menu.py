from config import MENU_OPTIONS

class Menu:
    def __init__(self):
        self.current_menu = "main"  # Menú actual
        self.menu_stack = []  # Pila de menús visitados

    def start_menu(self):
        while True:
            if self.current_menu == "main":
                self.display_main_menu()
            elif self.current_menu in MENU_OPTIONS:
                self.display_menu(self.current_menu)
            elif self.current_menu == "exit":
                print("¡Gracias por usar nuestro servicio!")
                break
            else:
                print("Menú no válido. Volviendo al menú principal.")
                self.current_menu = "main"

    def display_menu(self, menu_name):
        menu = MENU_OPTIONS.get(menu_name)
        if menu:
            print(f"=== {menu_name.capitalize()} ===")
            for option in menu:
                print(f"{option}. {menu[option]}")
            print("0. Regresar al menú principal")
            selected_option = self.get_input()
            if selected_option == "0":
                self.current_menu = "main"
            elif selected_option in menu:
                self.current_menu = menu[selected_option]
            else:
                print("Opción inválida.")
        else:
            print("Menú no válido. Volviendo al menú principal.")
            self.current_menu = "main"

    def display_main_menu(self):
        self.display_menu("main")

    def get_input(self):
        # Lógica para obtener la entrada del usuario desde el teclado o la entrada USSD
        # En este ejemplo, simplemente se solicita al usuario que ingrese la opción deseada.
        return input("Ingrese la opción deseada: ")
