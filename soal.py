import random

tipe = input('+ = penjumlahan\n- = pengurangan\nx = perkalian\n: = pembagian\nPilih tipe = ')
banyak = int(input('Banyak soal yang diinginkan = '))
jarak = int(input('Range angka ='))
score = 0

def cekbanyak():
    for _ in range (banyak):
        cekjarak()


def cekjarak():
    angka1 = random.randint(0,jarak)
    if tipe == ':':
        angka2 = random.randint(1,jarak)
    else : 
        angka2 = random.randint(0,jarak)
    print (angka1, tipe, angka2)
    x = input('= ')
    cekjawab(x,angka1,angka2)


def cekjawab(x,angka1,angka2):
    global score
    if tipe == '+':
        x = int(x)
        y = angka1 + angka2
        if x == y:
            print ('betul')
            score+=1
        else:
            print ('salah')
            print(y)

    if tipe == '-':
        x = int(x)
        y = angka1 - angka2
        if x == y:
            print ('betul')
            score+=1
        else:
            print ('salah')
            print(y)

    if tipe == 'x':
        x = int(x)
        y = angka1 * angka2
        if x == y:
            print ('betul')
            score+=1
        else:
            print ('salah')
            print(y)

    if tipe == ':':
        x = float(x)
        y = round((angka1 / angka2),2)
        if x == y:
            print ('betul')
            score+=1
        else:
            print ('salah')
            print (y)


cekbanyak()
print ('score =',score)
nilai = int((round(score / banyak,2))*100)
print ('nilai=',nilai)