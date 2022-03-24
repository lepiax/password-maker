import random
banner = """
██╗     ███████╗██████╗ ██╗ █████╗ ██╗  ██╗                                    
██║     ██╔════╝██╔══██╗██║██╔══██╗╚██╗██╔╝                                    
██║     █████╗  ██████╔╝██║███████║ ╚███╔╝                                     
██║     ██╔══╝  ██╔═══╝ ██║██╔══██║ ██╔██╗                                     
███████╗███████╗██║     ██║██║  ██║██╔╝ ██╗                                    
╚══════╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝                                    

██████╗  █████╗ ███████╗███████╗    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██████╔╝███████║███████╗███████╗    ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║    ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
██║     ██║  ██║███████║███████║    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""
print(banner)

karakter = 'abcçdefgğhıijklmnoöprsştuüvyz1234567890ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ!@#$%^&*'

while True:
    try:
        numara = int(input("[+] Number of passwords to be created: "))
        break
    except ValueError:
        print("Enter numeric value.")
        continue

while True:
    try:
        uzunluk = int(input("[-] Enter the password length: "))
        break
    except ValueError:
        print("Enter numeric value.")
        continue

for passw in range(numara):
    parola = ""
    for char in range(uzunluk):
        

        parola += random.choice(karakter)
    

print("[+] Parolanız: {}".format(parola))
    

