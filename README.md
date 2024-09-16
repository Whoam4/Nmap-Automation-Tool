# 👁️‍🗨️​ Ethical Hacking CheatSheet: Nmap & More

## Nmap
 ​**Nmap CheatSheet ❗**

| Command                                       | Description                                            |
|-----------------------------|--------------------------------------------------------|
| Detección de vulnerabilidades                                         | `nmap -v --script vuln TARGET`                                       |
| Escaneo completo con detección de vulnerabilidades                    | `sudo nmap -v -sS -sC -sV -T5 --script=vuln TARGET`                             |   
| Informe de vulnerabilidades                                          | `sudo nmap -v -sS -sC -sV -T5 --script=vuln -oX vulns.xml --webxml TARGE`                              |
| Reconocimiento de Hosts                                                 | `sudo nmap -sn TARGET `                                        |
| Descubrir todos los nodos de la red                               | `sudo nmap TARGET y el último valor cambiar por 0/24` / `sudo nmap 198.164.1.0/64`             |
| Descubrir puertos abiertos                                     | `sudo nmap -p- --open -sS --min-rate 5000 -v -n TARGET`                         |
| Escaneo de puertos                                                    | `sudo nmap -sS TARGET `  / `sudo nmap -sS IP(terminado en .0/24)     `             |
|Escaneo de servicios (la más intrusiva)                              | `sudo nmap -p- -sV TARGET` /  `sudo nmap -sV TARGET -p 80`                            |
| Generación de informe                                                | `sudo nmap -v --reason -sV -oX servicios.xml --webxml TARGET`                         |
| Escaneo completo con identificación de servicios                                               | `sudo nmap -sV -sC -p- Target` / `sudo nmap -sV -sC -sV -T5 (aumenta la Velocidad de escaneo) TARGET `                    |
| Identificación del sistema operativo                             | `sudo nmap -A -V TARGET` / `sudo nmap -v -0 TARGET`|
| Enumeración básica de servicios                                                                     | `sudo nmap -sCV -p 22,80 TARGET -oN targeted  `  
| Escaneo de versiones (más detallado)            |            `sudo nmap -sV --version-intensity 9 TARGET `          |
|Escaneo de scripts específicos (más enfocado en vulnerabilidades)                          |    `sudo nmap --script exploit,brute TARGET`    |
                                
|Detección de firewalls y sistemas de evasión         | `sudo nmap -f TARGET (Fragmentar paquetes para evitar firewalls) / sudo nmap -D RND:10 
                                                  TARGET ( Usar decoys para evitar detección)`        `sudo nmap --script http-enum TARGET`|                     
|Escaneo con traceroute:                           |       `sudo nmap --traceroute TARGET`                       |
|Escaneo de Puertos con Técnica de Stealth)                                                                            |   `sudo nmap -sS -p 1-65535 TARGET`    |
|Escaneo de Vulnerabilidades Web                                                                                   |   `sudo nmap --script http-vuln* TARGET`    |
|Escaneo de Hosts en un Rango de IPs        |   `sudo nmap -sP 192.168.1.1-50`    |
|Escaneo de Puertos Específicos con Técnica de Timing(evitar detección)        |   `sudo nmap -p 22,80,443 -T4 TARGET`    |
|Escaneo de Puertos con Evitación de IDS/IPS(Utiliza técnicas para evadir sistemas de detección y prevención de intrusiones)        |   `sudo nmap -sS -p 1-65535 -f -D RND:10 TARGET`    |
|Escaneo de scripts específicos (más enfocado en vulnerabilidades)        |   `sudo nmap --script exploit,brute TARGET`    |
|Escaneo de scripts específicos (más enfocado en vulnerabilidades)        |   `sudo nmap --script exploit,brute TARGET`    |

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
● Sirve para ganar datos de acceso a la confuracion de un sistema
● Trabaja en el puerto 161

`sudo nmap -v -sS -p 161 TARGET
cd /usr/share/nmap/scripts -> ls snmp*`

•Enumeración de SNMP con Comandos de Brute Force
`snmpenum -r TARGET`


### LIST SMB
```bash
smbclient -N -L \\\\10.129.42.253  # Listado SMB
smbclient \\\\10.129.42.253\\users  # Acceso por SMB
smbclient -U bob \\\\10.129.42.253\\users  # Acceso con usuario
```
### Identify MySQL databases
```bash
sudo nmap -sS -p 3306 TARGET.0/24
#El puerto 3306 es el de la base de datos MySQL
```






