import sys
import socket
from datetime import datetime

def check_port(ip, port, timeout):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout((timeout))
    answ = s.connect_ex((ip, port))

    if answ == 0:
        print(f"[+] Port {port} is open!")
    else:
        print(f"[-] Port {port} is closed...")

    s.settimeout(None)
    s.close()

HOST = '127.0.0.1'
PORT = 1
START = 1
END = 1000
TIMEOUT = 0.01

if __name__ == "__main__":
    try:
        if sys.argv[1].count('.') >= 1:
            print("[+] Ip is ok...")
            HOST = socket.gethostbyname(sys.argv[1])

            all_args = sys.argv[2:len(sys.argv[1])]
            if len(all_args) % 2 != 0:
                print("[!] Please specifiy all given options")
                sys.exit()

            options = all_args[::2]
            values = all_args[1::2]

            for arg in options:
                if arg == "-sP":
                    START = int(values[options.index(arg)])
                    continue
                if arg == "-eP":
                    END = int(values[options.index(arg)])
                    continue
                if arg == "-t":
                    TIMEOUT = int(values[options.index(arg)])
                    continue

            else:
                print("[!] Unknow option: {arg.split('-'.[1]}!")
                sys.exit()

        if START > END:
            print("[!] Start port can't be higher than end")
            sys.exit()
        if START <= 0 or END <= 0 or TIMEOUT <= 0:
            print("[!] Given ports or timeout can't be lower than 1 (timeout - 0)")
            sys.exit()

        print(f"HOST: {HOST}\nSTART {START}\n END {END}\nTIMEOUT")