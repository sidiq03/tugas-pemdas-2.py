'''fungsi pada python didefinisikan dengan def'''

'''def nama_fungsi():'''

def salam():
    print("Assalamualaikum !! Akhi Ukhty")

salam()
salam()
salam()

'''buatlah sebuah versi kalian'''

def haii():
    print("hai !! cewe")

haii()
haii()
haii()

'''fungsi dengan paerameter'''
'''def nama_fungsi(p1, p2)'''

def say_hi(nama):
    print("Halo perkenalkan nama saya", nama)

say_hi("dower")
say_hi("riski")

'''buatlah fungsi dengan 3 parametee'''

def beban_orangtua(beban1, beban2, beban3):
    print("beban orang tua yaitu" + beban1) 
    print("beban orang tua yaitu" + beban2)
    print("beban orang tua yaitu" + beban3)

beban_orangtua(beban1 = "riski", beban2 = "imam", beban3 = "dika")

def perkenalkan(nama, alamat, umur):
    print("nama saya:", nama)
    print("alamat saya:", alamat)
    print("umur saya:", umur)
perkenalkan("sidiq", "margonda", "16")
print("\n\n======= BATAS =======\n\n")
perkenalkan("imam", "margonda", "18")