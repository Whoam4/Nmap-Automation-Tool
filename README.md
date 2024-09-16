# Nmap

## 👁️‍🗨️​ Nmap CheatSheet

| Command                                       | Description                                            |
|-----------------------------|--------------------------------------------------------|
| nmap-v-script vuln TARGET                   | Simple host scan                                       |
| nmap <start_ip>-<end_ip>                    | Scanning IP address ranges                             |   
| nmap -p <port_range> <host>                 | Scanning a range of ports                              |
| nmap -p- <host>                             | Scan all ports                                         |
| nmap -p 1-1000 <host>                       | Scanning of the 1000 most common ports                 |
| nmap -sV <host>                             | Scanning services and versions                         |
| nmap -T5 -F <host>                          | Quick scan without DNS resolution                      |
| nmap -O <host>                              | Scanning operating systems                             |
| nmap --script vuln <host>                   | Vulnerability script scannings                         |
| nmap --script <script_name> <host>          | Scanning for specific scripts                   |
| nmap -sS <host>                             | Stealth scanning (does not generate logs at destination)|
| nmap -sU <host>                             | UDP scanning                                           |
| nmap -sn <network>                          | Scanning live hosts on a network                       |
| nmap -oX output.xml <host>                  | Save results in XML format                             |

