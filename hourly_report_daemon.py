import time
from pathlib import Path

import schedule

from generate_executive_report import generate_monthly_executive_report


def run_report_job() -> None:
    """Ejecuta el informe ejecutivo usando el ultimo CSV disponible."""
    current_dir = Path(__file__).resolve().parent

    try:
        report_path = generate_monthly_executive_report(
            input_dir=str(current_dir),
            output_dir=str(current_dir),
        )
        print(f"[INFO] Informe generado: {report_path}")
    except FileNotFoundError as error:
        print(f"[ERROR] {error}")
    except OSError as error:
        print(f"[ERROR] No se pudo escribir el informe: {error}")


def start_hourly_daemon() -> None:
    """Mantiene el proceso vivo y ejecuta el informe cada hora."""
    schedule.every(1).hours.do(run_report_job)
    print("[INFO] Demonio iniciado. Ejecutando informe cada hora.")

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    run_report_job()
    start_hourly_daemon()
