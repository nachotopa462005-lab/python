import os
import shutil
import subprocess


def check_ping(ip: str) -> bool:
    """Devuelve True si la IP responde a un ping, False si falla."""
    count_flag: str = "-n" if os.name == "nt" else "-c"
    command: list[str] = ["ping", count_flag, "1", ip]

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except OSError:
        return False

    return result.returncode == 0


def check_disk_space(partition: str, min_free_percent: float = 20.0) -> bool:
    """
    Comprueba el espacio libre de una particion.
    Devuelve True si hay suficiente espacio y False si esta por debajo del umbral.
    """
    partition_path: str = os.path.abspath(partition)
    total, used, free = shutil.disk_usage(partition_path)
    free_percent: float = (free / total) * 100

    print(f"[INFO] Particion: {partition_path}")
    print(f"[INFO] Espacio total: {_bytes_to_gb(total):.2f} GB")
    print(f"[INFO] Espacio usado: {_bytes_to_gb(used):.2f} GB")
    print(f"[INFO] Espacio libre: {_bytes_to_gb(free):.2f} GB ({free_percent:.2f}%)")

    if free_percent < min_free_percent:
        print(f"[ALERTA] El espacio libre es menor al {min_free_percent:.0f}%.")
        return False

    print("[INFO] Espacio libre suficiente.")
    return True


def _bytes_to_gb(value: int) -> float:
    return value / (1024**3)
