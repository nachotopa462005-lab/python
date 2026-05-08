import csv
import random
from pathlib import Path

from faker import Faker


HEADERS = [
    "server_id",
    "hostname",
    "ip",
    "mac",
    "operating_system",
    "ram_gb",
    "cpu_cores",
    "storage_gb",
    "department",
    "owner",
    "environment",
]

OPERATING_SYSTEMS = [
    "Windows Server 2019",
    "Windows Server 2022",
    "Ubuntu Server 24.04",
    "Debian 12",
    "Red Hat Enterprise Linux 9",
    "Rocky Linux 9",
]

DEPARTMENTS = [
    "IT",
    "Finance",
    "Human Resources",
    "Sales",
    "Operations",
    "Security",
    "Development",
    "Support",
]

ENVIRONMENTS = ["production", "staging", "development", "testing"]
RAM_OPTIONS = [2, 4, 8, 16, 32, 64, 128]
CPU_OPTIONS = [1, 2, 4, 8, 16, 32]
STORAGE_OPTIONS = [64, 128, 256, 512, 1024, 2048, 4096]


def generate_inventory(output_path: str, rows: int = 1000) -> None:
    """Genera un inventario CSV con servidores ficticios."""
    fake = Faker()
    destination = Path(output_path)

    with open(destination, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=HEADERS)
        writer.writeheader()

        for server_number in range(1, rows + 1):
            department = random.choice(DEPARTMENTS)
            hostname_prefix = department.lower().replace(" ", "-")

            writer.writerow(
                {
                    "server_id": f"SRV-{server_number:04d}",
                    "hostname": f"{hostname_prefix}-{server_number:04d}",
                    "ip": fake.ipv4_private(),
                    "mac": fake.mac_address(),
                    "operating_system": random.choice(OPERATING_SYSTEMS),
                    "ram_gb": random.choice(RAM_OPTIONS),
                    "cpu_cores": random.choice(CPU_OPTIONS),
                    "storage_gb": random.choice(STORAGE_OPTIONS),
                    "department": department,
                    "owner": fake.name(),
                    "environment": random.choice(ENVIRONMENTS),
                }
            )


if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent
    generate_inventory(str(current_dir / "inventory.csv"), rows=1000)
    print("[INFO] Inventario generado en inventory.csv con 1000 servidores.")
