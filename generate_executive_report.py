from datetime import date
from pathlib import Path

import pandas as pd

from inventory_manager import filter_windows_or_low_ram, load_inventory


def find_latest_inventory_csv(directory: str) -> Path:
    """Busca el CSV de inventario mas reciente en el directorio indicado."""
    inventory_files = sorted(
        Path(directory).glob("inventory*.csv"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )

    if not inventory_files:
        raise FileNotFoundError("No se encontro ningun archivo inventory*.csv.")

    return inventory_files[0]


def generate_monthly_executive_report(input_dir: str, output_dir: str) -> Path:
    """
    Lee el ultimo inventario CSV y genera un Excel limpio para gerencia.

    El criterio reutiliza el filtro del paso anterior:
    - Windows Server.
    - Servidores con menos de 4GB de RAM.
    """
    latest_csv = find_latest_inventory_csv(input_dir)
    inventory = load_inventory(str(latest_csv))
    vulnerable_or_old = filter_windows_or_low_ram(inventory)

    report_date = date.today().strftime("%Y-%m")
    output_path = Path(output_dir) / f"executive_server_report_{report_date}.xlsx"

    clean_report = vulnerable_or_old[
        [
            "server_id",
            "hostname",
            "ip",
            "operating_system",
            "ram_gb",
            "cpu_cores",
            "storage_gb",
            "department",
            "owner",
            "environment",
        ]
    ].sort_values(["department", "hostname"])

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        clean_report.to_excel(writer, sheet_name="Vulnerable Servers", index=False)

        department_summary = (
            clean_report.groupby("department")
            .size()
            .reset_index(name="affected_servers")
            .sort_values("affected_servers", ascending=False)
        )
        department_summary.to_excel(writer, sheet_name="Summary", index=False)

    return output_path


if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent
    try:
        report_path = generate_monthly_executive_report(
            input_dir=str(current_dir),
            output_dir=str(current_dir),
        )
        print(f"[INFO] Informe ejecutivo generado: {report_path}")
    except FileNotFoundError as error:
        print(f"[ERROR] {error}")
    except OSError as error:
        print(f"[ERROR] No se pudo generar el informe: {error}")
