import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from log_parser import parse_failed_ssh_ips


def get_ip_intel(ip: str) -> dict[str, str]:
    """Consulta ipinfo.io y devuelve pais y organizacion de una IP."""
    url = f"https://ipinfo.io/{ip}/json"

    try:
        with urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError, OSError, json.JSONDecodeError):
        return {"country": "N/A", "org": "N/A"}

    return {
        "country": data.get("country", "N/A"),
        "org": data.get("org", "N/A"),
    }


def show_threat_intel_table(log_path: str) -> None:
    """Muestra una tabla con IP atacante, intentos, pais y organizacion."""
    _, failed_counts = parse_failed_ssh_ips(log_path)
    rows: list[tuple[str, int, str, str]] = []

    for ip, attempts in sorted(failed_counts.items()):
        intel = get_ip_intel(ip)
        rows.append((ip, attempts, intel["country"], intel["org"]))

    _print_table(rows)


def _print_table(rows: list[tuple[str, int, str, str]]) -> None:
    headers = ("IP atacante", "Intentos", "Pais", "Organizacion")
    table_rows = [
        (ip, str(attempts), country, org)
        for ip, attempts, country, org in rows
    ]

    widths = [
        max(len(headers[index]), *(len(row[index]) for row in table_rows))
        if table_rows
        else len(headers[index])
        for index in range(len(headers))
    ]

    header_line = " | ".join(
        headers[index].ljust(widths[index]) for index in range(len(headers))
    )
    separator = "-+-".join("-" * width for width in widths)

    print(header_line)
    print(separator)

    for row in table_rows:
        print(" | ".join(row[index].ljust(widths[index]) for index in range(len(row))))


if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent
    show_threat_intel_table(str(current_dir / "auth.log"))
