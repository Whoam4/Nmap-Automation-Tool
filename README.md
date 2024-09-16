# Nmap

## 👁️‍🗨️​ Nmap CheatSheet

*Detección de vulnerabilidades*

`nmap-v-script vuln TARGET`

*Escaneo completo con detección de vulnerabilidades*

`sudo nmap -v-sS-C-V-T5-script-vuln TARGET`

*Informe de vulnerabilidades*

`sudo nmap -v-s5-SC-V-T5-script-vuln -oX vulns.xml --webxml TARGET`

Reconocimiento de Hosts

`sudo nmap -sn TARGET`

Descubrir todos los nodos de la red

sudo nmap TARGET y el último valor cambiar por 0/24

`sudo nmap 198.164.1.0/64`

Descubrir puertos abiertos

`sudo nmap-popen s5min-rate 5000-v-n TARGET`

Escaneo de puertos

`sudo nmap -sS TARGET`

`sudo nmap -sS IP(terminado en .0/24)`

Escaneo de servicios (la más intrusiva)

`sudo nmap -p--V TARGET`

`sudo nmap -SV TARGET -p 80`
