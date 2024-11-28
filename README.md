# Automatización  - Script de Nmap

--------------------------------------------------------

## 🔥 Presentación

**Nmap Security Script** es una herramienta interactiva diseñada para facilitar tareas de seguridad informática mediante el uso de Nmap. Permite a los usuarios ejecutar funciones de escaneo, detección de vulnerabilidades y enumeración SMB, todo a través de un menú fácil de usar. Creado por **Mario**.

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
git clone https://github.com/Whoam4/Nmap-ScriptTool.git

# Entra en el directorio del proyecto
cd Nmap-ScriptTool 

# Asegúrate de que el script tenga permisos de ejecución
chmod +x Nmap-Script-Tool.py
```
# 🚀 Uso

Inicia el programa ejecutando el script de Python desde la terminal:

``` python3 Nmap-Script-Tool.py ```

### 🔝​ Puntos Positivos

1.**`Interfaz de Usuario Profesional`**:

La estructura de menús y los colores para destacar opciones y mensajes hacen que la herramienta sea intuitiva y fácil de usar.

2.**`Múltiples Funcionalidades`**:

Combina comandos básicos, detección de vulnerabilidades y enumeración SMB, lo que aumenta su utilidad.

3.**`Validación de IPs`**:

La función es_ip_valida asegura que el usuario introduzca entradas válidas, evitando errores en tiempo de ejecución.

4**`.Logging`**:

Registrar comandos y salidas en un archivo es un excelente detalle para auditoría y depuración.

5.**`Uso de subprocess`**:

Ejecutar comandos con seguridad y capturar tanto la salida estándar como los errores proporciona flexibilidad.

