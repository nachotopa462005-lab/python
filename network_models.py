class NetworkDevice:
    """
    Modelo base para representar un dispositivo de red.

    La programacion orientada a objetos ayuda a mantener un inventario de red
    estructurado porque permite describir los datos comunes una sola vez
    (hostname, IP y MAC) y especializar cada tipo de equipo en clases hijas.
    Asi, un router y un servidor comparten una forma comun de identificarse,
    pero cada uno puede tener atributos y auditorias de seguridad propias.
    """

    def __init__(self, hostname: str, ip: str, mac: str) -> None:
        self.hostname = hostname
        self.ip = ip
        self.mac = mac

    def show_info(self) -> None:
        print(f"Hostname: {self.hostname}")
        print(f"IP: {self.ip}")
        print(f"MAC: {self.mac}")

    def audit_device(self) -> None:
        print("[AUDIT] Revisa configuracion general, actualizaciones y accesos.")


class Router(NetworkDevice):
    """Dispositivo encargado de enrutar trafico entre redes."""

    def __init__(
        self,
        hostname: str,
        ip: str,
        mac: str,
        routing_protocol: str,
        wan_interface: str,
    ) -> None:
        super().__init__(hostname, ip, mac)
        self.routing_protocol = routing_protocol
        self.wan_interface = wan_interface

    def audit_device(self) -> None:
        print(f"[AUDIT][Router] {self.hostname}")
        print("- Deshabilitar administracion remota insegura como Telnet.")
        print("- Revisar ACLs y reglas de firewall.")
        print("- Validar protocolos de routing y vecinos autorizados.")
        print("- Cambiar credenciales por defecto y usar SSH.")


class Server(NetworkDevice):
    """Equipo que ofrece servicios dentro de la red."""

    def __init__(
        self,
        hostname: str,
        ip: str,
        mac: str,
        operating_system: str,
        exposed_services: list[str],
    ) -> None:
        super().__init__(hostname, ip, mac)
        self.operating_system = operating_system
        self.exposed_services = exposed_services

    def audit_device(self) -> None:
        print(f"[AUDIT][Server] {self.hostname}")
        print("- Aplicar parches del sistema operativo.")
        print("- Revisar permisos de usuarios y claves SSH.")
        print("- Cerrar servicios innecesarios.")
        print("- Comprobar copias de seguridad y logs de acceso.")


if __name__ == "__main__":
    devices: list[NetworkDevice] = [
        Router(
            hostname="router-core",
            ip="192.168.1.1",
            mac="00:11:22:33:44:55",
            routing_protocol="OSPF",
            wan_interface="GigabitEthernet0/0",
        ),
        Server(
            hostname="srv-web-01",
            ip="192.168.1.20",
            mac="AA:BB:CC:DD:EE:FF",
            operating_system="Ubuntu Server",
            exposed_services=["ssh", "https"],
        ),
    ]

    for device in devices:
        device.show_info()
        device.audit_device()
        print()
