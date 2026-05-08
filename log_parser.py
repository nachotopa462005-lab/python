from pathlib import Path


def parse_failed_ssh_ips(log_path: str) -> tuple[set[str], dict[str, int]]:
    """
    Lee un auth.log linea a linea y extrae las IPs con intentos SSH fallidos.
    Devuelve un set con IPs unicas y un diccionario con el conteo por IP.
    """
    failed_ips: set[str] = set()
    failed_counts: dict[str, int] = {}

    with open(log_path, "r", encoding="utf-8") as log_file:
        for line in log_file:
            clean_line: str = line.strip()

            if "Failed password" not in clean_line:
                continue

            parts: list[str] = clean_line.split()
            if "from" not in parts:
                continue

            ip_index: int = parts.index("from") + 1
            if ip_index >= len(parts):
                continue

            ip: str = parts[ip_index]
            failed_ips.add(ip)
            failed_counts[ip] = failed_counts.get(ip, 0) + 1

    return failed_ips, failed_counts


def show_failed_ssh_report(log_path: str) -> None:
    failed_ips, failed_counts = parse_failed_ssh_ips(log_path)

    print("[INFO] IPs con fallos de login SSH:")
    for ip in sorted(failed_ips):
        print(f"- {ip}")

    print("\n[INFO] Conteo de fallos por IP:")
    for ip, count in sorted(failed_counts.items()):
        print(f"- {ip}: {count}")


if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent
    show_failed_ssh_report(str(current_dir / "auth.log"))
