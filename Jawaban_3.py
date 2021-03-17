#Soal 4
a=int(input('Masukkan Jumlah Baris: '))
def segitiga(a):
    print(' '*(a-1) + '***'+' '*(a-1))
    z=1
    for i in range(a-2,0,-1):
        space = ' '* i
        star = '**'
        print(space + star +(' '*z)+star)
        z+=2
    print('*'*(2*a +1))
segitiga(a)