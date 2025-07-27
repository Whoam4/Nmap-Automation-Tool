# 👁️‍🗨️​ Ethical Hacking CheatSheet: Nmap & More

## Nmap
 ​**Nmap CheatSheet ❗**

- EN -  Note:  If you come from the automated tool for whatever reason, here you can learn the same thing only in a more extensive, professional and theoretical way.
- ES -  Nota:  Si vienes de la herramienta automatizada, por lo que sea, aquí puedes aprender lo mismo, solo que de manera más extensa, profesional y teórica.
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

## 🤖 AUTOMATIZACIÓN AVANZADA CON TPA-NMAP.PY
**Interfaz interactiva que ejecuta todos los comandos anteriores sin memorización**

### 🗂️ Catálogo completo de operaciones
```bash
# DESCUBRIMIENTO DE RED
[1] Ping Sweep            → nmap -sn
[2] ARP Scan              → nmap -PR
[3] TCP SYN Discovery     → nmap -PS
[4] UDP Discovery         → nmap -PU
[5] Full Discovery        → nmap -sn -PE -PP -PM -PO
[6] Traceroute            → nmap --traceroute

# ESCANEO DE PUERTOS
[1] TCP SYN (Stealth)     → nmap -sS
[2] TCP Connect           → nmap -sT
[3] UDP Scan              → nmap -sU --top-ports 1000
[4] TCP ACK (Firewalls)   → nmap -sA
[5] Window Scan           → nmap -sW
[6] Maimon Scan           → nmap -sM
[7] FIN Scan              → nmap -sF
[8] NULL Scan             → nmap -sN
[9] XMAS Scan             → nmap -sX
[10] Top 1000 puertos     → nmap --top-ports 1000
[11] Todos los puertos    → nmap -p-
[12] Puertos personalizados → nmap -p [PUERTOS]

# DETECCIÓN DE SERVICIOS
[1] Versiones básicas     → nmap -sV
[2] Versiones agresivas   → nmap -sV --version-intensity 9
[3] Detección de SO       → nmap -O
[4] Scripts default       → nmap -sC -sV
[5] Escaneo agresivo      → nmap -A
[6] WAF/IPS/IDS           → nmap --script http-waf-detect,http-waf-fingerprint
[7] Banner grabbing       → nmap --script banner
[8] Tech web              → nmap --script http-enum,http-headers,http-methods

# VULNERABILIDADES
[1] General               → nmap --script vuln
[2] SMB                   → nmap --script smb-vuln*
[3] SSH                   → nmap --script ssh-*
[4] HTTP                  → nmap --script http-vuln*
[5] FTP                   → nmap --script ftp-*
[6] SSL/TLS               → nmap --script ssl-*
[7] Malware               → nmap --script malware
[8] XML completo          → nmap -sV --script=vuln -oX

# ENUMERACIÓN
[1] SMB completa          → nmap --script smb-enum-*,smb-ls,smb-os-discovery
[2] SNMP                  → nmap -sU --script snmp-*
[3] DNS                   → nmap --script dns-*
[4] HTTP/HTTPS            → nmap --script http-*enum*,http-methods
[5] FTP                   → nmap --script ftp-*enum*,ftp-anon
[6] SSH                   → nmap --script ssh-*enum*,ssh-auth-methods
[7] Bases de datos        → nmap --script mysql-*,ms-sql-*,oracle-*
[8] LDAP                  → nmap --script ldap-*

# EVASIÓN
[1] Fragmentación         → nmap -f
[2] Señuelos              → nmap -D [IPs]
[3] IP Spoofing           → nmap -S [IP_FALSA]
[4] Randomizar hosts      → nmap --randomize-hosts
[5] Timing lento (T0)     → nmap -T0
[6] Cambiar MTU           → nmap --mtu [VALOR]
[7] Proxy/Tor             → nmap --proxies [PROXY]

# SCRIPTS PERSONALIZADOS
[1] Script específico     → nmap --script [NOMBRE]
[2] Listar scripts        → nmap --script-help all
[3] Por categoría         → nmap --script [CATEGORÍA]
[4] Combo Discovery       → nmap -sS -sV -sC --script discovery,enumeration,vuln -A
[5] Escaneo completo      → nmap -sS -sV -sC -A -p- --script vuln,enum,discovery -oA


## 🔢​ SMB Enumeration

| Command | Description |
|---------|-------------|
| Sirve para encontrar carpetas y archivos compartidos. Suele trabajar en los puertos 139 y 445 | `sudo nmap -v -sS -p 139,445 TARGET` |
| Ver scripts de tareas automatizadas | `cd /usr/share/nmap/scripts && ls` |
| Añadir filtro dentro de la carpeta | `ls smb*` |
| Enumeración de Usuarios SMB | `smbclient -L \\TARGET -U ""` |
| Escaneo de SMB para Vulnerabilidades Comunes | `nmap --script smb-vuln* TARGET` |
| Enumeración de Recursos Compartidos | `smbclient -L \\TARGET -U USERNAME` |
| Enumeración de Políticas de Seguridad SMB | `sudo nmap -p 139,445 --script smb-security-mode TARGET` |
| Obtención de Información de la Versión del Protocolo SMB | `sudo nmap -p 139,445 --script smb-protocols TARGET` |


## ​SNMP Enumeration (Could be Vulnv)
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

## 🔒 Identify database MySQL
`sudo nmap -sS -p 3306 TARGET.0/24`
### PostgreSQL
`sudo nmap -sS -p 5432 TARGET.0/24 PostgreSQL`
### Microsoft SQL Server
`sudo nmap -sS -p 1433 TARGET.0/24`
`
### Oracle Database
`sudo nmap -sS -p 1521 TARGET.0/24`
















