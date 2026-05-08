from os_utils import check_disk_space, check_ping


def mostrar_menu() -> None:
    """Muestra las opciones disponibles en el toolkit."""
    print("\n--- SYSTEM TOOLKIT CLI ---")
    print("1. Verificar estado del sistema")
    print("2. Listar procesos (Simulado)")
    print("3. Comprobar ping")
    print("4. Comprobar espacio libre en disco")
    print("5. Salir")


def ejecutar_accion(opcion: str) -> bool:
    """
    Procesa la opcion del usuario.
    Retorna False si el usuario decide salir, True de lo contrario.
    """
    if opcion == "1":
        print("[INFO] El sistema esta operativo.")
    elif opcion == "2":
        procesos: list[str] = ["python", "bash", "vscode"]
        print(f"[INFO] Procesos activos: {', '.join(procesos)}")
    elif opcion == "3":
        ip: str = input("Introduce la IP o dominio: ")
        if check_ping(ip):
            print(f"[INFO] {ip} responde al ping.")
        else:
            print(f"[ERROR] {ip} no responde al ping.")
    elif opcion == "4":
        partition: str = input("Introduce la particion o ruta (ej. C:\\): ")
        try:
            check_disk_space(partition)
        except FileNotFoundError:
            print("[ERROR] La particion o ruta indicada no existe.")
    elif opcion == "5":
        print("Saliendo del toolkit...")
        return False
    else:
        print("[ERROR] Opcion no valida.")
    return True


def main() -> None:
    # Bucle principal de la interfaz CLI
    ejecutando: bool = True
    while ejecutando:
        mostrar_menu()
        seleccion: str = input("Selecciona una opcion: ")
        ejecutando = ejecutar_accion(seleccion)


if __name__ == "__main__":
    main()
