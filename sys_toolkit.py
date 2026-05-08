import sys

def mostrar_menu() -> None:
    """Muestra las opciones disponibles en el toolkit."""
    print("\n--- SYSTEM TOOLKIT CLI ---")
    print("1. Verificar estado del sistema")
    print("2. Listar procesos (Simulado)")
    print("3. Salir")

def ejecutar_accion(opcion: str) -> bool:
    """
    Procesa la opción del usuario.
    Retorna False si el usuario decide salir, True de lo contrario.
    """
    if opcion == "1":
        print("[INFO] El sistema está operativo.")
    elif opcion == "2":
        procesos: list[str] = ["python", "bash", "vscode"]
        print(f"[INFO] Procesos activos: {', '.join(procesos)}")
    elif opcion == "3":
        print("Saliendo del toolkit...")
        return False
    else:
        print("[ERROR] Opción no válida.")
    return True

def main() -> None:
    # Bucle principal de la interfaz CLI
    ejecutando: bool = True
    while ejecutando:
        mostrar_menu()
        seleccion: str = input("Selecciona una opción: ")
        ejecutando = ejecutar_accion(seleccion)

if __name__ == "__main__":
    main()