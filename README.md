# Nmap

## 👁️‍🗨️​ Nmap CheatSheet

| Command                                       | Description                                            |
|-----------------------------|--------------------------------------------------------|
| Detección de vulnerabilidades                   | `nmap -v --script vuln TARGET`                                       |
| Escaneo completo con detección de vulnerabilidades                    | `sudo nmap -v -sS -sC -sV -T5 --script=vuln TARGET`                             |   
| Informe de vulnerabilidades                | `sudo nmap -v -sS -sC -sV -T5 --script=vuln -oX vulns.xml --webxml TARGE`T                              |
| Reconocimiento de Hosts                             | `sudo nmap -sn TARGET `                                        |
| Descubrir todos los nodos de la red                       | `sudo nmap TARGET y el último valor cambiar por 0/24` \n `sudo nmap 198.164.1.0/64`             |
| Descubrir puertos abiertos                             | `sudo nmap -p- --open -sS --min-rate 5000 -v -n TARGET`                         |
| Escaneo de puertos                          | `sudo nmap -sS TARGET `  / `sudo nmap -sS IP(terminado en .0/24)     `             |
|Escaneo de servicios (la más intrusiva)                              | `sudo nmap -p- -sV TARGET` /  `sudo nmap -sV TARGET -p 80`                            |
| Generación de informe                   | `sudo nmap -v --reason -sV -oX servicios.xml --webxml TARGET`                         |
| Escaneo completo con identificación de servicios          | `sudo nmap -sV -sC -p- Target` / `sudo nmap -sV -sC -sV -T5 (aumenta la Velocdiad de escaneo) TARGET `                    |
| Identificación del sistema operativo                             | `sudo nmap -A -V TARGET` / `sudo nmap -v -0 TARGET`|
| Enumeración básica de servicios                             | `sudo nmap -sCV -p 22,80 TARGET -oN targeted  `                                 

