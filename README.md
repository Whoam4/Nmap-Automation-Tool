# Team Poisonous Nmap Automation v2.0  

--------------------------------------------------------
══════════════════════════════════════════════

 ████████╗███████╗ █████╗ ███╗   ███╗
 ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
    ██║   █████╗  ███████║██╔████╔██║
    ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
    ██║   ███████╗██║  ██║██║ ╚═╝ ██║
    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
                                      
██████╗  ██████╗ ██╗███████╗ ██████╗ ███╗   ██╗ ██████╗ ██╗   ██╗███████╗
██╔══██╗██╔═══██╗██║██╔════╝██╔═══██╗████╗  ██║██╔═══██╗██║   ██║██╔════╝
██████╔╝██║   ██║██║███████╗██║   ██║██╔██╗ ██║██║   ██║██║   ██║███████╗
██╔═══╝ ██║   ██║██║╚════██║██║   ██║██║╚██╗██║██║   ██║██║   ██║╚════██║
██║     ╚██████╔╝██║███████║╚██████╔╝██║ ╚████║╚██████╔╝╚██████╔╝███████║
╚═╝      ╚═════╝ ╚═╚══════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝


**Creado por Mario**.

<img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&style=for-the-badge" alt="Python">
<img src="https://img.shields.io/badge/🛡️%20Nmap-7.80%2B-green?style=for-the-badge" alt="Nmap">
<img src="https://img.shields.io/badge/📜%20TPA_License-Especial-4c1?style=for-the-badge" alt="Licencia Especial TPA">
<img src="https://img.shields.io/badge/⚙️%20Versión-2.0-red?style=for-the-badge" alt="Versión 2.0">
<img src="https://img.shields.io/badge/👨‍💻%20Creado%20por-Un%20Pentester-blueviolet?style=for-the-badge" alt="Creado por un Pentester">
<img src="https://img.shields.io/badge/🚀%20Top%202%20Scripts-automatización-orange?style=for-the-badge" alt="Top 2 Scripts automatización">




---

### 👤 Creado por Mario

---

## 🌟 ¿Por Qué Elegir Nuestra Herramienta?

Team Poisonous Nmap Automation revoluciona la forma de realizar auditorías de red al combinar el poder de Nmap con una interfaz intuitiva.

✅ 12 categorías de escaneo en menús interactivos  
✅ Automatización inteligente de técnicas avanzadas  
✅ Gestión profesional de resultados y reportes  
✅ Detección de vulnerabilidades con un solo clic  
✅ Técnicas de evasión para pruebas de penetración reales  

> *"La herramienta más completa que he usado para automatizar Nmap - ahorra horas de trabajo"*  
> – Hacker Ético Certificado

---

## 🔥 Características Destacadas

| Categoría      | Funcionalidades Clave                                                                 |
|----------------|----------------------------------------------------------------------------------------|
| 🌐 Descubrimiento | Ping Sweep, ARP Scan, TCP SYN Discovery, Traceroute                                   |
| 🔍 Escaneo        | 12 técnicas incluyendo Stealth, XMAS, NULL y UDP Scans                                |
| 🛡️ Vulnerabilidades | Detección SMB, SSH, HTTP, SSL y escaneo completo con XML                            |
| 📋 Enumeración    | SMB, SNMP, DNS, HTTP, FTP, SSH, Bases de Datos                                       |
| 🥷 Evasión         | Fragmentación, IP Spoofing, Señuelos, Proxy/Tor                                      |
| 📊 Reportes       | Estadísticas, Exportación Consolidada, Limpieza Inteligente                         |

---

## 🚀 Instalación en 30 Segundos

Asegúrate de tener **Python 3** y **Nmap** instalado.

```bash
# Instalar Nmap (Debian/Ubuntu)
sudo apt-get install nmap

# Clonar el repositorio
git clone https://github.com/Whoam4/TPA-Nmap-Script.git

# Entrar en el directorio
cd TPA-Nmap-Script

# Ejecutar la herramienta
python3 TPA-Nmap.py
```

### 🧭 Menú Principal Interactivo
══════════════════════════════════════

| Opción | Descripción                          |
|--------|--------------------------------------|
| [1]    | 🌐 Descubrimiento de Red             |
| [2]    | 🔍 Escaneo de Puertos                |
| [3]    | 🔧 Detección de Servicios            |
| [4]    | 🛡️ Detección de Vulnerabilidades     |
| [5]    | 📋 Enumeración de Servicios          |
| [6]    | 🥷 Técnicas de Evasión               |
| [7]    | ⚡ Scripts Personalizados            |
| [8]    | 📊 Estadísticas                      |
| [9]    | 📤 Exportar Resultados               |
| [10]   | 🧹 Limpiar Archivos                  |
| [0]    | 🚪 Salir                             |


---




### 🕵️‍♂️ Demostración Práctica
══════════════════════════════════════

*Menú interactivo con opciones de escaneo y vulnerabilidades.*
![Menú principal de la herramienta](Exe2.PNG)

*Ejemplo de algunas opciones de escaneo de Nmap ejecutado por la herramienta.*
![Resultado de un escaneo de Nmap](Exe1.PNG)

---

### 📊 Gestión Profesional de Resultados
🧠 Registro automático
Cada comando ejecutado queda registrado en nmap_scans.log, lo que permite revisar tu historial completo y auditar tu trabajo sin perder detalle.

🗂️ Archivos timestamp inteligentes
Los resultados se guardan con nombre automático y fecha, como:
vuln_scan_20240725_1423.txt
Ideal para identificar rápidamente qué se hizo y cuándo.

📤 Exportación consolidada
Con un solo clic puedes generar informes completos listos para entregar o documentar auditorías.

📈 Estadísticas avanzadas al instante
La herramienta calcula métricas de rendimiento para que midas tu eficiencia en tiempo real.


### 📊 ESTADÍSTICAS DE ESCANEOS

• 🧪 Comandos ejecutados:      24
• ❌ Errores detectados:        2
• 📁 Archivos generados:       15
• ✅ Tasa de éxito:           91.7%


---

### ⚠️ Uso Ético y Responsable

💡 Esta herramienta está diseñada exclusivamente para profesionales y entornos controlados.
El mal uso puede tener consecuencias legales graves.

✅ Está permitido en:

- Redes propias con autorización explícita

- Laboratorios de pruebas

- Actividades de pentesting legales

🚫 Está prohibido en:

- Redes de terceros sin permiso

- Sistemas en producción sin autorización

- Actividades maliciosas

🔐 ¡El hacking ético empieza con la responsabilidad!

---

## 🚨 Advertencia: El uso no autorizado en redes ajenas es ilegal y puede tener consecuencias legales graves.

### 🌟 Ventajas Competitivas
1. Interfaz Profesional Intuitiva
Menús con colores y formato claro que guían al usuario paso a paso

2. Automatización de Comandos Complejos
Convierte técnicas avanzadas de Nmap en selecciones simples:

```bash
# Técnica de Evasión con Señuelos
if opcion == "2":
    decoys = input("Introduce IPs señuelo separadas por comas: ")
    comando = f"nmap -D {decoys} {objetivo}"
```
3. Validación Inteligente de Entradas
Sistema que verifica IPs/dominios antes de ejecutar escaneos:
```bash
def es_ip_valida(ip):
    patron_ip = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?:/[0-9]{1,2})?$")
    patron_dominio = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}$")
    return patron_ip.match(ip) or patron_dominio.match(ip)
```

4. Gestión Avanzada de Resultados
Sistema todo-en-uno para manejo de outputs:

Guardado automático en múltiples formatos

Estadísticas de ejecución

Limpieza selectiva de archivos

---

### 📜 Licencia
Este proyecto está licenciado bajo la Licencia MIT.
Puedes usarlo, modificarlo y compartirlo libremente, siempre con responsabilidad ética.

---

### ⬇️ Descarga ahora y transforma tus auditorías
<img src="https://visitor-badge.laobi.icu/badge?page_id=Whoam4.Nmap-Automation-Tool" alt="Visitas"> <img src="https://img.shields.io/github/last-commit/Whoam4/Nmap-Automation-Tool?color=blue" alt="Último commit">
Creado con ❤️ por Mario

---
