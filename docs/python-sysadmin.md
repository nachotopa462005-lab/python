# Python para Administradores de Sistemas Modernos

## ¿Por qué Python además de Bash?

Si bien **Bash** es el rey indiscutible para tareas rápidas en la shell y manipulación de archivos local, un SysAdmin moderno necesita **Python** por las siguientes razones:

1. **Manejabilidad de la Complejidad**: A medida que un script de Bash crece más allá de las 100 líneas, se vuelve difícil de mantener. Python ofrece una estructura de objetos y funciones mucho más legible.
2. **Bibliotecas Robustas**: Python tiene módulos nativos para interactuar con APIs (JSON), bases de datos y protocolos de red (SSH, SNMP) de forma mucho más segura que parseando texto con `awk` o `sed`.
3. **Multiplataforma**: Un script de Bash está limitado a entornos Unix. Un script de Python bien escrito puede ejecutarse en Linux, macOS y Windows sin cambios mayores.
4. **Integración con la Nube**: Las herramientas de infraestructura como código (IaC) y los SDKs de AWS (Boto3), Azure o Google Cloud están optimizados para Python.

### Conclusión
Bash es para **orquestar comandos del sistema**; Python es para **construir herramientas y automatizaciones complejas**.