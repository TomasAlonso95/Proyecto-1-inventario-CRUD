
class Inventario:
    def __init__(self):
        self.productos = {}
    def agregar_productos(self, id, nombre, stock):
        if id in self.productos:
            print(f"❌Error: Ya existe un producto con ese ID.")
        else:
            self.productos[id] = {"nombre": nombre, "stock": stock}
            print(f"✅Producto agregado exitosamente al inventario.")
    def mostrar_productos(self):
        if len(self.productos) == 0:
            print("El inventario se encuentra vacio❗")
        else:
            print("---INVENTARIO ACTUAL❕---")
            for id, info in self.productos.items():
                print(f"ID {id} | Nombre: {info['nombre']} | Stock: {info['stock']}")
    def actualizar_productos(self, id, cantidad):
        if id in self.productos:
            self.productos[id]["stock"] = cantidad
            print(f"PERFECTO✔: Actualizaste la cantidad de stock a {cantidad}")
        else:
            print(f"ERROR❌: ID no encontrado.")
    def renombrar_productos(self, id, nuevo_nombre):
        if id in self.productos:
            self.productos[id]["nombre"] = nuevo_nombre
            print(f"PERFECTO✔: Actualizaste el nombre del producto, nombre cambiado a {nuevo_nombre}")
        else:
            print(f"ERROR❌: ID no encontrado.")

if __name__ == "__main__":
    bodega_norte = Inventario()

    while True:
        print("\n--- 📦 GESTIÓN DE INVENTARIO 📦 ---")
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Actualizar Stock")
        print("4. Renombrar Producto") # ¡Tu nueva habilidad!
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            stock = int(input("Stock inicial: "))
            bodega_norte.agregar_productos(id, nombre, stock)

        elif opcion == "2":
            bodega_norte.mostrar_productos()

        elif opcion == "3":
            id = input("ID del producto: ")
            cant = int(input("Nuevo stock total: "))
            bodega_norte.actualizar_productos(id, cant)

        elif opcion == "4":
            id = input("ID del producto: ")
            nuevo_nom = input("Nuevo nombre: ")
            bodega_norte.renombrar_productos(id, nuevo_nom)

        elif opcion == "5":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida.")
