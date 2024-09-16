# 👁️‍🗨️​ Ethical Hacking CheatSheet: Nmap & More

## Nmap
 ​**Nmap CheatSheet ❗**

## Nmap CheatSheet 📋

| Command                                                                   | Description                                                                                                 |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Detección de vulnerabilidades                                               | `nmap -v --script vuln TARGET`                                                                             |
| Escaneo completo con detección de vulnerabilidades                          | `sudo nmap -v -sS -sC -sV -T5 --script=vuln TARGET`                                                        |
| Informe de vulnerabilidades                                                 | `sudo nmap -v -sS -sC -sV -T5 --script=vuln -oX vulns.xml --webxml TARGET`                                  |
| Reconocimiento de Hosts                                                     | `sudo nmap -sn TARGET`                                                                                     |
| Descubrir todos los nodos de la red                                          | `sudo nmap TARGET` (cambiar el último valor por 0/24) / `sudo nmap 198.164.1.0/24`                         |
| Descubrir puertos abiertos                                                   | `sudo nmap -p- --open -sS --min-rate 5000 -v -n TARGET`                                                    |
| Escaneo de puertos                                                           | `sudo nmap -sS TARGET` / `sudo nmap -sS IP(terminado en .0/24)`                                           |
| Escaneo de servicios (la más intrusiva)                                      | `sudo nmap -p- -sV TARGET` / `sudo nmap -sV TARGET -p 80`                                                  |
| Generación de informe                                                        | `sudo nmap -v --reason -sV -oX servicios.xml --webxml TARGET`                                              |
| Escaneo completo con identificación de servicios                             | `sudo nmap -sV -sC -p- TARGET` / `sudo nmap -sV -sC -sV -T5 TARGET` (aumenta la velocidad de escaneo)       |
| Identificación del sistema operativo                                        | `sudo nmap -A -V TARGET` / `sudo nmap -v -O TARGET`                                                        |
| Enumeración básica de servicios                                             | `sudo nmap -sCV -p 22,80 TARGET -oN targeted`                                                              |
| Escaneo de versiones (más detallado)                                         | `sudo nmap -sV --version-intensity 9 TARGET`                                                               |
| Escaneo de scripts específicos (más enfocado en vulnerabilidades)           | `sudo nmap --script exploit,brute TARGET`                                                                  |
| Detección de firewalls y sistemas de evasión                                 | `sudo nmap -f TARGET` (Fragmentar paquetes para evitar firewalls) / `sudo nmap -D RND:10 TARGET` (Usar decoys para evitar detección)` |
| Escaneo con traceroute                                                       | `sudo nmap --traceroute TARGET`                                                                            |
| Escaneo de puertos con técnica de stealth                                    | `sudo nmap -sS -p 1-65535 TARGET`                                                                          |
| Escaneo de vulnerabilidades web                                             | `sudo nmap --script http-vuln* TARGET`                                                                     |
| Escaneo de hosts en un rango de IPs                                          | `sudo nmap -sP 192.168.1.1-50`                                                                            |
| Escaneo de puertos específicos con técnica de timing (evitar detección)      | `sudo nmap -p 22,80,443 -T4 TARGET`                                                                        |
| Escaneo de puertos con evitación de IDS/IPS (Utiliza técnicas para evadir sistemas de detección y prevención de intrusiones.)                             | `sudo nmap -sS -p 1-65535 -f -D RND:10 TARGET`                                                             |


## SMB Enumeration

| Command | Description |
|---------|-------------|
| Sirve para encontrar carpetas y archivos compartidos. Suele trabajar en los puertos 139 y 44 | `sudo nmap -v -sS -p 139,445 TARGET` |
|Ver scripts de tareas automatizadas: | `cd /usr/share/nmap/scripts -> ls` |
| Añadir filtro dentro de la carpeta | `ls smb* ` |
| Enumeración de Usuarios SMB | `smbclient -L \\TARGET -U "" `. |
| Escaneo de SMB para Vulnerabilidades Comunes | `nmap --script smb-vuln* TARGET `. |
| Ejecutar un script en concreto: | `sudo nmap -v -sS -p 139,445 --script=SCRIPT TARGET `. |
| Ejecutar un script en concreto: | `sudo nmap -v -sS -p 139,445 --script=SCRIPT TARGET `. |
| Ejecutar un script en concreto: | `sudo nmap -v -sS -p 139,445 --script=SCRIPT TARGET `. |
| Ejecutar un script en concreto: | `sudo nmap -v -sS -p 139,445 --script=SCRIPT TARGET `. |

## SNMP Enumeration (Could be Vulnv)
SNMP (Simple Network Management Protocol) es un protocolo utilizado para la gestión y monitoreo de redes. Puede ser explotado para obtener información sobre la configuración del sistema y posibles vulnerabilidades.

### Comandos de Enumeración SNMP
| Command                                       | Description                                           |
|-----------------------------------------------|-------------------------------------------------------|
| `sudo nmap -v -sS -p 161 TARGET`              | Escaneo SNMP en el puerto 161 del objetivo.          |
| `cd /usr/share/nmap/scripts && ls snmp*`      | Listar scripts SNMP disponibles en Nmap.             |
| `snmpenum -r TARGET`                         | Enumeración SNMP usando comandos de brute force.     |

### LIST SMB
```bash
smbclient -N -L \\\\10.129.42.253  # Listado SMB de recursos compartidos
smbclient \\\\10.129.42.253\\users  # Acceso a la carpeta 'users' en SMB
smbclient -U bob \\\\10.129.42.253\\users  # Acceso a la carpeta 'users' con el usuario 'bob'
```

## Identify database MySQL
`sudo nmap -sS -p 3306 TARGET.0/24`
### PostgreSQL
`sudo nmap -sS -p 5432 TARGET.0/24 PostgreSQL`
### Microsoft SQL Server
`sudo nmap -sS -p 1433 TARGET.0/24`
`
### Oracle Database
`sudo nmap -sS -p 1521 TARGET.0/24`







"El puerto 3306 es el puerto estándar de MySQL"








