print("PELUANG KOIN DAN DADU")

def koin():
    a = int(input("masukkan peluang satu koin :"))
    n = int(input("masukkan jumlah lemparan koin:"))
    p = a**n
    print ("peluang dari", n, "koin adalah",p)
    
def dadu():
    a = int(input("masukkan peluang satu dadu :"))
    n = int(input("masukkan jumlah lemparan dadu:"))
    p = a**n
    print ("peluang dari", n, "dadu adalah",p)

print("Mau menghitung apa?")
print("A.peluang koin")
print("B.peluang dadu")
jwb=str(input("ketikkan A atau B:"))
if jwb =='A':
    koin()
elif jwb=='B':
    dadu()
else:
    print("sorry,pilihlah A atau B")
