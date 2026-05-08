![Python](https://img.shields.io/badge/PYTHON-3.13-blue)
![CLI](https://img.shields.io/badge/CLI-System%20Toolkit-green)
![Pandas](https://img.shields.io/badge/PANDAS-Inventarios-yellow)
![Pytest](https://img.shields.io/badge/PYTEST-Tests-red)
![Security](https://img.shields.io/badge/SECURITY-Logs%20%26%20Threat%20Intel-black)

# System Toolkit CLI

## Login

### Descripcion breve

Toolkit de administracion y seguridad desarrollado en Python. El proyecto permite automatizar comprobaciones del sistema operativo, analizar logs SSH, consultar inteligencia de amenazas, modelar dispositivos de red con POO, generar inventarios masivos y crear informes ejecutivos en Excel.

| Despliegue | URL |
|---|---|
| Local | `C:\Users\Nacho Topa\python` |
| Ejecucion | `.\venv\Scripts\python.exe` |

---

## Caracteristicas

- Menu principal por consola para ejecutar acciones del toolkit.
- Comprobacion de conectividad con `ping`.
- Revision de espacio libre en disco con alerta si queda menos del 20%.
- Parseo de logs `auth.log` para detectar intentos SSH fallidos.
- Conteo de IPs atacantes usando `set` y `dict`.
- Consulta de inteligencia de amenazas con `ipinfo.io`.
- Modelado de dispositivos de red usando herencia y polimorfismo.
- Generacion masiva de inventario CSV con 1000 servidores ficticios.
- Analisis de inventario con Pandas.
- Generacion de informes ejecutivos en Excel.
- Demonio horario con `schedule`.
- Tests unitarios con `pytest`.

---

## Tecnologias

### Backend / Automatizacion

| Tecnologia | Uso |
|---|---|
| Python 3.13 | Lenguaje principal |
| subprocess | Ejecucion de comandos del sistema |
| os / shutil | Revision de rutas y espacio en disco |
| urllib / json | Consulta y parseo de APIs |
| schedule | Ejecucion automatica cada hora |

### Datos

| Tecnologia | Uso |
|---|---|
| csv | Generacion de inventario |
| Faker | Datos ficticios de servidores |
| Pandas | Carga, filtrado y agrupacion de datos |
| OpenPyXL | Exportacion a Excel |

### Testing

| Tecnologia | Uso |
|---|---|
| pytest | Pruebas unitarias |
| with open | Lectura eficiente de logs |
| set / dict | IPs unicas y conteo por IP |

---

## Estructura del proyecto

```text
python/
|-- .gitignore
|-- README.md
|-- auth.log                         # Log SSH simulado
|-- sys_toolkit.py                   # Menu principal del toolkit
|-- os_utils.py                      # Ping y espacio libre en disco
|-- log_parser.py                    # Parseo de auth.log y conteo de IPs
|-- threat_intel.py                  # Consulta ipinfo.io y tabla de amenazas
|-- network_models.py                # POO: NetworkDevice, Router y Server
|-- generate_inventory.py            # Genera inventory.csv con Faker
|-- inventory_manager.py             # Filtros y agrupaciones con Pandas
|-- generate_executive_report.py     # Genera informe Excel mensual
|-- hourly_report_daemon.py          # Demonio horario con schedule
|-- test_toolkit.py                  # Tests unitarios con pytest
|-- requirements.txt                 # Dependencias del proyecto
|-- inventory.csv                    # Inventario generado
`-- executive_server_report_*.xlsx   # Informe ejecutivo generado
```

---

## Descargar y ejecutar

```powershell
cd "C:\Users\Nacho Topa\python"
.\venv\Scripts\python.exe sys_toolkit.py
```

Si necesitas instalar dependencias:

```powershell
.\venv\Scripts\python.exe -m pip install pandas openpyxl faker pytest schedule
```

---

## Ejemplos para probar funcionalidad

### Menu principal

```powershell
.\venv\Scripts\python.exe sys_toolkit.py
```

Opciones recomendadas:

```text
3
127.0.0.1
```

Comprueba si localhost responde al ping.

```text
4
C:\
```

Muestra espacio total, usado y libre del disco.

### Parseo de logs SSH

```powershell
.\venv\Scripts\python.exe log_parser.py
```

Salida esperada aproximada:

```text
192.168.1.45: 3
198.51.100.23: 2
203.0.113.10: 3
```

### Inteligencia de amenazas

```powershell
.\venv\Scripts\python.exe threat_intel.py
```

Muestra una tabla con IP atacante, intentos, pais y organizacion. Si no hay conexion o la API falla, el script muestra `N/A` sin romperse.

### Programacion orientada a objetos

```powershell
.\venv\Scripts\python.exe network_models.py
```

Muestra un router y un servidor con auditorias de seguridad distintas usando polimorfismo.

### Inventario masivo

```powershell
.\venv\Scripts\python.exe generate_inventory.py
.\venv\Scripts\python.exe inventory_manager.py
```

Genera `inventory.csv`, filtra servidores Windows Server o con menos de 4GB de RAM, y cuenta servidores por departamento.

### Informe ejecutivo en Excel

```powershell
.\venv\Scripts\python.exe generate_executive_report.py
```

Genera un archivo como:

```text
executive_server_report_2026-05.xlsx
```

El Excel contiene:

- `Vulnerable Servers`
- `Summary`

### Demonio horario

```powershell
.\venv\Scripts\python.exe hourly_report_daemon.py
```

Ejecuta el informe al iniciar y luego vuelve a generarlo cada hora. Para detenerlo:

```text
Ctrl + C
```

### Tests unitarios

```powershell
.\venv\Scripts\python.exe -m pytest -q
```

Salida verificada:

```text
..                                                                       [100%]
2 passed in 0.31s
```

---

## Autor

Desarrollado por Ignacio Topa durante practicas de Python, automatizacion, seguridad y analisis de datos.
