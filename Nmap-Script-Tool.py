import subprocess
import re
import logging

# Configuración del logging
logging.basicConfig(filename='nmap_scans.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def banner():
    print("\033[1;92m")
    print("  /$$      /$$                     /$$           ")
    print(" | $$$    /$$$                    |__/           ")
    print(" | $$$$  /$$$$  /$$$$$$   /$$$$$$  /$$  /$$$$$$  ")
    print(" | $$ $$/$$ $$ |____  $$ /$$__  $$| $$ /$$__  $$ ")
    print(" | $$  $$$| $$  /$$$$$$$| $$  \\__/| $$| $$  \\ $$ ")
    print(" | $$\\  $ | $$ /$$__  $$| $$      | $$| $$  | $$ ")
    print(" | $$ \\/  | $$|  $$$$$$$| $$      | $$|  $$$$$$/ ")
    print(" |__/     |__/ \\_______/|__/      |__/ \\______/  ")
    print("\033[0m")
    print("Herramienta de automatización de Nmap")
    print("Creado por DK Mario\n")

def es_ip_valida(ip):
    """Validar si una IP o rango es válido."""
    patron = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?:/[0-9]{1,2})?$")
    return patron.match(ip) is not None

def ejecutar_comando(comando):
    try:
        print(f"\n\033[1;93mEjecutando: {comando}\033[0m\n")
        resultado = subprocess.run(comando, shell=True, text=True, capture_output=True)
        print(resultado.stdout)
        logging.info(f'Comando ejecutado: {comando}\nSalida:\n{resultado.stdout}')
        if resultado.stderr:
            print(f"\033[1;91mError: {resultado.stderr}\033[0m")
            logging.error(f'Error en el comando: {comando}\nError:\n{resultado.stderr}')
    except Exception as e:
        print(f"\033[1;91mOcurrió un error: {str(e)}\033[0m")
        logging.error(f'Ocurrió un error: {str(e)}')

def menu_deteccion_vulnerabilidades():
    print("\n\033[1;96mDetección de Vulnerabilidades\033[0m")
    print("┌───────────┬───────────────────────────────────────────────────┐")
    print("│ \033[1;94mOpción\033[0m    │ Descripción                                          │")
    print("├───────────┼───────────────────────────────────────────────────┤")
    print("│ \033[1;92m[1]\033[0m       │ Detección de vulnerabilidades                        │")
    print("│ \033[1;92m[2]\033[0m       │ Escaneo completo con detección de vulnerabilidades   │")
    print("│ \033[1;92m[3]\033[0m       │ Informe de vulnerabilidades                          │")
    print("└───────────┴───────────────────────────────────────────────────┘")
    opcion = input("\nSelecciona una opción: ").strip()

    if opcion in ["1", "2", "3"]:
        objetivo = input("Introduce el objetivo (IP o dominio): ").strip()
        if not es_ip_valida(objetivo):
            print("\033[1;91mIP o dominio no válido. Por favor, introduce una IP o dominio correcto.\033[0m")
            return
        if opcion == "1":
            ejecutar_comando(f"nmap -v --script vuln {objetivo}")
        elif opcion == "2":
            ejecutar_comando(f"sudo nmap -v -sS -sC -sV -T5 --script=vuln {objetivo}")
        elif opcion == "3":
            ejecutar_comando(f"sudo nmap -v -sS -sC -sV -T5 --script=vuln -oX vulns.xml --webxml {objetivo}")
    else:
        print("\033[1;91mOpción no válida. Volviendo al menú principal.\033[0m")

def menu_smb_enumeration():
    print("\n\033[1;96mSMB Enumeration\033[0m")
    print("┌───────────┬───────────────────────────────────────────────────┐")
    print("│ \033[1;94mOpción\033[0m    │ Descripción                                              │")
    print("├───────────┼───────────────────────────────────────────────────┤")
    print("│ \033[1;92m[1]\033[0m       │ Enumeración de Usuarios SMB                              │")
    print("│ \033[1;92m[2]\033[0m       │ Escaneo de SMB para Vulnerabilidades Comunes             │")
    print("│ \033[1;92m[3]\033[0m       │ Enumeración de Recursos Compartidos                      │")
    print("│ \033[1;92m[4]\033[0m       │ Enumeración de Políticas de Seguridad SMB                │")
    print("│ \033[1;92m[5]\033[0m       │ Obtención de Información de la Versión del Protocolo SMB │")
    print("└───────────┴───────────────────────────────────────────────────┘")
    opcion = input("\nSelecciona una opción: ").strip()

    if opcion in ["1", "2", "3", "4", "5"]:
        objetivo = input("Introduce el objetivo (IP o dominio): ").strip()
        if not es_ip_valida(objetivo):
            print("\033[1;91mIP o dominio no válido. Por favor, introduce una IP o dominio correcto.\033[0m")
            return
        if opcion == "1":
            ejecutar_comando(f"smbclient -L \\\\{objetivo} -U \"\"")
        elif opcion == "2":
            ejecutar_comando(f"nmap --script smb-vuln* {objetivo}")
        elif opcion == "3":
            usuario = input("Introduce el nombre de usuario: ").strip()
            ejecutar_comando(f"smbclient -L \\\\{objetivo} -U {usuario}")
        elif opcion == "4":
            ejecutar_comando(f"sudo nmap -p 139,445 --script smb-security-mode {objetivo}")
        elif opcion == "5":
            ejecutar_comando(f"sudo nmap -p 139,445 --script smb-protocols {objetivo}")
    else:
        print("\033[1;91mOpción no válida. Volviendo al menú principal.\033[0m")

def menu_comandos_basicos():
    print("\n\033[1;96mComandos Básicos de Nmap\033[0m")
    print("┌───────────┬───────────────────────────────────────────────────┐")
    print("│ \033[1;94mOpción\033[0m    │ Descripción                                        │")
    print("├───────────┼───────────────────────────────────────────────────┤")
    print("│ \033[1;92m[1]\033[0m       │ Reconocimiento de Hosts                            │")
    print("│ \033[1;92m[2]\033[0m       │ Descubrir todos los nodos de la red                │")
    print("│ \033[1;92m[3]\033[0m       │ Descubrir puertos abiertos                         │")
    print("│ \033[1;92m[4]\033[0m       │ Escaneo de servicios                               │")
    print("│ \033[1;92m[5]\033[0m       │ Escaneo de versiones de servicios                  │")
    print("│ \033[1;92m[6]\033[0m       │ Detección de sistema operativo                     │")
    print("│ \033[1;92m[7]\033[0m       │ Escaneo de puertos específicos                     │")
    print("│ \033[1;92m[8]\033[0m       │ Escaneo de scripts personalizados                  │")
    print("│ \033[1;92m[9]\033[0m       │ Escaneo de red completo                            │")
    print("│ \033[1;92m[10]\033[0m      │ Detección de dispositivos de red                   │")
    print("└───────────┴───────────────────────────────────────────────────┘")
    opcion = input("\nSelecciona una opción: ").strip()

    if opcion in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        objetivo = input("Introduce el objetivo (IP o dominio): ").strip()
        if not es_ip_valida(objetivo):
            print("\033[1;91mIP o dominio no válido. Por favor, introduce una IP o dominio correcto.\033[0m")
            return
        if opcion == "1":
            ejecutar_comando(f"nmap -sn {objetivo}")
        elif opcion == "2":
            ejecutar_comando("nmap -sn 192.168.1.0/24")
        elif opcion == "3":
            ejecutar_comando(f"nmap -p- {objetivo}")
        elif opcion == "4":
            ejecutar_comando(f"nmap -sS {objetivo}")
        elif opcion == "5":
            ejecutar_comando(f"nmap -sV {objetivo}")
        elif opcion == "6":
            ejecutar_comando(f"nmap -O {objetivo}")
        elif opcion == "7":
            puertos = input("Introduce los puertos que deseas escanear (ej. 22,80,443): ")
            ejecutar_comando(f"nmap -p {puertos} {objetivo}")
        elif opcion == "8":
            script = input("Introduce el script que deseas usar: ")
            ejecutar_comando(f"nmap --script {script} {objetivo}")
        elif opcion == "9":
            ejecutar_comando(f"nmap -A {objetivo}")
        elif opcion == "10":
            ejecutar_comando(f"nmap -sP {objetivo}")
    else:
        print("\033[1;91mOpción no válida. Volviendo al menú principal.\033[0m")

def menu_principal():
    while True:
        banner()
        print("┌───────────┬───────────────────────────────────────────────────┐")
        print("│ \033[1;94mOpción\033[0m    │ Descripción                                       │")
        print("├───────────┼───────────────────────────────────────────────────┤")
        print("│ \033[1;92m[1]\033[0m       │ Detección de vulnerabilidades                     │")
        print("│ \033[1;92m[2]\033[0m       │ SMB Enumeration                                   │")
        print("│ \033[1;92m[3]\033[0m       │ Comandos básicos de Nmap                          │")
        print("│ \033[1;92m[4]\033[0m       │ Ayuda                                             │")
        print("│ \033[1;92m[5]\033[0m       │ Salir                                             │")
        print("└───────────┴───────────────────────────────────────────────────┘")
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            menu_deteccion_vulnerabilidades()
        elif opcion == "2":
            menu_smb_enumeration()
        elif opcion == "3":
            menu_comandos_basicos()
        elif opcion == "4":
            print("\n\033[1;96mAyuda\033[0m")
            print("Puedes encontrar más información y el código fuente de esta herramienta en GitHub:")
            print("\033[1;94mhttps://github.com/Whoam4/Nmap-CheatSheet/blob/main/Sheet.md\033[0m")  # Reemplaza con tu URL
            input("\nPresiona Enter para volver al menú principal...")
        elif opcion == "5":
            print("\033[1;92mSaliendo...\033[0m")
            break
        else:
            print("\033[1;91mOpción no válida. Por favor, selecciona una opción correcta.\033[0m")

if __name__ == "__main__":
    menu_principal()