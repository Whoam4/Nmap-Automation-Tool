import subprocess
import re
import logging
import os
from datetime import datetime

# Configuración del logging
logging.basicConfig(filename='nmap_scans.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def banner():
    print("\033[1;92m")
    print(" ████████╗███████╗ █████╗ ███╗   ███╗")
    print(" ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║")
    print("    ██║   █████╗  ███████║██╔████╔██║")
    print("    ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║")
    print("    ██║   ███████╗██║  ██║██║ ╚═╝ ██║")
    print("    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝")
    print()
    print("██████╗  ██████╗ ██╗███████╗ ██████╗ ███╗   ██╗ ██████╗ ██╗   ██╗███████╗")
    print("██╔══██╗██╔═══██╗██║██╔════╝██╔═══██╗████╗  ██║██╔═══██╗██║   ██║██╔════╝")
    print("██████╔╝██║   ██║██║███████╗██║   ██║██╔██╗ ██║██║   ██║██║   ██║███████╗")
    print("██╔═══╝ ██║   ██║██║╚════██║██║   ██║██║╚██╗██║██║   ██║██║   ██║╚════██║")
    print("██║     ╚██████╔╝██║███████║╚██████╔╝██║ ╚████║╚██████╔╝╚██████╔╝███████║")
    print("╚═╝      ╚═════╝ ╚═╚══════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝")
    print("\033[0m")
    print("\033[1;96mHerramienta de Automatización Avanzada de Nmap v2.0\033[0m")
    print("Creado por Team Poisonous -M\n")

def es_ip_valida(ip):
    """Validar si una IP, dominio o rango es válido."""
    patron_ip = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?:/[0-9]{1,2})?$")
    patron_dominio = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}$")
    return patron_ip.match(ip) is not None or patron_dominio.match(ip) is not None or ip.count('.') >= 1

def ejecutar_comando(comando, guardar_archivo=False, nombre_archivo=""):
    try:
        print(f"\n\033[1;93m[+] Ejecutando: {comando}\033[0m\n")
        resultado = subprocess.run(comando, shell=True, text=True, capture_output=True)
        print(resultado.stdout)
        
        # Guardar en archivo si se especifica
        if guardar_archivo and nombre_archivo:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            archivo = f"{nombre_archivo}_{timestamp}.txt"
            with open(archivo, 'w') as f:
                f.write(f"Comando: {comando}\n")
                f.write(f"Fecha: {datetime.now()}\n")
                f.write("="*50 + "\n")
                f.write(resultado.stdout)
            print(f"\033[1;92m[+] Resultado guardado en: {archivo}\033[0m")
        
        logging.info(f'Comando ejecutado: {comando}\nSalida:\n{resultado.stdout}')
        if resultado.stderr:
            print(f"\033[1;91m[-] Error: {resultado.stderr}\033[0m")
            logging.error(f'Error en el comando: {comando}\nError:\n{resultado.stderr}')
    except Exception as e:
        print(f"\033[1;91m[-] Ocurrió un error: {str(e)}\033[0m")
        logging.error(f'Ocurrió un error: {str(e)}')

def menu_descubrimiento_red():
    print("\n\033[1;96m🌐 DESCUBRIMIENTO DE RED\033[0m")
    print("┌───────────┬─────────────────────────────────────────────────────────┐")
    print("│ \033[1;94mOpción\033[0m    │ Descripción                                                 │")
    print("├───────────┼─────────────────────────────────────────────────────────┤")
    print("│ \033[1;92m[1]\033[0m       │ Ping Sweep - Descubrir hosts activos                       │")
    print("│ \033[1;92m[2]\033[0m       │ Escaneo ARP - Red local                                     │")
    print("│ \033[1;92m[3]\033[0m       │ Descubrimiento TCP SYN                                      │")
    print("│ \033[1;92m[4]\033[0m       │ Descubrimiento UDP                                          │")
    print("│ \033[1;92m[5]\033[0m       │ Escaneo completo de red                                     │")
    print("│ \033[1;92m[6]\033[0m       │ Traceroute con Nmap                                         │")
    print("└───────────┴─────────────────────────────────────────────────────────┘")
    
    opcion = input("\nSelecciona una opción: ").strip()
    
    if opcion in ["1", "2", "3", "4", "5", "6"]:
        objetivo = input("Introduce el objetivo (IP/CIDR): ").strip()
        guardar = input("¿Guardar resultado en archivo? (s/n): ").strip().lower() == 's'
        
        if opcion == "1":
            ejecutar_comando(f"nmap -sn {objetivo}", guardar, "ping_sweep")
        elif opcion == "2":
            ejecutar_comando(f"nmap -PR {objetivo}", guardar, "arp_scan")
        elif opcion == "3":
            ejecutar_comando(f"nmap -PS {objetivo}", guardar, "tcp_syn_discovery")
        elif opcion == "4":
            ejecutar_comando(f"nmap -PU {objetivo}", guardar, "udp_discovery")
        elif opcion == "5":
            ejecutar_comando(f"nmap -sn -PE -PP -PM -PO {objetivo}", guardar, "full_discovery")
        elif opcion == "6":
            ejecutar_comando(f"nmap --traceroute {objetivo}", guardar, "traceroute")

def menu_escaneo_puertos():
    print("\n\033[1;96m🔍 ESCANEO DE PUERTOS\033[0m")
    print("┌───────────┬─────────────────────────────────────────────────────────┐")
    print("│ \033[1;94mOpción\033[0m    │ Descripción                                                 │")
    print("├───────────┼─────────────────────────────────────────────────────────┤")
    print("│ \033[1;92m[1]\033[0m       │ TCP SYN Scan (Stealth)                                      │")
    print("│ \033[1;92m[2]\033[0m       │ TCP Connect Scan                                            │")
    print("│ \033[1;92m[3]\033[0m       │ UDP Scan                                                    │")
    print("│ \033[1;92m[4]\033[0m       │ TCP ACK Scan (Firewall detection)                          │")
    print("│ \033[1;92m[5]\033[0m       │ TCP Window Scan                                             │")
    print("│ \033[1;92m[6]\033[0m       │ TCP Maimon Scan                                             │")
    print("│ \033[1;92m[7]\033[0m       │ FIN Scan                                                    │")
    print("│ \033[1;92m[8]\033[0m       │ NULL Scan                                                   │")
    print("│ \033[1;92m[9]\033[0m       │ XMAS Scan                                                   │")
    print("│ \033[1;92m[10]\033[0m      │ Top 1000 puertos TCP                                       │")
    print("│ \033[1;92m[11]\033[0m      │ Todos los puertos TCP (1-65535)                            │")
    print("│ \033[1;92m[12]\033[0m      │ Puertos específicos                                         │")
    print("└───────────┴─────────────────────────────────────────────────────────┘")
    
    opcion = input("\nSelecciona una opción: ").strip()
    
    if opcion in map(str, range(1, 13)):
        objetivo = input("Introduce el objetivo (IP o dominio): ").strip()
        if not es_ip_valida(objetivo):
            print("\033[1;91m[-] Objetivo no válido.\033[0m")
            return
        
        guardar = input("¿Guardar resultado en archivo? (s/n): ").strip().lower() == 's'
        timing = input("Timing template (0-5, default 3): ").strip() or "3"
        
        comandos = {
            "1": f"nmap -sS -T{timing} {objetivo}",
            "2": f"nmap -sT -T{timing} {objetivo}",
            "3": f"nmap -sU --top-ports 1000 -T{timing} {objetivo}",
            "4": f"nmap -sA -T{timing} {objetivo}",
            "5": f"nmap -sW -T{timing} {objetivo}",
            "6": f"nmap -sM -T{timing} {objetivo}",
            "7": f"nmap -sF -T{timing} {objetivo}",
            "8": f"nmap -sN -T{timing} {objetivo}",
            "9": f"nmap -sX -T{timing} {objetivo}",
            "10": f"nmap --top-ports 1000 -T{timing} {objetivo}",
            "11": f"nmap -p- -T{timing} {objetivo}",
            "12": ""
        }
        
        if opcion == "12":
            puertos = input("Introduce los puertos (ej: 22,80,443 o 1-1000): ").strip()
            comando = f"nmap -p {puertos} -T{timing} {objetivo}"
        else:
            comando = comandos[opcion]
        
        ejecutar_comando(comando, guardar, f"port_scan_type_{opcion}")

def menu_deteccion_servicios():
    print("\n\033[1;96m🔧 DETECCIÓN DE SERVICIOS Y VERSIONES\033[0m")
    print("┌───────────┬─────────────────────────────────────────────────────────┐")
    print("│ \033[1;94mOpción\033[0m    │ Descripción                                                 │")
    print("├───────────┼─────────────────────────────────────────────────────────┤")
    print("│ \033[1;92m[1]\033[0m       │ Detección de versiones básica                               │")
    print("│ \033[1;92m[2]\033[0m       │ Detección de versiones agresiva                             │")
    print("│ \033[1;92m[3]\033[0m       │ Detección de SO                                             │")
    print("│ \033[1;92m[4]\033[0m       │ Scripts por defecto + versiones                             │")
    print("│ \033[1;92m[5]\033[0m       │ Escaneo completo agresivo                                   │")
    print("│ \033[1;92m[6]\033[0m       │ Detección de WAF/IPS/IDS                                    │")
    print("│ \033[1;92m[7]\033[0m       │ Banner grabbing                                             │")
    print("│ \033[1;92m[8]\033[0m       │ Identificación de tecnologías web                          │")
    print("└───────────┴─────────────────────────────────────────────────────────┘")
    
    opcion = input("\nSelecciona una opción: ").strip()
    
    if opcion in map(str, range(1, 9)):
        objetivo = input("Introduce el objetivo (IP o dominio): ").strip()
        if not es_ip_valida(objetivo):
            print("\033[1;91m[-] Objetivo no válido.\033[0m")
            return
        
        guardar = input("¿Guardar resultado en archivo? (s/n): ").strip().lower() == 's'
        
        comandos = {
            "1": f"nmap -sV {objetivo}",
            "2": f"nmap -sV --version-intensity 9 {objetivo}",
            "3": f"nmap -O {objetivo}",
            "4": f"nmap -sC -sV {objetivo}",
            "5": f"nmap -A {objetivo}",
            "6": f"nmap --script http-waf-detect,http-waf-fingerprint {objetivo}",
            "7": f"nmap --script banner {objetivo}",
            "8": f"nmap --script http-enum,http-headers,http-methods,http-webdav-scan {objetivo}"
        }
        
        ejecutar_comando(comandos[opcion], guardar, f"service_detection_{opcion}")

def menu_vulnerabilidades():
    print("\n\033[1;96m🛡️ DETECCIÓN DE VULNERABILIDADES\033[0m")
    print("┌───────────┬─────────────────────────────────────────────────────────┐")
    print("│ \033[1;94mOpción\033[0m    │ Descripción                                                 │")
    print("├───────────┼─────────────────────────────────────────────────────────┤")
    print("│ \033[1;92m[1]\033[0m       │ Escaneo general de vulnerabilidades                        │")
    print("│ \033[1;92m[2]\033[0m       │ Vulnerabilidades SMB                                       │")
    print("│ \033[1;92m[3]\033[0m       │ Vulnerabilidades SSH                                       │")
    print("│ \033[1;92m[4]\033[0m       │ Vulnerabilidades HTTP                                      │")
    print("│ \033[1;92m[5]\033[0m       │ Vulnerabilidades FTP                                       │")
    print("│ \033[1;92m[6]\033[0m       │ Vulnerabilidades SSL/TLS                                   │")
    print("│ \033[1;92m[7]\033[0m       │ Detección de malware                                       │")
    print("│ \033[1;92m[8]\033[0m       │ Escaneo completo con informe XML                           │")
    print("└───────────┴─────────────────────────────────────────────────────────┘")
    
    opcion = input("\nSelecciona una opción: ").strip()
    
    if opcion in map(str, range(1, 9)):
        objetivo = input("Introduce el objetivo (IP o dominio): ").strip()
        if not es_ip_valida(objetivo):
            print("\033[1;91m[-] Objetivo no válido.\033[0m")
            return
        
        guardar = input("¿Guardar resultado en archivo? (s/n): ").strip().lower() == 's'
        
        comandos = {
            "1": f"nmap --script vuln {objetivo}",
            "2": f"nmap --script smb-vuln* {objetivo}",
            "3": f"nmap --script ssh-* {objetivo}",
            "4": f"nmap --script http-vuln* {objetivo}",
            "5": f"nmap --script ftp-* {objetivo}",
            "6": f"nmap --script ssl-* {objetivo}",
            "7": f"nmap --script malware {objetivo}",
            "8": f"nmap -sV --script=vuln -oX vulns_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xml {objetivo}"
        }
        
        ejecutar_comando(comandos[opcion], guardar, f"vuln_scan_{opcion}")

def menu_enumeracion():
    print("\n\033[1;96m📋 ENUMERACIÓN DE SERVICIOS\033[0m")
    print("┌───────────┬─────────────────────────────────────────────────────────┐")
    print("│ \033[1;94mOpción\033[0m    │ Descripción                                                 │")
    print("├───────────┼─────────────────────────────────────────────────────────┤")
    print("│ \033[1;92m[1]\033[0m       │ Enumeración SMB completa                                    │")
    print("│ \033[1;92m[2]\033[0m       │ Enumeración SNMP                                           │")
    print("│ \033[1;92m[3]\033[0m       │ Enumeración DNS                                            │")
    print("│ \033[1;92m[4]\033[0m       │ Enumeración HTTP/HTTPS                                     │")
    print("│ \033[1;92m[5]\033[0m       │ Enumeración FTP                                            │")
    print("│ \033[1;92m[6]\033[0m       │ Enumeración SSH                                            │")
    print("│ \033[1;92m[7]\033[0m       │ Enumeración bases de datos                                 │")
    print("│ \033[1;92m[8]\033[0m       │ Enumeración LDAP                                           │")
    print("└───────────┴─────────────────────────────────────────────────────────┘")
    
    opcion = input("\nSelecciona una opción: ").strip()
    
    if opcion in map(str, range(1, 9)):
        objetivo = input("Introduce el objetivo (IP o dominio): ").strip()
        if not es_ip_valida(objetivo):
            print("\033[1;91m[-] Objetivo no válido.\033[0m")
            return
        
        guardar = input("¿Guardar resultado en archivo? (s/n): ").strip().lower() == 's'
        
        comandos = {
            "1": f"nmap --script smb-enum-*,smb-ls,smb-mbenum,smb-os-discovery,smb-security-mode,smb-server-stats,smb-system-info {objetivo}",
            "2": f"nmap -sU --script snmp-* {objetivo}",
            "3": f"nmap --script dns-* {objetivo}",
            "4": f"nmap --script http-*enum*,http-methods,http-webdav-scan {objetivo}",
            "5": f"nmap --script ftp-*enum*,ftp-anon {objetivo}",
            "6": f"nmap --script ssh-*enum*,ssh-auth-methods {objetivo}",
            "7": f"nmap --script mysql-*,ms-sql-*,oracle-*,mongodb-* {objetivo}",
            "8": f"nmap --script ldap-* {objetivo}"
        }
        
        ejecutar_comando(comandos[opcion], guardar, f"enum_{opcion}")

def menu_evasion():
    print("\n\033[1;96m🥷 TÉCNICAS DE EVASIÓN\033[0m")
    print("┌───────────┬─────────────────────────────────────────────────────────┐")
    print("│ \033[1;94mOpción\033[0m    │ Descripción                                                 │")
    print("├───────────┼─────────────────────────────────────────────────────────┤")
    print("│ \033[1;92m[1]\033[0m       │ Fragmentación de paquetes                                  │")
    print("│ \033[1;92m[2]\033[0m       │ Usar señuelos (decoys)                                     │")
    print("│ \033[1;92m[3]\033[0m       │ IP spoofing                                                │")
    print("│ \033[1;92m[4]\033[0m       │ Randomizar orden de puertos                                │")
    print("│ \033[1;92m[5]\033[0m       │ Escaneo ultra lento                                        │")
    print("│ \033[1;92m[6]\033[0m       │ Cambiar tamaño MTU                                         │")
    print("│ \033[1;92m[7]\033[0m       │ Usar proxy/Tor                                             │")
    print("└───────────┴─────────────────────────────────────────────────────────┘")
    
    opcion = input("\nSelecciona una opción: ").strip()
    
    if opcion in map(str, range(1, 8)):
        objetivo = input("Introduce el objetivo (IP o dominio): ").strip()
        if not es_ip_valida(objetivo):
            print("\033[1;91m[-] Objetivo no válido.\033[0m")
            return
        
        if opcion == "1":
            comando = f"nmap -f {objetivo}"
        elif opcion == "2":
            decoys = input("Introduce IPs señuelo separadas por comas: ").strip()
            comando = f"nmap -D {decoys} {objetivo}"
        elif opcion == "3":
            ip_falsa = input("Introduce IP falsa: ").strip()
            comando = f"nmap -S {ip_falsa} {objetivo}"
        elif opcion == "4":
            comando = f"nmap --randomize-hosts {objetivo}"
        elif opcion == "5":
            comando = f"nmap -T0 {objetivo}"
        elif opcion == "6":
            mtu = input("Introduce tamaño MTU (múltiplo de 8): ").strip()
            comando = f"nmap --mtu {mtu} {objetivo}"
        elif opcion == "7":
            proxy = input("Introduce proxy (formato: tipo://ip:puerto): ").strip()
            comando = f"nmap --proxies {proxy} {objetivo}"
        
        ejecutar_comando(comando, True, f"evasion_{opcion}")

def menu_scripts_personalizados():
    print("\n\033[1;96m⚡ SCRIPTS PERSONALIZADOS\033[0m")
    print("┌───────────┬─────────────────────────────────────────────────────────┐")
    print("│ \033[1;94mOpción\033[0m    │ Descripción                                                 │")
    print("├───────────┼─────────────────────────────────────────────────────────┤")
    print("│ \033[1;92m[1]\033[0m       │ Ejecutar script específico                                  │")
    print("│ \033[1;92m[2]\033[0m       │ Listar scripts disponibles                                  │")
    print("│ \033[1;92m[3]\033[0m       │ Scripts de categoría específica                             │")
    print("│ \033[1;92m[4]\033[0m       │ Combo: Discovery + Enum + Vuln                             │")
    print("│ \033[1;92m[5]\033[0m       │ Escaneo completo automatizado                               │")
    print("└───────────┴─────────────────────────────────────────────────────────┘")
    
    opcion = input("\nSelecciona una opción: ").strip()
    
    if opcion == "1":
        script = input("Introduce el nombre del script: ").strip()
        objetivo = input("Introduce el objetivo: ").strip()
        if es_ip_valida(objetivo):
            ejecutar_comando(f"nmap --script {script} {objetivo}", True, "custom_script")
    elif opcion == "2":
        ejecutar_comando("nmap --script-help all | grep -E '^[a-z]'", False)
    elif opcion == "3":
        print("Categorías: auth, broadcast, brute, default, discovery, dos, exploit, external, fuzzer, intrusive, malware, safe, version, vuln")
        categoria = input("Introduce categoría: ").strip()
        objetivo = input("Introduce el objetivo: ").strip()
        if es_ip_valida(objetivo):
            ejecutar_comando(f"nmap --script {categoria} {objetivo}", True, f"category_{categoria}")
    elif opcion == "4":
        objetivo = input("Introduce el objetivo: ").strip()
        if es_ip_valida(objetivo):
            comando = f"nmap -sS -sV -sC --script discovery,enumeration,vuln -A {objetivo}"
            ejecutar_comando(comando, True, "combo_scan")
    elif opcion == "5":
        objetivo = input("Introduce el objetivo: ").strip()
        if es_ip_valida(objetivo):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            comando = f"nmap -sS -sV -sC -A -p- --script vuln,enum,discovery -oA full_scan_{timestamp} {objetivo}"
            ejecutar_comando(comando, True, "full_automated")

def mostrar_estadisticas():
    """Mostrar estadísticas de los escaneos realizados"""
    print("\n\033[1;96m📊 ESTADÍSTICAS DE ESCANEOS\033[0m")
    print("═" * 60)
    
    try:
        with open('nmap_scans.log', 'r') as f:
            contenido = f.read()
            total_comandos = contenido.count('Comando ejecutado:')
            total_errores = contenido.count('Error en el comando:')
            
        archivos_generados = len([f for f in os.listdir('.') if f.endswith(('.txt', '.xml', '.nmap'))])
        
        print(f"• Total de comandos ejecutados: {total_comandos}")
        print(f"• Total de errores: {total_errores}")
        print(f"• Archivos generados: {archivos_generados}")
        print(f"• Tasa de éxito: {((total_comandos - total_errores) / total_comandos * 100):.1f}%" if total_comandos > 0 else "N/A")
        
    except FileNotFoundError:
        print("No se han realizado escaneos aún.")
    
    input("\nPresiona Enter para continuar...")

def exportar_resultados():
    """Exportar todos los resultados en un solo archivo"""
    print("\n\033[1;96m📤 EXPORTAR RESULTADOS\033[0m")
    print("═" * 60)
    
    archivos = [f for f in os.listdir('.') if f.endswith(('.txt', '.xml', '.nmap'))]
    
    if not archivos:
        print("\033[1;93mNo hay archivos para exportar.\033[0m")
        input("\nPresiona Enter para continuar...")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo_exportacion = f"nmap_results_export_{timestamp}.txt"
    
    try:
        with open(archivo_exportacion, 'w') as export_file:
            export_file.write("=" * 80 + "\n")
            export_file.write("REPORTE CONSOLIDADO DE ESCANEOS NMAP\n")
            export_file.write(f"Generado: {datetime.now()}\n")
            export_file.write("Team Poisonous - Nmap Automation Tool v2.0\n")
            export_file.write("=" * 80 + "\n\n")
            
            for archivo in archivos:
                try:
                    with open(archivo, 'r') as f:
                        contenido = f.read()
                    export_file.write(f"\n{'='*20} {archivo} {'='*20}\n")
                    export_file.write(contenido)
                    export_file.write(f"\n{'='*60}\n")
                except Exception as e:
                    export_file.write(f"Error leyendo {archivo}: {str(e)}\n")
        
        print(f"\033[1;92m[+] Resultados exportados a: {archivo_exportacion}\033[0m")
        
    except Exception as e:
        print(f"\033[1;91m[-] Error exportando: {str(e)}\033[0m")
    
    input("\nPresiona Enter para continuar...")

def limpiar_archivos():
    """Limpiar archivos de resultados antiguos"""
    print("\n\033[1;96m🧹 LIMPIAR ARCHIVOS\033[0m")
    print("═" * 60)
    
    archivos = [f for f in os.listdir('.') if f.endswith(('.txt', '.xml', '.nmap', '.gnmap'))]
    
    if not archivos:
        print("\033[1;93mNo se encontraron archivos de escaneo.\033[0m")
        input("\nPresiona Enter para continuar...")
        return
    
    print("\nArchivos encontrados:")
    for i, archivo in enumerate(archivos, 1):
        print(f"{i}. {archivo}")
    
    print("\nOpciones:")
    print("  [a] Eliminar TODOS los archivos")
    print("  [s] Seleccionar archivos específicos")
    print("  [c] Cancelar")
    
    opcion = input("\nSelecciona una opción: ").lower().strip()
    
    if opcion == 'a':
        confirmacion = input("¿Estás seguro de eliminar TODOS los archivos? (s/n): ").lower().strip()
        if confirmacion == 's':
            for archivo in archivos:
                try:
                    os.remove(archivo)
                    print(f"\033[1;92m[+] Eliminado: {archivo}\033[0m")
                except Exception as e:
                    print(f"\033[1;91m[-] Error eliminando {archivo}: {str(e)}\033[0m")
    elif opcion == 's':
        seleccion = input("Introduce los números de archivo separados por comas: ").strip()
        indices = [int(i.strip()) - 1 for i in seleccion.split(',') if i.strip().isdigit()]
        
        for idx in indices:
            if 0 <= idx < len(archivos):
                try:
                    os.remove(archivos[idx])
                    print(f"\033[1;92m[+] Eliminado: {archivos[idx]}\033[0m")
                except Exception as e:
                    print(f"\033[1;91m[-] Error eliminando {archivos[idx]}: {str(e)}\033[0m")
    else:
        print("\033[1;93mOperación cancelada.\033[0m")
    
    input("\nPresiona Enter para continuar...")

def main():
    banner()
    while True:
        print("\n\033[1;95m" + "═"*60 + "\033[0m")
        print("\033[1;94m" + "MENÚ PRINCIPAL".center(60) + "\033[0m")
        print("\033[1;95m" + "═"*60 + "\033[0m")
        print("┌───────────┬─────────────────────────────────────────────────────────┐")
        print("│ \033[1;94mOpción\033[0m    │ Descripción                                                 │")
        print("├───────────┼─────────────────────────────────────────────────────────┤")
        print("│ \033[1;92m[1]\033[0m       │ Descubrimiento de Red                                      │")
        print("│ \033[1;92m[2]\033[0m       │ Escaneo de Puertos                                         │")
        print("│ \033[1;92m[3]\033[0m       │ Detección de Servicios y Versiones                        │")
        print("│ \033[1;92m[4]\033[0m       │ Detección de Vulnerabilidades                             │")
        print("│ \033[1;92m[5]\033[0m       │ Enumeración de Servicios                                   │")
        print("│ \033[1;92m[6]\033[0m       │ Técnicas de Evasión                                       │")
        print("│ \033[1;92m[7]\033[0m       │ Scripts Personalizados                                    │")
        print("│ \033[1;92m[8]\033[0m       │ Estadísticas de Escaneos                                  │")
        print("│ \033[1;92m[9]\033[0m       │ Exportar Resultados                                       │")
        print("│ \033[1;92m[10]\033[0m      │ Limpiar Archivos                                          │")
        print("│ \033[1;91m[0]\033[0m       │ Salir                                                      │")
        print("└───────────┴─────────────────────────────────────────────────────────┘")
        
        opcion = input("\nSelecciona una opción: ").strip()
        
        if opcion == "1":
            menu_descubrimiento_red()
        elif opcion == "2":
            menu_escaneo_puertos()
        elif opcion == "3":
            menu_deteccion_servicios()
        elif opcion == "4":
            menu_vulnerabilidades()
        elif opcion == "5":
            menu_enumeracion()
        elif opcion == "6":
            menu_evasion()
        elif opcion == "7":
            menu_scripts_personalizados()
        elif opcion == "8":
            mostrar_estadisticas()
        elif opcion == "9":
            exportar_resultados()
        elif opcion == "10":
            limpiar_archivos()
        elif opcion == "0":
            print("\n\033[1;92m[+] Saliendo del programa. ¡Hasta pronto!\033[0m")
            break
        else:
            print("\033[1;91m[-] Opción no válida. Inténtalo de nuevo.\033[0m")

if __name__ == "__main__":
    main()
