# Team Poisonous Nmap Automation v2.0  

--------------------------------------------------------

## 🔥 Presentación/Presentation

ES: Esta herramienta permite realizar escaneos automatizados de redes y detección de vulnerabilidades utilizando Nmap. Diseñada para simplificar y optimizar el proceso de recopilación de información sobre hosts, servicios y posibles vulnerabilidades, esta herramienta ofrece un menú interactivo que permite al usuario seleccionar diferentes opciones de escaneo, incluyendo detección de vulnerabilidades y enumeración de SMB. 

EN: This tool allows automated network scanning and vulnerability detection using Nmap. Designed to simplify and streamline the process of gathering information about hosts, services, and potential vulnerabilities, this tool offers an interactive menu that allows the user to select different scanning options, including vulnerability detection and SMB enumeration.

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

