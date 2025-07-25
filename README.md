# Team Poisonous Nmap Automation v2.0  

--------------------------------------------------------

## 🔥 Presentación/Presentation

<div align="center"> <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python"> <img src="https://img.shields.io/badge/Nmap-7.80%2B-green?logo=linux" alt="Nmap"> <img src="https://img.shields.io/badge/License-MIT-yellow" alt="Licencia"> <img src="https://img.shields.io/badge/Version-2.0-red" alt="Versión"> <img src="https://img.shields.io/github/stars/Whoam4/Nmap-Automation-Tool?style=social" alt="Stars"> </div>

**Creado por Mario**.

---

## 🔒 Licencia de Responsabilidad

Esta herramienta está destinada para un uso ético y la mejora de la seguridad. Cualquier uso indebido de esta herramienta es responsabilidad del usuario.

---

## ⚙️ Requisitos 

Asegúrate de tener Nmap y Python3 Instalado en el sistema. En sistemas basados en Debian/Ubuntu, puedes instalar Nmap con:
 
```sudo apt-get install nmap```

---

## 📥 Descarga e Instalación

Sigue estos pasos para clonar y configurar la herramienta en tu máquina local.

```bash
# Clona el repositorio
git clone https://github.com/Whoam4/Nmap-Automation-Tool.git

# Entra en el directorio del proyecto
cd TPA -Nmap.py

# Asegúrate de que el script tenga permisos de ejecución
chmod +x TPA -Nmap.py
```
# 🚀 Uso

Inicia el programa ejecutando el script de Python desde la terminal:

``` python3 TPA -Nmap.py ```

*Menú interactivo con opciones de escaneo y vulnerabilidades.*
![Menú principal de la herramienta](Exe2.PNG)

*Ejemplo de algunas opciones de escaneo de Nmap ejecutado por la herramienta.*
![Resultado de un escaneo de Nmap](Exe1.PNG)


---
### 🔝​ Puntos Positivos

1.**`Interfaz de Usuario Profesional`**:

La estructura de menús y los colores para destacar opciones y mensajes hacen que la herramienta sea intuitiva y fácil de usar.

2.**`Múltiples Funcionalidades`**:

Combina comandos básicos, detección de vulnerabilidades y enumeración SMB, lo que aumenta su utilidad.

3.**`Validación de IPs`**:

La función es_ip_valida asegura que el usuario introduzca entradas válidas, evitando errores en tiempo de ejecución.

4.**`.Logging`**:

Registrar comandos y salidas en un archivo es un excelente detalle para auditoría y depuración.

5.**`Uso de subprocess`**:

Ejecutar comandos con seguridad y capturar tanto la salida estándar como los errores proporciona flexibilidad.

