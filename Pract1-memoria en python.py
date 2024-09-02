import ctypes
import gc

# Variable estática simulada: una variable global
static_var = 23  # Esto representa una variable estática que vive durante todo el programa

class DynamicObject:
    def __init__(self, value):
        # Simulando la memoria dinámica: objetos en el heap
        self.value = value

def display_memory(address, label):
    # Mostrar la dirección de memoria usando ctypes
    print(f"{label} está en la dirección de memoria: {ctypes.addressof(address)}")

def main():
    # Mostrando la memoria estática
    print(f"Valor de la variable estática: {static_var}")
    display_memory(ctypes.c_int(static_var), "Variable estática")

    # Creación de un objeto dinámico
    dynamic_var = DynamicObject(5)
    print(f"Valor de la variable dinámica: {dynamic_var.value}")
    display_memory(ctypes.c_int(dynamic_var.value), "Variable dinámica")

    # Creación de otro objeto dinámico
    dynamic_var2 = DynamicObject(15)
    print(f"Valor de la segunda variable dinámica: {dynamic_var2.value}")
    display_memory(ctypes.c_int(dynamic_var2.value), "Segunda variable dinámica")

    # Simular la liberación de memoria
    print("\nLiberando la memoria dinámica...")
    del dynamic_var
    del dynamic_var2
    gc.collect()  # Forzamos el recolector de basura para liberar la memoria

if __name__ == "__main__":
    main()
