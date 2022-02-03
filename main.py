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
        numara = int(input("[+] Oluşturulacak parola sayısı: "))
        break
    except ValueError:
        print("Sayısal değer giriniz.")
        continue

while True:
    try:
        uzunluk = int(input("[-] Parola uzunluğunu giriniz: "))
        break
    except ValueError:
        print("Sayısal değer giriniz.")
        continue

for passw in range(numara):
    parola = ""
    for char in range(uzunluk):
        

        parola += random.choice(karakter)
    

print("[+] Parolanız: {}".format(parola))
    

