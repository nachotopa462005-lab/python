from pathlib import Path

import pandas as pd


def load_inventory(csv_path: str) -> pd.DataFrame:
    """Carga el inventario CSV con pandas."""
    return pd.read_csv(csv_path)


def filter_windows_or_low_ram(inventory: pd.DataFrame) -> pd.DataFrame:
    """Filtra servidores Windows Server o con menos de 4GB de RAM."""
    windows_servers = inventory["operating_system"].str.contains(
        "Windows Server",
        case=False,
        na=False,
    )
    low_ram_servers = inventory["ram_gb"] < 4

    return inventory[windows_servers | low_ram_servers]


def count_servers_by_department(inventory: pd.DataFrame) -> pd.DataFrame:
    """Agrupa los servidores por departamento y cuenta cuantos tiene cada area."""
    return (
        inventory.groupby("department")
        .size()
        .reset_index(name="server_count")
        .sort_values("server_count", ascending=False)
    )


def show_inventory_report(csv_path: str) -> None:
    inventory = load_inventory(csv_path)
    filtered_inventory = filter_windows_or_low_ram(inventory)
    department_counts = count_servers_by_department(inventory)

    print("[INFO] Servidores Windows Server o con menos de 4GB de RAM:")
    print(
        filtered_inventory[
            [
                "server_id",
                "hostname",
                "operating_system",
                "ram_gb",
                "department",
                "environment",
            ]
        ].to_string(index=False)
    )

    print("\n[INFO] Conteo de servidores por departamento:")
    print(department_counts.to_string(index=False))


if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent
    show_inventory_report(str(current_dir / "inventory.csv"))
